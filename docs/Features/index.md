---
title: Features
nav_order: 4
---

# Task Board Features

Following are some of the key features  of this plugin.

### Task Formats

This plugin supports all kinds of checklist item formats. That is any formatted line which Obsidian renders as a checkbox element will be considered as a inline-task. Whether it may start with characters like ‘- [ ] ‘, ‘* [ ]’, ‘+ [ ]’ or even numbers like ‘1.[ ]’, ‘1)[ ]’, etc. These checklist item can even be indented using multi-level indentation, can be inside a codeblock or can have sub-tasks and description.

Checkout in Details here : [Task Formats](../Components/Task_Formats.md)

### Adding a Task

There are two way you can add a task to the Task Board. First is the usual old method of directly writing down the task inside the markdown file. The second method is using a **Add New Task** Window to add different properties to the task using input elements to make the adding properties easy and ensuring the format comes properly.

Checkout detailed information here : [Adding new Task](./AddingANewTask.md)

### Editing a Task

![Editing a Task from Board](../../assets/EditTaskWindow.gif)

Edit task directly from the Edit Task Window. You can add different properties to the task, add more subTask, add or edit description to the task. And the changes will be return to the parent markdown file exactly the way you see it in the preview.

Checkout detailed information here : [Editing a task](./EditingATask.md)

### Marking as Complete

![Marking Task as Complete](../../assets/MarkTaskComplete.gif)

Marking a Task as complete from the board is real-time, as soon as you will mark or un-mark the task, the changes will be instantly made in the parent markdown file.

Checkout detailed information here : [Marking a task complete](./MarkingTaskComplete.md)

### Deleting a Task

Directly delete unwanted task from the board using the delete Icon. The task will also be deleted from the parent markdown file.

### Archive Tasks

**Added in version 1.5.0**

Archive your completed tasks instead of permanently deleting them. Choose between commenting out tasks in your files or moving them to a dedicated archive note to maintain a history of your work.

Checkout detailed information here : [Archive Tasks](./Archive_Tasks.md)

### Search Tasks

**Added in version 1.6.0**

Quickly find specific tasks on your board using the search functionality. Search through task content in real-time to locate the tasks you need.

Checkout detailed information here : [Search Tasks](./Search_Tasks.md)

### Plugin Integrations

Task Board integrates seamlessly with several popular Obsidian plugins including QuickAdd, Tasks plugin, Reminder plugins, and Highlightr. These integrations enhance your workflow and provide powerful features.

Checkout detailed information here : [Plugin Integrations](./Plugin_Integrations.md)

### Mobile Support

**Added in version 1.4.0**

Task Board now works great on mobile devices with optimized UI/UX for phones and tablets. Manage your tasks on the go with touch-friendly controls and responsive layouts.

Checkout detailed information here : [Mobile Support](./Mobile_Support.md)

### Applying Filters

At present there are mainly two types of filters. The first one is [Filters for Scanning](./Filters_for_Scanning.md), which is a very powerful feature and give you the option to scan only specific folder, file to look out for tasks and also only scan tasks with certain tags on them.
The second type of filters, are [Board Filters](../How_To/HowToUseBoardSettings.md#Board%20Filters) which allows you to only show the tasks with certain tags in them. You can use this filters to search for few related tasks.

A new type of filters are coming soon, called as Column Filters to filter out tasks under any column.

### Multi-Language Support

The plugin currently supports more than 20 languages and new languages are planned to being  added in subsequent releases. Although a proper care has been taken to translate the default english language to other languages, the exact content meaning cannot be guaranteed, since online services has been used to translation.
Your contribution for updating the current content in any language or adding a new language will be highly appreciated. It will be easy but a powerful step to make this plugin, accessible to many people. Read this doc to learn to contribute for Language Translation : [Contribute To Language Translation](../Advanced/Contribution_For_Languages.md).

### Re Scan Vault

This is a Special feature which allows you to Scan your whole vault to detect any undetected changes or when you update the [Scan Filters](./Filters_for_Scanning.md) settings from the Global Settings.
