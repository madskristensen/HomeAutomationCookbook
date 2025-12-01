/**
 * Share functionality for Home Automation Cookbook
 * Uses the Web Share API to enable native sharing on supported devices
 */
(function() {
  'use strict';

  /**
   * Check if the Web Share API is supported
   */
  function isShareSupported() {
    return navigator.share !== undefined;
  }

  /**
   * Handle share button click
   */
  function handleShareClick() {
    var title = document.title;
    var url = window.location.href;
    
    // Try to get a description from the page
    var metaDescription = document.querySelector('meta[name="description"]');
    var text = metaDescription ? metaDescription.getAttribute('content') : '';

    navigator.share({
      title: title,
      text: text,
      url: url
    }).catch(function(err) {
      // User cancelled or error occurred - silently ignore
      if (err.name !== 'AbortError') {
        console.warn('Share failed:', err.message);
      }
    });
  }

  /**
   * Move article meta section to after the title wrapper or h1
   */
  function moveArticleMetaAfterH1() {
    var articleMeta = document.querySelector('.article-meta');
    if (!articleMeta) return;

    var mainContent = document.querySelector('.main-content');
    if (!mainContent) return;

    // First, check if there's a title-with-favorite wrapper (created by favorites.js)
    var titleWrapper = mainContent.querySelector('.title-with-favorite');
    if (titleWrapper) {
      // Move article meta after the entire title wrapper
      titleWrapper.parentNode.insertBefore(articleMeta, titleWrapper.nextSibling);
      return;
    }

    // Fallback: move after h1 if no title wrapper exists
    var h1 = mainContent.querySelector('h1');
    if (h1) {
      h1.parentNode.insertBefore(articleMeta, h1.nextSibling);
    }
  }

  /**
   * Initialize share buttons in the article meta section
   */
  function initArticleShareButtons() {
    if (!isShareSupported()) {
      return;
    }

    // Find all article share buttons and enable them
    var articleShareBtns = document.querySelectorAll('.article-share-btn');
    articleShareBtns.forEach(function(btn) {
      btn.style.display = 'inline-flex';
      btn.addEventListener('click', handleShareClick);
    });
  }

  /**
   * Initialize share functionality
   */
  function init() {
    // Use a small delay to ensure favorites.js has run first
    setTimeout(function() {
      moveArticleMetaAfterH1();
      initArticleShareButtons();
    }, 0);
  }

  // Run on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
