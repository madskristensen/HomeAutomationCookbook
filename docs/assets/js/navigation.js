/**
 * Navigation flyout positioning
 * Prevents flyout menus from extending beyond viewport on smaller screens
 */

document.addEventListener('DOMContentLoaded', function() {
  const flyoutItems = document.querySelectorAll('.dropdown-item.has-flyout');
  
  function positionFlyout(item) {
    const flyout = item.querySelector('.flyout-menu');
    if (!flyout) return;
    
    // Remove existing class
    flyout.classList.remove('flyout-left');
    
    // Get parent dropdown item position
    const itemRect = item.getBoundingClientRect();
    const viewportWidth = window.innerWidth;
    
    // Calculate expected flyout width (min-width from CSS is 240px)
    const flyoutWidth = 240;
    
    // Check if flyout would overflow viewport when opened to the right
    // itemRect.right is where flyout would start, add flyout width + buffer
    if (itemRect.right + flyoutWidth + 20 > viewportWidth) {
      flyout.classList.add('flyout-left');
    }
  }
  
  // Position flyout on hover
  flyoutItems.forEach(item => {
    item.addEventListener('mouseenter', function() {
      positionFlyout(this);
    });
    
    // Also handle focus for keyboard navigation
    item.addEventListener('focusin', function() {
      positionFlyout(this);
    });
  });
  
  // Reposition on window resize (debounced)
  let resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      flyoutItems.forEach(item => {
        if (item.matches(':hover') || item.querySelector(':focus')) {
          positionFlyout(item);
        }
      });
    }, 250);
  });
});
