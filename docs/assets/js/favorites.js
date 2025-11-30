/**
 * Favorites functionality for Home Automation Cookbook
 * Uses localStorage to store user's favorite recipes
 */
(function() {
  'use strict';

  var STORAGE_KEY = 'home-automation-favorites';

  /**
   * Get the current page path normalized for storage
   */
  function getCurrentPath() {
    var path = window.location.pathname;
    path = path.replace(/\/+$/, '');
    if (!path.endsWith('.html') && path !== '/' && path.length > 0) {
      path = path + '.html';
    }
    return path;
  }

  /**
   * Get all favorites from localStorage
   */
  function getFavorites() {
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      return stored ? JSON.parse(stored) : [];
    } catch (e) {
      console.warn('Could not read favorites from localStorage:', e.message);
      return [];
    }
  }

  /**
   * Save favorites to localStorage
   */
  function saveFavorites(favorites) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(favorites));
    } catch (e) {
      console.warn('Could not save favorites to localStorage:', e.message);
    }
  }

  /**
   * Check if a path is favorited
   */
  function isFavorited(path) {
    var favorites = getFavorites();
    return favorites.indexOf(path) !== -1;
  }

  /**
   * Toggle favorite status for a path
   */
  function toggleFavorite(path) {
    var favorites = getFavorites();
    var index = favorites.indexOf(path);
    
    if (index === -1) {
      favorites.push(path);
    } else {
      favorites.splice(index, 1);
    }
    
    saveFavorites(favorites);
    return index === -1;
  }

  /**
   * Normalize a URL path for comparison
   */
  function normalizePath(href) {
    if (!href) return '';
    href = href.replace(/\/+$/, '');
    if (!href.endsWith('.html') && href !== '/' && href.length > 0 && href.indexOf('.') === -1) {
      href = href + '.html';
    }
    return href;
  }

  /**
   * Initialize the favorite button on recipe pages
   */
  function initFavoriteButton() {
    var container = document.querySelector('.container');
    var h1 = container ? container.querySelector('h1') : null;
    
    var path = getCurrentPath();
    // Only add favorite button on automation detail pages (not index pages)
    if (path.indexOf('/automation/') === -1 || path.endsWith('index.html') || path === '/automation.html') {
      return;
    }
    
    if (!h1) return;

    var isFav = isFavorited(path);
    
    // Create wrapper div
    var wrapper = document.createElement('div');
    wrapper.className = 'title-with-favorite';
    
    // Create favorite button
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'favorite-btn' + (isFav ? ' is-favorited' : '');
    button.setAttribute('aria-label', isFav ? 'Remove from favorites' : 'Add to favorites');
    button.setAttribute('aria-pressed', isFav ? 'true' : 'false');
    
    // Create heart span
    var heart = document.createElement('span');
    heart.className = 'favorite-heart';
    heart.setAttribute('aria-hidden', 'true');
    button.appendChild(heart);
    
    // Handle click
    button.addEventListener('click', function() {
      var newStatus = toggleFavorite(path);
      button.className = 'favorite-btn' + (newStatus ? ' is-favorited' : '');
      button.setAttribute('aria-label', newStatus ? 'Remove from favorites' : 'Add to favorites');
      button.setAttribute('aria-pressed', newStatus ? 'true' : 'false');
      updateNavigationHearts();
    });
    
    // Insert wrapper before h1, move h1 into wrapper, add button
    h1.parentNode.insertBefore(wrapper, h1);
    wrapper.appendChild(h1);
    wrapper.appendChild(button);
  }

  /**
   * Update navigation menu to show hearts for favorited items
   */
  function updateNavigationHearts() {
    var favorites = getFavorites();
    var navLinks = document.querySelectorAll('.nav-menu a, .dropdown-menu a, .flyout-menu a');
    
    for (var i = 0; i < navLinks.length; i++) {
      var link = navLinks[i];
      var href = normalizePath(link.getAttribute('href'));
      
      if (favorites.indexOf(href) !== -1) {
        link.classList.add('is-favorited');
      } else {
        link.classList.remove('is-favorited');
      }
    }
  }

  /**
   * Initialize favorites functionality
   */
  function init() {
    initFavoriteButton();
    updateNavigationHearts();
  }

  // Run on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
