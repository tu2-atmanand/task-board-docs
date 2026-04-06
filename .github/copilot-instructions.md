# Copilot Instructions: Task Board Documentation

This is a Jekyll-based documentation site for the **Task Board** Obsidian plugin, built with the "just-the-docs" theme. These instructions help AI agents contribute consistently to this documentation project.

## Project Architecture

**Homepage**: `index.md` (root level, `layout: home`)  
**Documentation Structure**: Numbered directories and files in `/docs` for hierarchical organization
- `3_Installation.md` → Getting Started (Level 0)
- `5_How_To/` → Folder with `0_index.md` + numbered sub-docs
- `6_Features/` → Folder with `0_index.md` + numbered sub-docs (1_Task_Formats.md, 10_Filters_for_Scanning.md, etc.)

**Navigation**: Ordered by `nav_order` in frontmatter + file/folder numbering (e.g., `10_*` comes after `1_*` alphabetically but nav_order controls display order).

**Assets**: `/assets/images/` for all visual content (images referenced in docs)

## Critical Conventions

### Frontmatter Requirements
Every documentation file must include:
```yaml
---
title: Human Readable Title
nav_order: NUMBER
---
```

For nested documents (inside folders), add `parent`:
```yaml
---
parent: Parent Folder Name
title: Sub-Document Title
nav_order: NUMBER
---
```

**Homepage only** uses `layout: home` and `permalink: /`.

### File Naming & Organization
- **Numbered prefixes** for ordering: `1_`, `2_`, through `20_` (not `01_` or `001_`)
- **Index files**: Name as `0_index.md` for folder landing pages
- **Directories**: Also numbered (e.g., `5_How_To/`, `6_Features/`, `10_Advanced/`)
- Top-level docs and numbered folders both live in `/docs/`
- Alphabetical ordering only applies within folders (10 sorts after 1 alphabetically)

### Markdown Features (just-the-docs/kramdown)
- **Callouts**: `{: .note }` and `{: .warning }` on lines before blockquotes:
  ```markdown
  {: .warning }
  > This is important!
  ```
- **Labels/Badges**: `{: .d-inline-block }` + `{: .label .label-purple }` for version badges
- **Links**: Use relative paths (e.g., `../6_Features/1_Task_Formats.md`) without `.md` extension in links: `[Link Text](../folder/1_File)`
- **Images**: Reference from `/assets/images/`.

## Documentation Workflow

### Adding New Documentation
1. Determine parent section and nav_order (check existing docs in that section)
2. Create file with correct numbering: `docs/SECTION/NN_FileName.md`
3. Always include frontmatter with `parent` (section title) and `nav_order`
4. Use relative paths for cross-document links (remove `.md`: `../Other_Section/3_Page` not `../Other_Section/3_Page.md`)
5. Store images in `/assets/images/`, reference with: `/assets/ImageName.png`

### Content Patterns
- **Feature docs**: Include Overview, Why-it-matters, How-to-use, Best-practices, and "Learn more" links
- **Getting-Started**: Step-by-step guides with screenshots/GIFs (stored as `/assets/FileName.gif`)
- **How-To guides**: Concise action-oriented steps (see `5_How_To/1_HowToAddNewTask.md`)
- **Cross-references**: Link to related Features, How-To guides, and Components
- **Version badges**: Add above headings for newly released features: `v1.8.0 {: .label .label-purple }`

### Configuration
- Theme: just-the-docs 0.12.0 (see `Gemfile`)
- Build: Jekyll 4.4.1
- Logo: `/assets/images/DocsWebsiteLogo.png` (configured in `_config.yml`)
- Site title: "Task Board Documentation"

## Key Files & Examples

- [Homepage Example](index.md): Shows layout, video embedding, section linking
- [Getting Started](docs/4_Getting_Started.md): Demonstrates callouts, relative links, image references
- [Feature Index](docs/6_Features/0_index.md): Parent navigation, table of content style
- [Dependency Map](docs/6_Features/16_Dependency_Map.md): Feature doc with callouts, version badge, comprehensive explanation

## Build & Preview

```bash
bundle install          # Install dependencies
bundle exec jekyll serve # Preview locally at http://localhost:4000
```

## Quick Checklist When Adding/Editing Docs

- [ ] Frontmatter has `title`, `nav_order`, and `parent` (if nested)
- [ ] File name follows: `NN_FileName.md` (two-digit number prefix)
- [ ] Cross-links use relative paths without `.md` extension
- [ ] Images stored in `/assets/images/` with relative path references
- [ ] Callouts use correct syntax: `{: .note }` above blockquote
- [ ] Version badges added for new features: `v.X.X.X {: .label .label-purple }`
- [ ] Content is organized: Overview → Details → How-To → Resources

---

**Note**: This documentation powers https://tu2-atmanand.github.io/task-board-docs/ — keep it accurate and up-to-date for Task Board plugin users.
