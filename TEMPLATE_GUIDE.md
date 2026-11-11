
## SEO checks

Every `<img>` needs a non-empty alt. Page titles, with the site name, must be 70 characters or less. The build runs `script/check-seo.py` and fails if either rule breaks.

## last_modified_at

When you change the body, product list, or FAQs of a page that has `last_modified_at`, update that field to the date of the change. A pull request check runs `script/check-lastmod.py` and fails if the field is left unchanged. Title and description-only edits do not need a bump. To skip the check on a frontmatter or template sweep, add the `skip-lastmod-check` label or a `Skip-Lastmod-Check: true` commit trailer.

