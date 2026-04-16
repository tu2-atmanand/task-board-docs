---
parent: Plugin Settings
title: Task Notes
nav_order: 5
---

# Task Notes Tab

The Task Notes tab contains settings specific to how Task Board handles [task-note](/docs/Features/Task_Formats/Note_per_Task.md) style tasks.


## Task note identifier tag

| Input Field | Default |
|---|---|
| Text (Tags suggestions) | `tasknote` |

In this setting you configure the identifier tag which helps Task Board to identify which of your notes you want to consider as a task-note.

## Folder for new task-notes

| Input Field | Default |
|---|---|
| Text (File suggestions) | `Meta/Task_Board/Task_Notes` |

In this setting you set the default folder location where all your newly created task-notes should be stored when you created them through the [task editor](/docs/Features/Task_Editor.md).

## Folder for archived task-notes

| Input Field | Default |
|---|---|
| Text (File suggestions) | `Meta/Task_Board/Archived_Task_Notes` |

In this setting you define the folder location where your task-note should automatically be moved, when you mark the task-note as archived.

## Frontmatter formatting

Under this setting section, you will see a list of items which are basically the [default task properties](/docs/Features/Task_Properties.md) supported in Task Board.

In this setting you are mapping the name of the frontmatter key to the task property. When your task-notes will be scanned, these frontmatter keys will be used to parse the values for the respective task property. Ensure that, the value you are providing for the respective frontmatter key are in the expected format, for example, of date related properties, the value in the frontmatter should be a valid date format.