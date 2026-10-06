(function() {
  'use strict';

  var queryInput = document.getElementById('recipe-query');
  var categorySelect = document.getElementById('recipe-category');
  var cards = Array.prototype.slice.call(document.querySelectorAll('.recipe-directory-card'));
  var status = document.getElementById('recipe-results-status');
  var noResults = document.getElementById('recipe-no-results');

  if (!queryInput || !categorySelect || !cards.length || !status || !noResults) {
    return;
  }

  function normalize(value) {
    return value.toLowerCase().trim();
  }

  function updateResults() {
    var query = normalize(queryInput.value);
    var terms = query.split(/\s+/).filter(Boolean);
    var category = categorySelect.value;
    var visibleCount = 0;

    cards.forEach(function(card) {
      var searchableText = card.getAttribute('data-search') || '';
      var matchesQuery = terms.every(function(term) {
        return searchableText.indexOf(term) !== -1;
      });
      var matchesCategory = !category || card.getAttribute('data-category') === category;
      var isVisible = matchesQuery && matchesCategory;

      card.hidden = !isVisible;
      if (isVisible) {
        visibleCount++;
      }
    });

    status.textContent = visibleCount + (visibleCount === 1 ? ' recipe' : ' recipes') + ' shown';
    noResults.hidden = visibleCount !== 0;
  }

  queryInput.addEventListener('input', updateResults);
  categorySelect.addEventListener('change', updateResults);
  updateResults();
})();
