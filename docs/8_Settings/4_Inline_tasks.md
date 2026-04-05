---
parent: Plugin Settings
title: Inline Tasks
nav_order: 4
---

# Inline Tasks Settings

The Inline Tasks tab contains settings specific to how Task Board handles inline-style tasks (tasks embedded directly in markdown lines).

## Preview Section

This section shows a live preview of how your inline tasks will be rendered based on the settings you configure. As you change options below, the preview updates to show the format your tasks will appear in.

## Supported Plugin Formats

| Input Field | Options | Default |
|---|---|---|
| Dropdown | **Default** - Task Board native format<br>**Tasks Plugin** - Compatible with Tasks plugin format<br>**Dataview Plugin** - Compatible with Dataview plugin format<br>**Obsidian Native** - Uses Obsidian's native task format | Default |

Select which task metadata format you follow in your markdown files. Different plugins use different conventions for representing task properties like due dates and completion status.

### Format Examples

- **Default**: `- task title 📅 2024-01-01`
- **Tasks Plugin**: Uses specific emoji patterns compatible with the Tasks plugin
- **Dataview Plugin**: Uses Dataview-compatible metadata syntax
- **Obsidian Native**: Standard Obsidian checkbox format

Choose the format that matches your current task management setup. To see complete format specifications, see: [Metadata Formats](../6_Features/3_MetadataFormats.md)

## Default note for adding new tasks

## File for archived tasks

## Inherit frontmatter tags for inline-tasks