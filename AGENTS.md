# Agent Notes: marcelwa.github.io

This is Marcel Walter's personal academic website (Jekyll, GitHub Pages,
academicpages-derived theme).

## CV and publication list (LaTeX)

`cv-source/` holds the LaTeX sources for Marcel's CV, cover letter, and
publications list (Awesome-CV template, XeLaTeX + Roboto fonts under
`cv-source/fonts/`). It was moved here from the `ptp` repo so the PDF CV and
publication list live alongside the canonical record of the same content
(this website), instead of a separate, harder-to-keep-in-sync repo.

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
* The `ptp` repo (Marcel's private application-materials vault) keeps a
  symlink at `CV -> ../marcelwa.github.io/cv-source` so existing workflows
  there (`cd CV && latexmk ...`) keep working unchanged. **Edit the files
  here** (or through that symlink — same underlying files); there is only
  one copy.

## Keeping the PDF CV and the web CV in sync

`_pages/cv.md` (the human-readable `/cv/` page) and `cv-source/cv.tex` +
its `cv-source/cv/*.tex` sections describe the same career facts in two
different formats. They are edited independently and can drift. When
updating one, check whether the other needs the same update — e.g. a new
job, award, or publication should normally go in both. `_publications/`
(one Markdown file per paper) should stay in sync with
`cv-source/bibliography.bib` the same way: a paper added to one should
generally be added to the other too.

## Instructions for future agents

1. Treat this website as the up-to-date, authoritative record of Marcel's
   CV content; when the LaTeX CV and this site disagree, ask which is
   correct rather than assuming either is right.
2. Never let `cv-source/` leak into the published site. If you touch
   `_config.yml`'s `exclude:` list, keep `cv-source` in it.
3. Don't commit LaTeX build junk — check `.gitignore` covers new artifact
   types if you introduce a new build tool.
