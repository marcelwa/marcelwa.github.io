# Agent Notes: marcelwa.github.io

This is Marcel Walter's personal academic website: a Jekyll site (GitHub
Pages, `academicpages`/`minimal-mistakes`-derived theme) at
https://marcelwa.github.io.

## Site structure

- `_pages/` — the static pages: `about.md` (home page, `/`), `cv.md`
  (`/cv/`), `publications.md` (`/publications/`), `teaching.html`
  (`/teaching/`), `talks.html` (`/talks/`), `portfolio.html`, plus archive
  and utility pages (`sitemap.md`, `404.md`, `terms.md`, etc.).
- `_publications/`, `_talks/`, `_teaching/` — Jekyll collections, one
  Markdown file per item (publication, invited talk, or teaching role).
  `publications.md`, `talks.html`, `teaching.html`, and `cv.md` all render
  from these collections via a Liquid for-loop over the collection
  (reversed, i.e. newest first), so **adding an item to a collection
  updates every page that lists it** — no need to hand-edit those pages
  separately.
- `_data/` — YAML data (`authors.yml`, `navigation.yml`, `ui-text.yml`) and
  Staticman comment storage.
- `files/` — hosted PDFs (papers, award certificates) linked from
  `_publications/*.md` and `_pages/cv.md`.
- `assets/`, `_sass/`, `_layouts/`, `_includes/` — theme internals; rarely
  need editing for content changes.
- `talkmap.py` / `talkmap.ipynb` / `talkmap/` — generates the optional talk
  map (disabled by default via `talkmap_link: false` in `_config.yml`).
- `_config.yml` — site settings, including Jekyll's `exclude:` list
  (controls what's copied into the built `_site/`, i.e. what actually goes
  live — distinct from `.gitignore`, which only controls what git tracks).

## CV and publication list (LaTeX)

`cv-source/` holds the LaTeX sources for Marcel's CV, cover letter, and
publications list (Awesome-CV template, XeLaTeX + Roboto fonts under
`cv-source/fonts/`).

Key points:

* **`cv-source/` is excluded from the built Jekyll site** (`_config.yml`'s
  `exclude:` list). The PDF CV must never appear on the live website — it
  is kept here purely for safe-keeping and so both the PDF and the web CV
  (`_pages/cv.md`) can be updated together and stay consistent.
* Only `.tex`/`.cls`/`.bib` sources and the final compiled PDFs
  (`cv.pdf`, `coverletter.pdf`, `publications_list.pdf`) are tracked by git.
  LaTeX build artifacts (`.aux`, `.log`, `.bbl`, `.bcf`, `.blg`,
  `.fdb_latexmk`, `.fls`, `.out`, `.run.xml`, `.synctex.gz`, `.xdv`) are
  gitignored — see `.gitignore`.
* Build with `latexmk -xelatex cv.tex` (or `coverletter.tex` /
  `publications_list.tex`) from inside `cv-source/`. Requires XeLaTeX,
  latexmk, and biber.

## Keeping the PDF CV and the web CV in sync

`_pages/cv.md` and `cv-source/cv.tex` + its `cv-source/cv/*.tex` sections
describe the same career facts in two different formats. They are edited
independently and can drift. When updating one, check whether the other
needs the same update — e.g. a new job, award, repository, or research
interest should normally go in both. `_publications/` should stay in sync
with `cv-source/bibliography.bib` the same way: a paper added to one
should generally be added to the other too (title, venue, and — for
`_publications/` — an abstract and a hosted PDF under `files/`).

## Instructions for future agents

1. Treat this website as the up-to-date, authoritative record of Marcel's
   CV content; when the LaTeX CV and this site disagree, ask which is
   correct rather than assuming either is right.
2. Never let `cv-source/` leak into the published site. If you touch
   `_config.yml`'s `exclude:` list, keep `cv-source` in it.
3. Don't commit LaTeX build junk — check `.gitignore` covers new artifact
   types if you introduce a new build tool.
4. When adding a publication, add it to *both* `_publications/` (with a
   hosted PDF in `files/`) and `cv-source/bibliography.bib`, so the web
   list and the PDF publication list stay in sync.
