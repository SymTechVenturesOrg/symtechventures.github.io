(() => {
  "use strict";
  const params = new URLSearchParams(location.search);
  const requested = params.get("src") || "";
  const allowed = /^images\/symmetria\/paper-0[1-4]\/[A-Za-z0-9_-]+\.webp$/;
  const stage = document.getElementById("image-stage");
  const image = document.getElementById("full-image");
  const title = document.getElementById("figure-title");
  const original = document.getElementById("original-image");
  const message = document.getElementById("viewer-error");
  const zoomValue = document.getElementById("zoom-value");
  const controls = ["zoom-out", "zoom-in", "zoom-fit", "zoom-actual"].map(id => document.getElementById(id));
  if (!allowed.test(requested)) {
    message.hidden = false;
    controls.forEach(control => control.disabled = true);
    return;
  }

  const description = (params.get("alt") || "SYMMETRIA illustration").trim().slice(0,180);
  title.textContent = description;
  image.alt = description;
  const url = new URL("../" + requested, location.href);
  original.href = url.href;
  original.hidden = false;

  let naturalWidth = 0;
  let naturalHeight = 0;
  let fit = 1;
  let zoom = 1;
  let panX = 0;
  let panY = 0;
  const active = new Map();

  function fitLevel() {
    return Math.min(stage.clientWidth / naturalWidth, stage.clientHeight / naturalHeight);
  }

  function bounds() {
    const maxX = Math.max(0, (naturalWidth * zoom - stage.clientWidth) / 2);
    const maxY = Math.max(0, (naturalHeight * zoom - stage.clientHeight) / 2);
    panX = Math.min(maxX, Math.max(-maxX, panX));
    panY = Math.min(maxY, Math.max(-maxY, panY));
  }

  function draw() {
    bounds();
    image.style.left = (stage.clientWidth / 2 + panX) + "px";
    image.style.top = (stage.clientHeight / 2 + panY) + "px";
    image.style.transform = "scale(" + zoom + ") translate(-50%, -50%)";
    zoomValue.value = Math.round(zoom * 100) + "%";
    zoomValue.textContent = zoomValue.value;
  }

  function setZoom(next, clientX, clientY) {
    if (!naturalWidth || !naturalHeight) return;
    const before = zoom;
    const maximum = Math.max(8, fit * 12);
    const minimum = Math.min(fit * .5, .25);
    zoom = Math.max(minimum, Math.min(maximum, next));
    const rect = stage.getBoundingClientRect();
    const x = clientX === undefined ? rect.left + rect.width / 2 : clientX;
    const y = clientY === undefined ? rect.top + rect.height / 2 : clientY;
    const offsetX = x - rect.left - rect.width / 2;
    const offsetY = y - rect.top - rect.height / 2;
    panX = offsetX - (offsetX - panX) * zoom / before;
    panY = offsetY - (offsetY - panY) * zoom / before;
    draw();
  }

  function resetFit() {
    if (!naturalWidth) return;
    fit = fitLevel();
    zoom = fit;
    panX = 0;
    panY = 0;
    draw();
  }

  image.addEventListener("load", () => {
    naturalWidth = image.naturalWidth;
    naturalHeight = image.naturalHeight;
    if (!naturalWidth || !naturalHeight) {
      message.hidden = false;
      return;
    }
    image.style.width = naturalWidth + "px";
    image.style.height = naturalHeight + "px";
    image.hidden = false;
    resetFit();
    controls.forEach(control => control.disabled = false);
  });

  image.addEventListener("error", () => {
    message.hidden = false;
    controls.forEach(control => control.disabled = true);
  });
  controls.forEach(control => control.disabled = true);
  image.src = url.href;

  controls[0].addEventListener("click", () => setZoom(zoom / 1.25));
  controls[1].addEventListener("click", () => setZoom(zoom * 1.25));
  controls[2].addEventListener("click", resetFit);
  controls[3].addEventListener("click", () => setZoom(1));

  stage.addEventListener("wheel", event => {
    if (!naturalWidth) return;
    event.preventDefault();
    const delta = Math.max(-400, Math.min(400, event.deltaY));
    setZoom(zoom * Math.exp(-delta * .0015), event.clientX, event.clientY);
  }, { passive: false });

  function pair() {
    const points = [...active.values()];
    if (points.length < 2) return null;
    return { x:(points[0].x + points[1].x)/2,
             y:(points[0].y + points[1].y)/2,
             distance:Math.hypot(points[0].x - points[1].x, points[0].y - points[1].y) };
  }

  stage.addEventListener("pointerdown", event => {
    if (!naturalWidth || event.target.closest("button,a")) return;
    if (event.pointerType === "mouse" && event.button !== 0) return;
    active.set(event.pointerId, {x:event.clientX, y:event.clientY});
    try { stage.setPointerCapture(event.pointerId); } catch (_) {}
    stage.classList.add("is-grabbing");
  });

  stage.addEventListener("pointermove", event => {
    const previous = active.get(event.pointerId);
    if (!previous) return;
    const oldPair = pair();
    active.set(event.pointerId, {x:event.clientX, y:event.clientY});
    if (active.size >= 2 && oldPair) {
      const current = pair();
      if (oldPair.distance > 0 && current.distance > 0) {
        setZoom(zoom * current.distance / oldPair.distance, current.x, current.y);
        panX += current.x - oldPair.x;
        panY += current.y - oldPair.y;
      }
    } else {
      panX += event.clientX - previous.x;
      panY += event.clientY - previous.y;
    }
    draw();
  });

  function release(event) {
    active.delete(event.pointerId);
    if (active.size === 0) stage.classList.remove("is-grabbing");
  }
  stage.addEventListener("pointerup", release);
  stage.addEventListener("pointercancel", release);
  stage.addEventListener("lostpointercapture", release);

  document.addEventListener("keydown", event => {
    if (event.altKey || event.ctrlKey || event.metaKey) return;
    const t = event.target;
    if (t && /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return;
    if (["+", "="].includes(event.key)) {event.preventDefault();setZoom(zoom * 1.25);}
    else if (event.key === "-") {event.preventDefault();setZoom(zoom / 1.25);}
    else if (event.key === "0") {event.preventDefault();resetFit();}
    else if (["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].includes(event.key) && document.activeElement === stage) {
      event.preventDefault();
      const step = 64;
      panX += event.key === "ArrowLeft" ? step : event.key === "ArrowRight" ? -step : 0;
      panY += event.key === "ArrowUp" ? step : event.key === "ArrowDown" ? -step : 0;
      draw();
    }
  });

  const onResize = () => {
    if (!naturalWidth) return;
    const wasFit = Math.abs(zoom - fit) < .001;
    fit = fitLevel();
    if (wasFit) resetFit();
    else draw();
  };
  window.addEventListener("resize", onResize);
})();
