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
        var successful = document.execCommand('copy');
        if (successful) {
          resolve();
        } else {
          reject(new Error('Copy command failed'));
        }
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
    initArticleShareButtons();
  }

  // Run on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
