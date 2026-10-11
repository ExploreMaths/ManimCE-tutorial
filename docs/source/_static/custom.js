/* ManimCE tutorial — interactions: reading progress, scroll restore,
   and the home progress card. */
(function () {
  "use strict";

  /* ================= reading progress (localStorage) ================= */

  var PROGRESS_KEY = "mce-progress";
  var SCROLL_KEY = "mce-scroll";
  var RESTORED_PREFIX = "mce-restored";

  function readJson(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) {
      return fallback;
    }
  }

  function visitedMap() {
    return readJson(PROGRESS_KEY, {});
  }

  function markVisited(path) {
    var map = visitedMap();
    map[path] = Date.now();
    try {
      localStorage.setItem(PROGRESS_KEY, JSON.stringify(map));
    } catch (e) {}
  }

  function saveScroll(path, y) {
    var map = readJson(SCROLL_KEY, {});
    map[path] = Math.round(y);
    try {
      localStorage.setItem(SCROLL_KEY, JSON.stringify(map));
    } catch (e) {}
  }

  function takeScrollRestore(path) {
    var flag = RESTORED_PREFIX + ":" + path;
    if (sessionStorage.getItem(flag)) return null;
    var y = readJson(SCROLL_KEY, {})[path];
    if (typeof y !== "number") return null;
    sessionStorage.setItem(flag, "1");
    return y;
  }

  function resetAll() {
    localStorage.removeItem(PROGRESS_KEY);
    localStorage.removeItem(SCROLL_KEY);
    for (var i = sessionStorage.length - 1; i >= 0; i--) {
      var key = sessionStorage.key(i);
      if (key && key.indexOf(RESTORED_PREFIX) === 0) sessionStorage.removeItem(key);
    }
  }

  /* ================= toast / restore bar ================= */

  var toastEl = null;

  function dismissToast() {
    if (toastEl) {
      toastEl.remove();
      toastEl = null;
    }
  }

  function showRestoreToast(onRestart) {
    dismissToast();
    toastEl = document.createElement("div");
    toastEl.className = "mce-restore-toast";
    toastEl.setAttribute("role", "status");
    var msg = document.createElement("span");
    msg.textContent = "已恢复到上次阅读处";
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "mce-toast-btn";
    btn.textContent = "从头开始";
    btn.addEventListener("click", function () {
      resetAll();
      dismissToast();
      window.scrollTo({ top: 0, behavior: "instant" in window ? "instant" : "auto" });
      if (onRestart) onRestart();
    });
    toastEl.appendChild(msg);
    toastEl.appendChild(btn);
    document.body.appendChild(toastEl);
  }

  /* ================= chapter pages ================= */

  function initProgress() {
    var path = location.pathname;
    var onChapter = /\/chapters\//.test(path);

    if (onChapter) {
      markVisited(path);
      var t = null;
      window.addEventListener(
        "scroll",
        function () {
          if (t) clearTimeout(t);
          t = setTimeout(function () {
            saveScroll(path, window.scrollY);
          }, 300);
        },
        { passive: true }
      );
      var y = takeScrollRestore(path);
      if (y && y > 240) {
        window.scrollTo(0, y);
        showRestoreToast(function () {
          /* progress badges elsewhere on the page, if any */
          location.reload();
        });
      }
    }

    var home = document.getElementById("home-progress");
    if (home) initHomeProgress(home);
  }

  /* ================= home progress card ================= */

  function initHomeProgress(el) {
    var total = parseInt(el.getAttribute("data-total"), 10) || 0;
    var visited = Object.keys(visitedMap()).length;
    var pct = total > 0 ? Math.min(100, Math.round((visited / total) * 100)) : 0;

    var bar = document.createElement("div");
    bar.className = "mce-progress-card";
    var label = document.createElement("div");
    label.className = "mce-progress-label";
    label.textContent = "学习进度：" + visited + " / " + total + " 节（" + pct + "%）";
    var track = document.createElement("div");
    track.className = "mce-progress-track";
    var fill = document.createElement("div");
    fill.className = "mce-progress-fill";
    fill.style.width = pct + "%";
    track.appendChild(fill);
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "mce-toast-btn";
    btn.textContent = "重置进度";
    btn.addEventListener("click", function () {
      resetAll();
      initHomeProgress(el);
    });
    bar.appendChild(label);
    bar.appendChild(track);
    bar.appendChild(btn);
    el.replaceChildren(bar);
  }

  /* ================= boot ================= */

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  function boot() {
    initProgress();
  }
})();
