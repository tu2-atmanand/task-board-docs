---
parent: Features
title: Adding a new Task
nav_order: 1
---

# Adding a New Task

There are multiple ways to add a new task to the board. The first, normal method which you know is by directly writing inside the markdown file learn more here : [Adding new task from file](../How_To/HowToAddNewTask.md#from-file).

But this plugin gives you special functionality for adding tasks with ease as explained below.

## Add Task Window

This window gives you the power to add new task to a file with ease. Since various plugins have their own way of adding properties/[metadata](../Components/MetadataFormats.md) to the task, this window helps you to add the task content by following a global format and formatting all your tasks to follow the same format as configured by you in the setting.

**Enhanced in v1.5.0:** The Add Task window now includes a **Live Embedded Editor** that provides real-time preview of your task as you type.

### Ways to Add a Task

1. **Add to Current File**: The plugin provides a command to add new task to the currently opened markdown file.

2. **Add to Pre-defined File** (v1.5.0): Add tasks to a default note you've specified in settings, from anywhere in Obsidian.

3. **Add to Any File** (v1.5.0): Use the file suggester in the modal to choose any file in your vault to add the task to.

4. **QuickAdd Integration** (v1.5.0): Select from different QuickAdd choices to add tasks using templates and macros.

< Gif showing how to add a task >

> Assign a hotkey to this command to use this functionality faster.

{: .note }
> Please note that before running the command, place your cursor in the editor where you want to add the task. For running the command its important that you are focusing inside an active editor.

## Live Editor Features

**Added in v1.5.0**

The Live Embedded Editor in the Add/Edit Task modal provides:

- Real-time preview of task content
- Syntax highlighting
- Auto-completion for tags (v1.5.0)
- Support for all markdown formatting
- Immediate feedback on task structure

## Task Properties You Can Add

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

## Task Property Insertion (v1.6.0)

Task properties can now be added at the cursor position instead of always being appended at the end of the task, giving you more control over task formatting.
