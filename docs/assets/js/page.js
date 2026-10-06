/**
 * Shared page helpers for Home Automation Cookbook.
 * Print CSS is injected only on beforeprint so media=print is not
 * downloaded on every visit (browsers still fetch media=print eagerly).
 */
(function () {
  'use strict';

  var node = document.querySelector('script[data-print]');
  var printHref = (node && node.getAttribute('data-print')) || '';
  if (!printHref) return;

  function addPrint() {
    if (document.head.querySelector('link[data-print-css]')) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = printHref;
    link.media = 'print';
    link.setAttribute('data-print-css', '');
    document.head.appendChild(link);
  }

  window.addEventListener('beforeprint', addPrint);
})();
