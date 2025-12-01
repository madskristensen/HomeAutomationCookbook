/**
 * Share functionality for Home Automation Cookbook
 * Uses the Web Share API when available, falls back to copying URL to clipboard
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
   * Copy text to clipboard with fallback for older browsers
   */
  function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    
    // Fallback for older browsers
    var textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    return new Promise(function(resolve, reject) {
      try {
        document.execCommand('copy');
        resolve();
      } catch (err) {
        reject(err);
      } finally {
        textArea.remove();
      }
    });
  }

  /**
   * Show a brief tooltip/feedback message
   */
  function showFeedback(button, message) {
    var originalText = button.querySelector('.share-text');
    if (originalText) {
      var originalContent = originalText.textContent;
      originalText.textContent = message;
      setTimeout(function() {
        originalText.textContent = originalContent;
      }, 2000);
    }
  }

  /**
   * Handle share button click
   */
  function handleShareClick(event) {
    var button = event.currentTarget;
    var title = document.title;
    var url = window.location.href;
    
    // Try to get a description from the page
    var metaDescription = document.querySelector('meta[name="description"]');
    var text = metaDescription ? metaDescription.getAttribute('content') : '';

    if (isShareSupported()) {
      navigator.share({
        title: title,
        text: text,
        url: url
      }).catch(function(err) {
        // User cancelled or error occurred
        if (err.name !== 'AbortError') {
          // Fall back to copying URL
          copyToClipboard(url).then(function() {
            showFeedback(button, 'Link copied!');
          });
        }
      });
    } else {
      // Fall back to copying URL to clipboard
      copyToClipboard(url).then(function() {
        showFeedback(button, 'Link copied!');
      }).catch(function() {
        showFeedback(button, 'Copy failed');
      });
    }
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
    // Find all article share buttons and add click handlers
    var articleShareBtns = document.querySelectorAll('.article-share-btn');
    for (var i = 0; i < articleShareBtns.length; i++) {
      articleShareBtns[i].addEventListener('click', handleShareClick);
    }
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
