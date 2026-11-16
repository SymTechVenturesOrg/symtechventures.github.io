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
