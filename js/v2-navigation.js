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
