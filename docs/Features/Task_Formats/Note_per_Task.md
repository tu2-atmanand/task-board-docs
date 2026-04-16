---
parent: Task Formats
title: Note per Task
nav_order: 3
---

# Task Note

Also know as **note-per-task**. This is a new idea which got popularized through the TaskNotes plugin. Read this docs from TaskNotes plugin docs to learn more : [The Note-Per-Task Approach](https://tasknotes.dev/core-concepts/). Throughout this wiki, will refer this kind of task as "`task-note`".

Task Board also adheres to the same concepts and provides various features to manage your task-notes. Also refer the following wiki to learn more about the integration of Task Board with TaskNotes plugin : [TaskNotes plugin integration](/docs/Features/Plugin_Integrations/TaskNotes_Plugin_Integration.md).


## How does it work

Since a single note can be now imagined as a task. The simplest way to convert any note into a task is by using an tag identifier. You define this tag inside the ["Task note identifier tag" setting](/docs/Settings/Task_notes.md#task-note-identifier-tag).

Once you have configured the tag, through which you are instructing Task Board to consider the note as task. Now, as soon as you edit the note or if you scan your whole vault, all the notes with that specific tag will be rendered as [task item card](/docs/Components/Task_Item_Card.md) on the Task Board view.

Based on the frontmatter properties, the tasks will be placed in the respective columns, as per the [columns criteria](/docs/Features/Type_of_Columns/Overview.md). But for this to work, make sure you frontmatter property names are properly mapped inside the ["Frontmatter formatting" setting](/docs/Settings/Task_notes.md#frontmatter-formatting).

## Core concept

Individual Markdown notes replace centralized databases or proprietary formats. Each task file can be read, edited, and backed up with any text editor or automation tool.

### Task Structure Example

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

## Some heading

Some content related to the task. Perhaps task description.

- [ ] Sub task for this main task-note.
```

The frontmatter contains structured, queryable properties. The note body holds freeform content—research findings, meeting notes, checklists, or links to related documents.

## Obsidian Integration

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


<!-- ### Custom Fields

Add any frontmatter property to your tasks. User-defined fields work in filtering, sorting, and templates. You can add your custom properties inside the plugin's setting. -->

## Best practices
{: .d-inline-block }
Under Development
{: .label .label-purple }

Although Task Board provides most of the functionalities to have a proper integration with the TaskNotes plugin, the idea of Task Notes is slightly different in Task Board plugin...


Task Board plugin, do not recommend creating a task-note directly, unless its really required. In Task Board, you should move from an inline-task to a task-note.

The idea is... 
1. You create a simple inline-task first, to note down the idea which have came to your mind. 
2. This inline-task will appear under the backlog column inside the Kanban view of Task Board.
3. Now you will try to organize this task in other columns, which will automatically apply properties on to the inline-task.
4. The moment you feel, this task will going to grow into something called as a **work item**, this is when you will convert this simple inline-task into a task-note.

> You are also free to create a task-note directly inside Task Board using the various options we have in the following wiki : [Add a new task](/docs/How_To/Add_New_Task.md).

{: .note }
> This feature is under development. You can read more about this feature and track its development in the following GitHub ticket : [tu2-atmanand/task-board#33](https://github.com/tu2-atmanand/Task-Board/issues/33).
>
> BTW... This is the [vision of Task Board plugin](/docs/Vision/index.md).