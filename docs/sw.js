---
permalink: /sw.js
sitemap: false
---
{%- comment -%}
  The page cache name is a hash of the precached shell files, so a content
  commit that does not change those files keeps the same worker. The image
  cache name stays put across deploys. No push notifications.
{%- endcomment -%}
/* Home Automation Cookbook. Pages and images are cached apart. No push. */
var VERSION = {{ site.data.shell.version | jsonify }};
var PAGES = "hac-pages-" + VERSION;
var IMAGES = "hac-images";
var IMAGE_CAP = 60;
var PAGE_CAP = 80;
var NAV_TIMEOUT = 3000;
var imageWrite = Promise.resolve();

function enqueueImageWrite(task) {
  var run = imageWrite.then(task, task);
  imageWrite = run.then(function () {}, function () {});
  return run;
}

var SHELL_PAGES = [
  {%- for path in site.data.shell.pages -%}
  "{{ path | relative_url }}",
  {%- endfor -%}
];

var SHELL_IMAGES = [
  {%- for path in site.data.shell.images -%}
  "{{ path | relative_url }}",
  {%- endfor -%}
];

self.addEventListener("install", function (event) {
  event.waitUntil(
    Promise.all([
      caches.open(PAGES).then(function (cache) {
        return precache(cache, SHELL_PAGES);
      }),
      caches.open(IMAGES).then(function (cache) {
        return precache(cache, SHELL_IMAGES);
      })
    ]).then(function () {
      return self.skipWaiting();
    })
  );
});

self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (key) {
        if (key === PAGES || key === IMAGES) return Promise.resolve();
        return caches.delete(key);
      }));
    }).then(function () {
      if (!self.registration.navigationPreload) return;
      return self.registration.navigationPreload.enable().catch(function () {});
    }).then(function () {
      return self.clients.claim();
    })
  );
});

function precache(cache, urls) {
  return Promise.all(urls.map(function (url) {
    return fetch(new Request(url, { cache: "reload" })).then(function (response) {
      if (!response || !response.ok) throw new Error("precache " + url);
      return putStamped(cache, url, response);
    });
  }));
}

function isHtml(request) {
  if (request.mode === "navigate") return true;
  var accept = request.headers.get("accept") || "";
  return accept.indexOf("text/html") !== -1;
}

function isImage(request, url) {
  if (request.destination === "image") return true;
  return /\.(?:avif|webp|png|jpe?g|gif|svg|ico)$/i.test(url.pathname);
}

function cacheKey(request) {
  return typeof request === "string" ? request : request.url;
}

function putStamped(cache, request, response) {
  if (!response || !response.ok || response.type !== "basic") return Promise.resolve();
  var headers = new Headers(response.headers);
  headers.set("X-Cached-At", new Date().toISOString());
  var stamped = new Response(response.clone().body, {
    status: response.status,
    statusText: response.statusText,
    headers: headers
  });
  // Navigation requests cannot be cache keys. Store the URL instead.
  return cache.put(cacheKey(request), stamped).catch(function () {});
}

function byCachedAt(entries) {
  entries.sort(function (a, b) {
    if (a.at < b.at) return -1;
    if (a.at > b.at) return 1;
    return 0;
  });
  return entries;
}

function stampedEntries(cache, requests) {
  return Promise.all(requests.map(function (request) {
    return cache.match(request).then(function (response) {
      var at = response && response.headers.get("X-Cached-At") || "";
      return { request: request, at: at };
    });
  }));
}

function trimTo(cache, requests, cap) {
  if (requests.length <= cap) return Promise.resolve();
  return stampedEntries(cache, requests).then(function (entries) {
    var extra = entries.length - cap;
    return Promise.all(byCachedAt(entries).slice(0, extra).map(function (entry) {
      return cache.delete(entry.request);
    }));
  });
}

function trimImages(cache) {
  return cache.keys().then(function (requests) {
    return trimTo(cache, requests, IMAGE_CAP);
  });
}

function shellUrl(path) {
  return new URL(path, self.location.origin).href;
}

function trimPages(cache) {
  var shell = {};
  SHELL_PAGES.forEach(function (path) {
    shell[shellUrl(path)] = true;
  });
  return cache.keys().then(function (requests) {
    var extras = requests.filter(function (request) {
      return !shell[request.url];
    });
    return trimTo(cache, extras, PAGE_CAP);
  });
}

function offlineDocument() {
  var html = "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">" +
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">" +
    "<meta name=\"theme-color\" content=\"#2c3e50\">" +
    "<title>Offline. Home Automation Cookbook</title></head>" +
    "<body style=\"margin:0;background:#fff;color:#1a1a1a;font-family:system-ui,-apple-system,Segoe UI,sans-serif\">" +
    "<main style=\"max-width:36rem;margin:0 auto;padding:2.2rem 1rem\">" +
    "<h1 style=\"font-size:1.4rem;margin:0 0 0.75rem\">You are offline</h1>" +
    "<p style=\"line-height:1.5;margin:0 0 1rem\">This page is not in the local cache yet. Reconnect and try again.</p>" +
    "<p style=\"margin:0\"><a href=\"/\" style=\"color:#2c3e50\">Go to Home Automation Cookbook</a></p>" +
    "</main></body></html>";
  return new Response(html, {
    status: 200,
    headers: { "Content-Type": "text/html; charset=utf-8" }
  });
}

function networkFromEvent(event, request) {
  var preload = event.preloadResponse || Promise.resolve();
  var preloadedOrFetch = Promise.resolve(preload).then(function (preloaded) {
    if (preloaded) return preloaded;
    return fetch(request);
  }, function () {
    return fetch(request);
  });
  if (typeof navigator !== "undefined" && navigator.onLine === false) {
    preloadedOrFetch.catch(function () {});
    return Promise.reject(new Error("offline"));
  }
  return preloadedOrFetch;
}

function withTimeout(promise, ms) {
  return new Promise(function (resolve, reject) {
    var done = false;
    var timer = setTimeout(function () {
      if (done) return;
      done = true;
      resolve(null);
    }, ms);
    promise.then(function (value) {
      if (done) return;
      done = true;
      clearTimeout(timer);
      resolve(value);
    }, function (err) {
      if (done) return;
      done = true;
      clearTimeout(timer);
      reject(err);
    });
  });
}

function serveCachedPage(request, network) {
  return caches.open(PAGES).then(function (cache) {
    return cache.match(cacheKey(request)).then(function (cached) {
      if (cached) return cached;
      return network.then(function (response) {
        return response || offlineDocument();
      }).catch(function () {
        return offlineDocument();
      });
    });
  });
}

function networkFirstNavigation(event, request) {
  var network = networkFromEvent(event, request);
  var caching = network.then(function (response) {
    if (!response || !response.ok || response.type !== "basic") return;
    var copy = response.clone();
    return caches.open(PAGES).then(function (cache) {
      return putStamped(cache, request, copy).then(function () {
        return trimPages(cache);
      });
    });
  }).catch(function () {});
  event.waitUntil(caching);
  return withTimeout(network, NAV_TIMEOUT).then(function (response) {
    if (response) return response;
    return serveCachedPage(request, network);
  }).catch(function () {
    return serveCachedPage(request, network);
  });
}

function staleWhileRevalidate(event, request, cacheName) {
  return caches.open(cacheName).then(function (cache) {
    return cache.match(cacheKey(request)).then(function (cached) {
      var refreshed = fetch(request).then(function (response) {
        var store = function () {
          return putStamped(cache, request, response).then(function () {
            if (cacheName === IMAGES) return trimImages(cache);
            if (cacheName === PAGES) return trimPages(cache);
          });
        };
        var stored = cacheName === IMAGES ? enqueueImageWrite(store) : store();
        return stored.then(function () {
          return response;
        });
      }).catch(function () {
        return cached;
      });
      if (cached) {
        event.waitUntil(refreshed.catch(function () {}));
        return cached;
      }
      return refreshed.then(function (response) {
        return response || new Response("", { status: 504, statusText: "Offline" });
      });
    });
  });
}

self.addEventListener("fetch", function (event) {
  var request = event.request;
  if (request.method !== "GET") return;
  if (request.headers.get("range")) return;

  var url;
  try {
    url = new URL(request.url);
  } catch (err) {
    return;
  }
  if (url.origin !== self.location.origin) return;
  if (url.pathname === "/sw.js") return;

  if (isHtml(request)) {
    event.respondWith(networkFirstNavigation(event, request));
    return;
  }
  var cacheName = isImage(request, url) ? IMAGES : PAGES;
  event.respondWith(staleWhileRevalidate(event, request, cacheName));
});
