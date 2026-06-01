---
name: update-publications
description: Automatically updates the publication list when new unsorted PDFs are added to the files/ folder. Use this skill to extract metadata from PDFs, research publication details online (CDA, IEEE Xplore, ACM DL), and generate the corresponding markdown entry in _publications/.
---

# Update Publications

This skill automates the process of adding new publications to the website. It handles metadata extraction from PDFs, online research for accurate details, and file organization.

## Workflow

When a new PDF is added to `files/` (or another folder) that does not follow the `YYYY_NNN.pdf` naming scheme:

### 1. Identify New Publications
- Scan the `files/` directory for PDFs that do not match the `YYYY_NNN.pdf` pattern.
- Identify the title and authors from the PDF using `pdftotext`.

### 2. Extract Abstract
- Use `pdftotext` to extract the text content of the PDF.
- Locate the "Abstract" section and extract its content.

### 3. Research Metadata
- **CDA Publications:** Search [https://www.cda.cit.tum.de/publications/](https://www.cda.cit.tum.de/publications/) for the paper title or authors to find official metadata (Venue, Year, etc.).
- **Conference Dates:** For conference papers, search the official conference website for the exact days the venue took place.
- **Journal Dates:** For journal papers, check **IEEE Xplore** or the **ACM Digital Library** for the exact publication date.

### 4. Determine Next ID
- Use the bundled `scripts/get_next_id.py` to find the next sequential ID for the publication year (e.g., `2025_012`).

### 5. Generate Markdown Entry
- Create a new file in `_publications/YYYY_NNN.md` with the following YAML frontmatter:
  ```yaml
  ---
  title: "Full Paper Title"
  collection: publications
  permalink: /publication/YYYY_NNN
  date: YYYY-MM-DD
  venue: 'Full Venue Name'
  paperurl: 'http://marcelwa.github.io/files/YYYY_NNN.pdf'
  ---
  ```
- Append the extracted abstract below the frontmatter.
- Add a download link at the end: `Download [here](http://marcelwa.github.io/files/YYYY_NNN.pdf)`

### 6. Rename and Move PDF
- Rename the original PDF to `files/YYYY_NNN.pdf`.

## Example Usage

**User:** "I just added `ICCAD_2023_paper.pdf` to the files folder. Please update the publication list."

**Agent:**
1. Uses `pdftotext` on `files/ICCAD_2023_paper.pdf`.
2. Extracts abstract.
3. Searches CDA website and ICCAD 2023 website for dates.
4. Runs `python3 update-publications/scripts/get_next_id.py 2023` -> returns `2023_009`.
5. Creates `_publications/2023_009.md`.
6. Renames `files/ICCAD_2023_paper.pdf` to `files/2023_009.pdf`.
