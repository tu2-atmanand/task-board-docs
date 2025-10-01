---
parent: Features
title: Plugin Integrations
nav_order: 9
---

# Plugin Integrations

Task Board integrates seamlessly with several popular Obsidian plugins to enhance your task management workflow. These integrations allow you to leverage the features of multiple plugins together.

## QuickAdd Plugin Integration

**Added in version 1.5.0**

Task Board now integrates with the [QuickAdd plugin](https://github.com/chhoumann/quickadd) to provide powerful task creation capabilities.

### How It Works

- Create different **QuickAdd choices** for various types of tasks or projects
- Select any QuickAdd choice directly from the Add New Task modal
- Add tasks to specific locations based on your QuickAdd configuration
- Combine QuickAdd's macro functionality with Task Board's task management

### Benefits

- Streamlined task creation workflow
- Template-based task creation
- Automated task properties based on QuickAdd choices
- Integration with other QuickAdd features

{: .note }
> To use this feature, you need to have the QuickAdd plugin installed and configured in your vault.

## Tasks Plugin Integration

Task Board maintains strong compatibility with the [Tasks plugin](https://github.com/obsidian-tasks-group/obsidian-tasks):

### Task Status Support (v1.3.0)

- Use custom task statuses similar to the Tasks plugin
- Support for different checkbox states with emojis
- Integration with Tasks plugin's [status system](https://publish.obsidian.md/tasks/Getting+Started/Statuses/About+Statuses)

### Task Properties

- **Recurring tasks** (v1.5.0): Full support for recurring task syntax using Tasks plugin API
- **Scheduled date**: Track when tasks are scheduled to start
- **Start date**: Mark when you began working on a task
- **Created date**: Automatically track task creation time
- **Cancelled date**: Mark tasks as cancelled with a date
- Support for Tasks plugin metadata format

## Reminder Plugin Integration

**Added in version 1.4.0**

Task Board integrates with reminder plugins to help you never miss a deadline:

### Features

- Add reminders using the same due date and scheduled time values
- Choose your preferred notification service in settings (v1.6.0)
- Formatted reminder property that works with your reminder plugin
- Date-time selector for setting reminders at any time on any date (v1.6.0)

### Supported Reminder Plugins

- Obsidian Reminder
- Other compatible reminder plugins that use standard notification formats

## Highlightr Plugin Integration

**Added in version 1.4.0**

Style your tasks with highlighting:

- Add highlighting HTML tags like `<mark>` and `<font>` to your tasks
- Visual emphasis on important tasks or task sections
- Full rendering support in Task Board view

{: .note }
> Make sure the Highlightr plugin is enabled for this feature to work properly.

## Frontmatter Tags Inheritance

**Added in version 1.6.0**

Also known as **Virtual Tags**, this feature allows:

- Task Board automatically applies frontmatter tags from notes to all tasks within those notes
- Filter tasks by note-level tags without adding tags to individual tasks
- Cleaner task syntax while maintaining powerful filtering capabilities

### How It Works

If your note has frontmatter like:
```yaml
---
tags: [project, urgent]
---
```

All tasks in that note will inherit these tags and can be filtered accordingly in your board.

## Task Board API

**Added in version 1.5.0**

A public API for developers to integrate with Task Board:

- Programmatically open the Add or Edit Task modal
- Extend Task Board functionality in your own plugins
- Build custom workflows around task management

{: .note }
> API documentation is available for developers who want to build integrations with Task Board.
