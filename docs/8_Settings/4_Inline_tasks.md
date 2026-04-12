---
parent: Plugin Settings
title: Inline Tasks
nav_order: 4
---

# Inline Tasks Tab

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

Choose the format that matches your current task management setup. To see complete format specifications, see: [Metadata Formats](/docs/6_Features/1_Task_Formats/2_Inline_Task.md#task-metadata)

## Default Note for Adding New Tasks

| Input Field | Default |
|---|---|
| File Picker text box | `Meta/Task_Board/New_Tasks.md` |

Specify the default markdown file where new inline-tasks created via the [task editor](/docs/6_Features/4_Task_Editor.md) will be saved.

{: .note }
> In few recent discussions, we have realized a problem with having a single note to save all your newly created tasks. Over time, this single file can become wildly massive in size and can be difficult to manage.
>
> To solve this issue, we have a better solution on roadmap : [tu2-atmanand/task-board#702](https://github.com/tu2-atmanand/Task-Board/issues/702).


## File for archived tasks

| Input Field | Default |
|---|---|
| File Picker text box | `Meta/Task_Board/New_Tasks.md` |

Specify the default markdown file where all your archived inline-tasks should be moved to.

Please refer the following wiki to learn more about this feature : [Archive tasks](/docs/6_Features/12_Archive_Tasks.md).


## Inherit frontmatter tags (read-only)

| Input Field | Default |
|---|---|
| Toggle | OFF |

This feature allows you to virtually inherit the tags from the frontmatter of the note and virtually apply them on the inline-tasks present within that note.

Read more about this feature and its benefits here : [Frontmatter tags inheritance](/docs/6_Features/19_Frontmatter_Tags_Inheritance.md).

## Hide specific properties in inline-tasks

| Input Field | Default |
|---|---|
| Multiple Toggle | ALL OFF |

Under this setting you will see a list of task properties and how they look inside your Obsidian's Live editor mode or in reading mode.

This setting helps you to hide specific properties inside both this modes, so that you can get a nice and clean look of your notes and the inline-tasks within them.

For task-note, its easy to hide its properties by simply minimizing the frontmatter section, or hide it completely via the Obsidian's settings. But for inline-tasks, with multiple properties, the content might look bloated. And this setting help you in exactly solving this issue.