/* Keep the native mobile disclosure menu easy to dismiss by keyboard. */
document.querySelectorAll(".mobile-nav").forEach(function (menu) {
  var summary = menu.querySelector("summary");
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && menu.open) {
      menu.open = false;
      summary.focus();
    }
  });
});
