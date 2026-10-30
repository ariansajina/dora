# Dora Brkarić — website

The site lives at **https://&lt;github-username&gt;.github.io/dora/** and is published by GitHub Pages
from this repository. You edit it in **Pages CMS**, a free website where everything on the site is
a form: type, upload a photo, press **Save**, and about two minutes later the change is live.

- [Editing the site](#editing-the-site) — for Dora
- [Handing the site over](#handing-the-site-over) — one-time steps when the repository changes owner
- [How it’s built](#how-its-built) — technical notes

---

## Editing the site

### Opening the editor

1. Go to **https://app.pagescms.org** and click **Sign in with GitHub**. Use your GitHub account.
2. **The first time only**, Pages CMS asks for access to your repositories:
   click **Install the GitHub App**, choose **Only select repositories**, pick **dora**, and click
   **Install**. You’re taken back to Pages CMS.
3. Click **dora**. If it asks for a branch, pick **main**.

On the left you now see:

| Section | What it holds |
| --- | --- |
| **Works** | Your own works: one entry per work. Each one is a line in the works list *and* its own page. |
| **Performing & curating** | The two lists lower down on the works page: “performing” and “curating / teaching / other”. |
| **About** | Bio, portrait, facts, links (“elsewhere”) and the contact email. |
| **Media** | All photos on the site. |

### Saving and seeing your change

- Press **Save** at the top of the form. Nothing changes on the site until you save.
- About **2 minutes** later the site is updated. Reload the page in your browser to see it
  (if it still looks old, reload once more; browsers like to keep old copies).
- Every save is kept forever in the history (the **History** button in the editor shows the past versions),
  so nothing you do is final: an earlier version can always be brought back.

### Changing text on a work

**Works** → click the work → change any field → **Save**.

The fields, top to bottom:

| Field | Where it shows |
| --- | --- |
| **Title** | Works list and the big title on the work’s page. |
| **Pin to the top of the works list** | See [Pinning a work](#pinning-a-work). |
| **Year (works list)** | Left column of the works list. Write it any way you like: `2024`, `2018–20`, `2019–`. |
| **Sort year** | Not shown. Decides the order, see [The order of the works list](#the-order-of-the-works-list). |
| **What it is (works list)** | Small text on the right of the list, e.g. `experimental film · 5′`. |
| **Award (works list)** | Optional red line under that text. |
| **Title on the work page, line by line** | Optional. Breaks the big title over several lines (every line after the first is indented). Leave it empty and the title wraps by itself. |
| **Letter-spaced title** | Spreads the letters further apart. Use it for titles typed with spaces between letters, like `S T R I P T E A S E`. |
| **Details under the title** | The small lines next to the title: year and type, who made it, etc. **Add an item** for each line. |
| **Award (work page)** | Optional red line under the details. |
| **Photos** | See [Photos](#photos). |
| **Vimeo video number** | Optional. Shows the video on the page. For `https://vimeo.com/398974009` type `398974009`. |
| **Description** | The paragraph of text on the page. |
| **Credits** | Name + role for each person. |
| **Supported by** | Optional line under the credits. |
| **Shown** | Dates and places, newest first. Write the date as you want it shown: `13.03.2026`, `25.07.–21.08.2024`, `2021`. |
| **Links** | The links at the bottom of the page (an ↗ is added automatically). |
| **Link preview** | Optional. The picture people see when the page is shared in a chat or on social media. Without one, the general site picture is used. |

Anything in `[square brackets]` on the site is a placeholder waiting for real content: just type over it.

### Adding a new work

1. **Works** → **Add an entry**.
2. Fill in at least **Title**, **Year (works list)**, **Sort year** and **What it is**. Everything else
   can be added later.
3. The **file name** box is filled in from the title. It becomes the page’s web address
   (`…/dora/works/<file name>/`), so keep it short, lowercase, with dashes instead of spaces,
   e.g. `padian-rota`. It can only be chosen when the work is created.
4. **Save**. The work appears in the works list in the right place, and the “next” and “previous”
   links on the neighbouring work pages update by themselves.

### The order of the works list

The works list is ordered by **Sort year**, highest first (newest at the top), and the “next →” and
“← previous” links on each work page follow the same order. So to put a work in its place, give it
the right sort year; there’s nothing to drag.

- Usually the sort year is simply the year the work was made: `2024`.
- Two works from the same year? Add a decimal to the one that should come first:
  `2026.5` comes before `2026`. (`2021.5` before `2021`, and so on.)
- A work whose year you don’t know: give it a small number like `0.5` or `0`, or leave it empty
  to put it at the very bottom.

These are the sort years right now:

| Work | Sort year |
| --- | --- |
| S T R I P T E A S E (pinned) | 2023 |
| Pussy, it’s time for you to breathe, Pussy | 2026.5 |
| Padian Rota | 2026 |
| Meanwhile, in the Glossy Interface | 2024 |
| an_hum_an | 2021.5 |
| S A L T | 2021 |
| Striptease (film) | 2020.5 |
| Life is GREJP | 2019.5 |
| HOTDOG | 2019 |
| Which Football Team Won a Basketball Competition | 0.5 |
| Magician Stefano | 0 |

### Pinning a work

Turn on **Pin to the top of the works list** on a work and it moves above all the others, set apart
by a line (as S T R I P T E A S E is now). You can pin more than one: pinned works are ordered among
themselves by sort year. Turn it off to put the work back in its place in the list.

### Removing a work

**Works** → click the work → **Delete**. The list and the next/previous links close the gap by themselves.
(Its photos stay in **Media**; delete them there too if you don’t need them any more.)

### Photos

**Adding a photo to a work:** open the work → **Photos** → **Add an item** → click the photo box
and upload a file (or pick one already in Media). Then fill in:

- **What the photo shows**: a short description for people who can’t see it (blind visitors use
  screen readers), e.g. `Two performers tangled together on the floor in deep red light`.
- **Caption**: shown under the photo, e.g. `photo © Name Surname`.

Photos are shown one per row, alternating left and right, in the order of the list. Drag them to
reorder. Leave the photo box empty to show a grey placeholder with the caption in it.

**Size and format:**

- Upload the photo as it is, even straight from your phone. **Big photos are shrunk automatically**
  a minute after saving (to 1600 pixels on the long side, which is plenty for the site).
  Photos from a phone are also turned the right way up, and hidden camera data (including the
  GPS location of where the photo was taken) is removed.
- **JPG, PNG, WebP and HEIC** (the iPhone format) all work. Most browsers can’t show HEIC, so
  HEIC photos are **turned into JPG automatically** a minute after uploading, and the work is
  updated to use the JPG. Until then the editor may show an empty box instead of the photo
  (except in Safari); that’s fine.
  After uploading a HEIC photo, **reload the editor page about a minute after saving** before you
  change that work again, so it picks up the JPG. (If **Save** ever says the file has changed in the
  meantime, reload the page and make your change again.)
- Give the file a sensible name before uploading if you can, e.g. `padian-rota-3.jpg`.

**Replacing a photo:** open the photo box and pick or upload a different file.

### Performing & curating

**Performing & curating** has the two lists that sit below your works on the works page. These are
shown exactly in the order they have in the editor:

- **Add an item** adds a new entry **at the bottom**; drag it (by its handle) up to where it belongs,
  usually the top.
- Click an entry to open it. **Link** is the address the title links to. **Trailer link** (performing
  only) adds “trailer ↗”.

### About page

**About** has:

- **Bio**: plain text with a few simple marks:
  - Leave an **empty line** between paragraphs.
  - A link is written `[the text](the address)`, e.g. `[Zagrebački plesni ansambl](https://www.zagrebackiplesniansambl.hr/)`.
  - To link to one of your works, use `../works/` and its file name:
    `[S A L T](../works/salt/)`.
  - `{: .nobr}` right after a link keeps that link on one line (used for S T R I P T E A S E so its
    letters don’t break over two lines). Leave it where it is.
- **Portrait**: the photo and an optional caption.
- **Facts**: label + text, e.g. `born` / `Pula, 1996`. In the award fact, `<span class="nobr">…</span>`
  does the same job as `{: .nobr}`: keep it around a letter-spaced title.
- **Elsewhere (links)**: Instagram, Vimeo, etc. Add the `↗` to the link text yourself.
- **Contact email**.

### If something goes wrong

- **The change doesn’t show up after 5 minutes.** On GitHub, open the repository and click
  **Actions**. The top line is your last save:
  - a yellow dot means it’s still publishing: wait a minute;
  - a green tick means it’s published: reload the site once more;
  - a red cross means publishing failed. The site keeps showing the previous version, so nothing
    is broken for visitors. Click it, then **Re-run all jobs**. If it fails again, the last change is the
    likely cause: undo it (via **History**) or ask for help.
- **Something looks wrong on the site.** Undo the last change: open it in the editor, click
  **History**, and look at what changed. Or ask for help: send the link of the page and say what
  you changed.

---

## Handing the site over

One-time steps for moving the repository to Dora’s own GitHub account.

1. **Switch publishing to GitHub Actions** (if not done yet): repository **Settings → Pages →
   Build and deployment → Source: GitHub Actions**. The workflow in
   `.github/workflows/publish.yml` builds the site and shrinks photos; it only runs with this setting.
   Check that **Actions** shows a green run afterwards (start one with **Actions → Publish site →
   Run workflow** if needed).
2. **Dora creates a GitHub account** at https://github.com/signup (free). Her username becomes part
   of the address: `https://<username>.github.io/dora/`.
3. **Transfer the repository:** **Settings → General → Danger Zone → Transfer ownership**, enter her
   username. She gets an email and accepts the transfer.
4. **After the transfer:**
   - The old address (`https://ariansajina.github.io/dora/`) stops working; GitHub doesn’t
     redirect Pages sites. Links already shared will need the new address.
   - Nothing needs editing: the build takes the site address from wherever the repository lives.
     Check **Settings → Pages** still says *GitHub Actions*, then run **Actions → Publish site →
     Run workflow** once so the site is published under the new address.
   - Dora follows [Opening the editor](#opening-the-editor) to install Pages CMS on her account.
     (If you installed the Pages CMS app on your own account to try it out, remove it under
     GitHub **Settings → Applications → Installed GitHub Apps**.)

---

## How it’s built

Static portfolio built with Jekyll 3 (the `github-pages` gem). No theme, no JavaScript.

- **Publishing:** `.github/workflows/publish.yml` runs on every push to `main`: prepares photos in
  `assets/img` and commits the result back, then builds and deploys.
  `.github/scripts/prepare_photos.py` converts HEIC/HEIF to JPEG (deleting the original and rewriting
  references to it in content files; a name already taken gets `-heic`), shrinks the longer side to
  1600px, applies EXIF orientation, strips camera/GPS data and keeps the colour profile. It’s
  idempotent. The upload and the save that uses it arrive as separate commits, so references are
  resolved against what’s in the folder rather than during conversion.
  `url` and `baseurl` are taken from the Pages settings at build time, so `_config.yml` doesn’t need
  changing when the repository moves or gets a custom domain (for a custom domain, set it in
  Settings → Pages).
- **Preview:** `bundle install && bundle exec jekyll serve`
- **Content:**
  - Works: `_works/<name>.md`, one file per work, used for both the works list and the work page.
    `_includes/ordered-works.html` sets the order for both the list and the pager: `featured: true`
    first, then `sort_year` descending, empty last. (The field can’t be called `sort`: in Jekyll 3
    that name clashes with the built-in sort method and the build crashes.)
  - Performing and curating lists: `_data/works.yml`.
  - About: front matter and bio in `about.md`, markup in `_layouts/about.html`.
- **Editor:** `.pages.yml` configures Pages CMS. When Pages CMS saves, it rewrites the whole file
  from the form: comments are dropped and, inside lists, keys not in `.pages.yml` are lost. So
  **every field a template uses must be listed there** (`settings.content.merge` keeps unknown
  top-level keys such as `layout` and `permalink`). New works get `layout: work` from the defaults
  in `_config.yml`.
- **Sources:** where every fact comes from is in `SOURCES.md` (not published). Keep it up to date
  there rather than in YAML comments, which the editor would remove.
- **Link previews:** pages show `assets/img/share.jpg` when shared, unless a page sets its own
  `image: { path: /assets/img/<file>.jpg, alt: "…" }`.
