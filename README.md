# Dora Brkarić — website

Static portfolio built by GitHub Pages (Jekyll 3 via the `github-pages` gem). No theme, no JavaScript.

- **Deploy:** Settings → Pages → Deploy from a branch → `main`, `/ (root)`. Set `url` / `baseurl` in `_config.yml`; for a custom domain add a `CNAME` file.
- **Preview:** `bundle install && bundle exec jekyll serve`
- **Content:** works lists in `_data/works.yml`; project pages in `_works/<slug>.md` (link one from the list with `page: <slug>`); bio and facts in `about.md`; contact address is `contact_email` in `_config.yml`.
- **Photos:** put them in `assets/img/<slug>-<n>.jpg` and set `src: /assets/img/<slug>-<n>.jpg` on the image (or `portrait`) entry; the grey placeholder is replaced by the image with its caption below.

Text in `[square brackets]` is a placeholder waiting for real content.
