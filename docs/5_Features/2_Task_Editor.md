---
parent: Features
title: Task Editor
nav_order: 2
---

## Task Editor

This custom view gives the user the ability to add new tasks to a file or files in various ways as well as assists with managing properties/[metadata](../Components/MetadataFormats.md) for tasks in a way that is compatible with your other plugins, as well as how you have it configured in the plugin's global settings. The window also provides a live preview as you type.

To understand the complete UI of this view, read the following wiki : [Task Editor UI](../5_Components/3_TaskEditor.md).

You can open the Task Editor modal by using either of the following two commands from the Obsidian's command palette : 
1. `Task Board : Add New Task in Current File` : Using this command you can add a task to the specific place where you have placed your cursor.
{: .note }

> Please note that before running the command, place your cursor in the editor where you want to add the task. For running the command its important that you are focusing inside an active editor.

2. 

It will be recommended that you add a shortcut to this command, so you can directly add a new task to the current file you are editing.

Ensure that, to run this command, or to open this pop-up window, you are suppose to be inside a markdown file editor. Inside the file place your cursor, where you want to add a new task, and the new task will appear at that line.

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
{: .d-inline-block }
v1.6.0
{: .label .label-blue }

Task properties can also be added at the cursor position instead of only being appended at the end of the task. This gives you more control over task formatting.
