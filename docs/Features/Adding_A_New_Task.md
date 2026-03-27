---
parent: Features
title: Adding a new Task
nav_order: 1
---

# Adding a New Task

There are a couple ways to add tasks to a board:
- Manually typing it within a markdown file: [Adding new task from file](../How_To/HowToAddNewTask.md#from-file)
- Via **Task Board**'s **Add Task Window** (accessed via the button on the top right of the board itself or via Obsidian's Command Palette `Default: CTRL+P`)

{: .note }
> Please note that before running the command, place your cursor in the editor where you want to add the task. For running the command its important that you are focusing inside an active editor.

## Add Task Window

This window gives the user the ability to add new tasks to a file or files in various ways as well as assists with managing properties/[metadata](../Components/MetadataFormats.md) for tasks in a way that is compatible with your other plugins, as well as how you have it configured in the plugin's global settings. The window also provides a live preview as you type.

### Ways to Add a Task

1. **Add to Current File**: The plugin provides a command to add new task to the currently opened markdown file.
2. **Add to Pre-defined File**: Add tasks to a default note you've specified in settings, from anywhere in Obsidian.
3. **Add to Any File**: Use the file suggester in the modal to choose any file in your vault to add the task to.
4. **QuickAdd Integration**: Select from different QuickAdd choices to add tasks using templates and macros.

< Gif showing how to add a task >

> _Note: A hotkey can be assigned to this functionality in the "Hotkey" section found in Obsidian's general settingns._

### Live Editor Features

The Live Embedded Editor in the Add/Edit Task modal provides:
- Real-time preview of task content
- Syntax highlighting
- Auto-completion for tags
- Support for all markdown formatting
- Immediate feedback on task structure

### Task Properties You Can Add

In the Add Task window, you can easily add:
- Task title and description
- Priority level
- Due date, scheduled date, start date (v1.5.0)
- Tags (with tag suggester in v1.5.0)
- Status (v1.3.0)
- Reminders (v1.4.0)
- Recurring task rules (v1.5.0)
- Sub-tasks
- And more!

## Task Property Insertion

Task properties can also be added at the cursor position instead of only being appended at the end of the task. This gives you more control over task formatting.
