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
   * Create and insert the share button
   */
  function createShareButton() {
    // Only create button if Web Share API is supported
    if (!isShareSupported()) {
      return;
    }

    // Create the share button
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'share-btn';
    button.setAttribute('aria-label', 'Share this page');
    button.setAttribute('title', 'Share this page');

    // Create share icon (standard share icon - box with arrow pointing up)
    var icon = document.createElement('span');
    icon.className = 'share-icon';
    icon.setAttribute('aria-hidden', 'true');
    icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/></svg>';
    button.appendChild(icon);

    // Handle click
    button.addEventListener('click', function() {
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
    });

    // Insert the button in the navigation, before the nav menu
    var navContainer = document.querySelector('.nav-container');
    if (navContainer) {
      var navMenu = navContainer.querySelector('.nav-menu');
      if (navMenu) {
        navContainer.insertBefore(button, navMenu);
      } else {
        // Fallback: insert after site title
        var siteTitle = navContainer.querySelector('.site-title');
        if (siteTitle && siteTitle.nextElementSibling) {
          navContainer.insertBefore(button, siteTitle.nextElementSibling);
        } else {
          navContainer.appendChild(button);
        }
      }
    }
  }

  /**
   * Initialize share functionality
   */
  function init() {
    createShareButton();
  }

  // Run on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
