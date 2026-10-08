/* ManimCE tutorial — interactions: reading progress, scroll restore,
   home progress card, and the interactive inheritance graph. */
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

  /* ================= inheritance graph ================= */

  function loadViz() {
    return new Promise(function (resolve, reject) {
      if (window.Viz && window.Viz.instance) return resolve(window.Viz.instance());
      var base = document.querySelector('script[src$="custom.js"]');
      var src = base ? base.src.replace(/custom\.js$/, "vendor/viz.js") : "_static/vendor/viz.js";
      var s = document.createElement("script");
      s.src = src;
      s.onload = function () {
        window.Viz.instance().then(resolve, reject);
      };
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  function initInheritanceGraph(root) {
    var dataEl = root.querySelector("script.inheritance-data");
    var container = root.querySelector(".graph-container");
    var filterInput = root.querySelector(".graph-filter");
    if (!dataEl || !container) return;
    var allNodes;
    try {
      allNodes = JSON.parse(dataEl.textContent);
    } catch (e) {
      container.textContent = "继承关系图数据解析失败。";
      return;
    }
    var byName = new Map();
    allNodes.forEach(function (n) {
      byName.set(n.name, n);
    });
    var childrenOf = new Map();
    allNodes.forEach(function (n) {
      if (n.parent && byName.has(n.parent)) {
        if (!childrenOf.has(n.parent)) childrenOf.set(n.parent, []);
        childrenOf.get(n.parent).push(n);
      }
    });
    var roots = allNodes.filter(function (n) {
      return !n.parent || !byName.has(n.parent);
    });
    var hasChildren = function (name) {
      return (childrenOf.get(name) || []).length > 0;
    };

    var collapsed = new Set();
    var viz = null;
    var timer = null;

    function visibleSet() {
      var set = new Set();
      var queue = roots.map(function (r) {
        return r.name;
      });
      while (queue.length) {
        var name = queue.shift();
        if (set.has(name)) continue;
        set.add(name);
        if (collapsed.has(name)) continue;
        (childrenOf.get(name) || []).forEach(function (c) {
          queue.push(c.name);
        });
      }
      return set;
    }

    function displayName(name) {
      return name.length > 22 ? name.slice(0, 21) + "…" : name;
    }

    function buildDot(visible) {
      var q = (filterInput.value || "").trim().toLowerCase();
      var L = [
        "digraph G {",
        '  graph [rankdir=LR, bgcolor="transparent", nodesep="0.3", ranksep="0.6", splines=spline];',
        '  node  [shape=box, style="rounded,filled", fontname="Helvetica,sans-serif", fontsize=11, height=0.34, color="#8b93a1", fillcolor="#f2f4f7", fontcolor="#1f2733"];',
        '  edge  [color="#a6adba", arrowsize=0.6, penwidth=1.1];',
      ];
      visible.forEach(function (name) {
        var hit = !q || name.toLowerCase().indexOf(q) !== -1;
        var pen = hit ? "#5b64d6" : "#8b93a1";
        var fill = hit ? "#eef0fd" : "#f2f4f7";
        L.push(
          '  "' + name + '" [label="' + displayName(name) + '", color="' + pen + '", fillcolor="' + fill + '"];'
        );
      });
      allNodes.forEach(function (n) {
        if (!n.parent) return;
        if (!visible.has(n.name) || !visible.has(n.parent)) return;
        L.push('  "' + n.name + '" -> "' + n.parent + '";');
      });
      L.push("}");
      return L.join("\n");
    }

    function decorate(svg) {
      svg.classList.add("graphviz-svg");
      var q = (filterInput.value || "").trim().toLowerCase();
      Array.prototype.forEach.call(svg.querySelectorAll("g.node"), function (g) {
        var title = g.querySelector("title");
        var name = title ? title.textContent : "";
        if (!name) return;
        var node = byName.get(name);
        g.style.cursor = node && node.link ? "pointer" : "default";
        g.addEventListener("click", function (e) {
          e.stopPropagation();
          if (node && node.link) location.href = node.link;
          else if (hasChildren(name)) toggle(name);
        });
        var dimmed = q && name.toLowerCase().indexOf(q) === -1;
        if (dimmed) g.style.opacity = "0.25";
        if (!hasChildren(name)) return;
        var shape = g.querySelector(":scope > path");
        var bx = 0;
        var by = 0;
        if (shape) {
          var bb = shape.getBBox();
          bx = bb.x + bb.width;
          by = bb.y;
        }
        var NS = "http://www.w3.org/2000/svg";
        var badge = document.createElementNS(NS, "g");
        badge.setAttribute("class", "fold-badge");
        badge.style.cursor = "pointer";
        var c = document.createElementNS(NS, "circle");
        c.setAttribute("cx", String(bx));
        c.setAttribute("cy", String(by));
        c.setAttribute("r", "7");
        c.setAttribute("fill", "#5b64d6");
        c.setAttribute("stroke", "#ffffff");
        c.setAttribute("stroke-width", "1.5");
        var t = document.createElementNS(NS, "text");
        t.setAttribute("x", String(bx));
        t.setAttribute("y", String(by + 3.5));
        t.setAttribute("text-anchor", "middle");
        t.setAttribute("font-size", "10");
        t.setAttribute("font-weight", "700");
        t.setAttribute("fill", "#ffffff");
        t.setAttribute("pointer-events", "none");
        t.textContent = collapsed.has(name) ? "+" : "−";
        badge.appendChild(c);
        badge.appendChild(t);
        badge.addEventListener("click", function (e) {
          e.stopPropagation();
          toggle(name);
        });
        g.appendChild(badge);
      });
      Array.prototype.forEach.call(svg.querySelectorAll("g.edge"), function (e) {
        var t = e.querySelector("title");
        if (!t) return;
        var parts = t.textContent.split("->").map(function (s) {
          return s.trim();
        });
        if (q && (parts[0].toLowerCase().indexOf(q) === -1 || parts[1].toLowerCase().indexOf(q) === -1)) {
          e.style.opacity = "0.25";
        }
      });
    }

    function toggle(name) {
      if (collapsed.has(name)) collapsed.delete(name);
      else collapsed.add(name);
      scheduleRender();
    }

    function scheduleRender() {
      if (timer) clearTimeout(timer);
      timer = setTimeout(render, 60);
    }

    function render() {
      if (!viz) return;
      var svg = viz.renderSVGElement(buildDot(visibleSet()));
      container.replaceChildren(svg);
      decorate(svg);
    }

    loadViz().then(function (v) {
      viz = v;
      render();
    }).catch(function () {
      container.textContent = "继承关系图加载失败（viz.js 不可用）。";
    });

    filterInput.addEventListener("input", scheduleRender);
    root.querySelectorAll(".graph-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        collapsed = new Set();
        if (btn.getAttribute("data-act") === "collapse") {
          allNodes.forEach(function (n) {
            if (hasChildren(n.name)) collapsed.add(n.name);
          });
        }
        scheduleRender();
      });
    });
  }

  /* ================= boot ================= */

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  function boot() {
    initProgress();
    document.querySelectorAll(".inheritance-graph").forEach(initInheritanceGraph);
  }
})();
