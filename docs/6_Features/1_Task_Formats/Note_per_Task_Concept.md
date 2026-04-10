## The Note-Per-Task Approach

Individual Markdown notes replace centralized databases or proprietary formats. Each task file can be read, edited, and backed up with any text editor or automation tool.

### Task Structure

A task-note type of task is a standard Markdown file with YAML frontmatter:

```markdown
---
tags:
  - task
title: Review quarterly report
status: in-progress
priority: high
due: 2025-01-15
scheduled: 2025-01-14
contexts:
  - "@office"
projects:
  - "[[Q1 Planning]]"
---

## Notes

Key points to review:
- Revenue projections
- Budget allocations

## Meeting Notes

Discussion with finance team on 2025-01-10...
```

The frontmatter contains structured, queryable properties. The note body holds freeform content—research findings, meeting notes, checklists, or links to related documents.

### Obsidian Integration

Since tasks are proper notes, they work with Obsidian's core features:

- **Backlinks**: See which notes reference a task
- **Graph View**: Visualize task relationships and project connections
- **Tags**: Use Obsidian's tag system for additional categorization
- **Search**: Find tasks using Obsidian's search
- **Links**: Reference tasks from daily notes, meeting notes, or project documents

This approach creates many small files. You can configure the path to store this task-notes in your vault.
In practice, this lets this new approach fit into existing vault habits instead of replacing them. You keep using normal note workflows, and this feature adds structure, filtering, and commands on top.

## YAML Frontmatter

Task properties are stored in YAML frontmatter, a standard format with broad tool support.
Treat frontmatter as the machine-readable layer and the note body as the human-readable layer.

### Property Types

This plugin uses several property types:

| Type | Example | Description |
|------|---------|-------------|
| Text | `title: Buy groceries` | Single text value |
| List | `tags: [work, urgent]` | Multiple values |
| Date | `due: 2025-01-15` | ISO 8601 date format |
| DateTime | `scheduled: 2025-01-15T09:00` | Date with time |
| Link | `projects: ["[[Project A]]"]` | Obsidian wikilinks |
| Number | `timeEstimate: 60` | Numeric values (minutes) |

### Field Mapping

Property keys are configurable. If your vault uses `deadline` instead of `due`, you can configure these things in the plugin settings.

### Custom Fields

Add any frontmatter property to your tasks. User-defined fields work in filtering, sorting, and templates. You can add your custom properties inside the plugin's setting.