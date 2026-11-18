/* Keep the native mobile disclosure menu usable by keyboard and pointer. */
document.querySelectorAll(".mobile-nav").forEach(function (menu) {
  var summary = menu.querySelector("summary");
  if (!summary) return;

  function syncMenuLabel() {
    summary.setAttribute("aria-label", menu.open ? "Close navigation menu" : "Open navigation menu");
  }

  syncMenuLabel();
  menu.addEventListener("toggle", syncMenuLabel);

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && menu.open) {
      menu.open = false;
      summary.focus();
    }
  });

  document.addEventListener("pointerdown", function (event) {
    if (menu.open && !menu.contains(event.target)) {
      menu.open = false;
    }
  });
});

// Make only horizontally overflowing paper tables keyboard-scrollable.
function updatePaperTableFocus() {
  document.querySelectorAll('.symmetria-article-page .paper-content table').forEach(function (table) {
    if (table.scrollWidth > table.clientWidth + 1) table.setAttribute('tabindex', '0');
    else table.removeAttribute('tabindex');
  });
}
updatePaperTableFocus();
window.addEventListener('resize', updatePaperTableFocus);


/* Add separate-tab full-resolution image links without editing the original paper text or figure markup. */
document.querySelectorAll(".symmetria-article-page .paper-content img").forEach(function (figure) {
  const source = figure.getAttribute("src");
  if (!source || !/^\.\.\/\.\.\/images\/symmetria\/paper-0[1-4]\/[a-zA-Z0-9_-]+\.webp$/.test(source) || figure.closest("a")) return;

  const link = document.createElement("a");
  link.className = "paper-figure-open";
  const viewer = new URL("../../pages/figure-viewer.html", document.baseURI);
  viewer.searchParams.set("src", source.slice(6));
  viewer.searchParams.set("alt", figure.getAttribute("alt") || "SYMMETRIA figure");
  link.href = viewer.href;
  link.target = "_blank";
  link.rel = "noopener";
  link.setAttribute("aria-label", "Open interactive image viewer in a new tab: " + (figure.getAttribute("alt") || "SYMMETRIA figure"));
  link.title = "Mouse wheel or pinch to zoom; drag to pan. Original image available in the viewer.";

  const label = document.createElement("span");
  label.className = "paper-figure-open-label";
  label.setAttribute("aria-hidden", "true");
  label.textContent = "Open interactive image viewer ↗";

  figure.parentNode.insertBefore(link, figure);
  link.appendChild(figure);
  link.appendChild(label);
});
