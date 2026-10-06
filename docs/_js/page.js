/**
 * Shared page helpers for Home Automation Cookbook.
 * Print CSS is injected only on beforeprint so media=print is not
 * downloaded on every visit (browsers still fetch media=print eagerly).
 * The service worker registers on window load.
 */
(function () {
  'use strict';

  var node = document.querySelector('script[data-print]');
  var printHref = (node && node.getAttribute('data-print')) || '';

  function addPrint() {
    if (!printHref) return;
    if (document.head.querySelector('link[data-print-css]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = printHref;
    link.media = 'print';
    link.setAttribute('data-print-css', '');
    document.head.appendChild(link);
  }

  function registerServiceWorker() {
    if (!('serviceWorker' in navigator)) return;
    var swNode = document.querySelector('script[data-sw]');
    var url = (swNode && swNode.getAttribute('data-sw')) || '/sw.js';
    navigator.serviceWorker.register(url, { scope: '/', updateViaCache: 'none' }).catch(function () {});
  }

  window.addEventListener('beforeprint', addPrint);
  window.addEventListener('load', registerServiceWorker);
})();
