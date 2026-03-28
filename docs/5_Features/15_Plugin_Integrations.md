---
parent: Features
title: Plugin Integrations
nav_order: 15
---

# Plugin Integrations

Task Board integrates seamlessly with several popular Obsidian plugins to enhance your task management workflow. These integrations allow you to leverage the features of multiple plugins together.

## QuickAdd Plugin Integration
{: .d-inline-block }
1.5.0
{: .label .label-blue }

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
{: .d-inline-block }
1.5.0
{: .label .label-blue }

- **Custom statuses** : Task Board has its own setting to configure custom statuses. But in the same setting, this plugin also provides an option to easily import all the "Custom statuses" configurations from the Tasks plugin's [status system](https://publish.obsidian.md/tasks/Getting+Started/Statuses/About+Statuses).
- All the other common task properties are supported by Task Board to have a full integration. **Except two properties**...

{: .warning }
> At present Task Board dont support the following properties natively, neither it allows to enter these properties to the tasks, hence it is dependent on the Tasks plugin so that users can use them for inline-tasks. Task Board integrates well with the Tasks plugin's API so that the tasks with recurring property can still work from Task Board. : 
> - **Recurring tasks** :  Using this property you can configure to create a new task after the specified recurrence interval when you will mark the task as complete.
> - **On-Completion** : This property helps you to decide what happens to the task when it is marked as completed (through checkbox or by changing the status of the task to COMPLETED status type).

## Reminder Plugin Integration
{: .d-inline-block }
1.4.0
{: .label .label-blue }

Task Board integrates with reminder plugin to help you never miss a deadline:

### Features

- Add reminders using the same due date and scheduled time values
- Choose your preferred notification service in settings (v1.6.0)
- Formatted reminder property that works with your reminder plugin
- Date-time selector for setting reminders at any time on any date (v1.6.0)

### Supported Reminder Plugins

- Obsidian Reminder
- Other compatible reminder plugins that use standard notification formats

## Highlightr Plugin Integration
{: .d-inline-block }
1.4.0
{: .label .label-blue }

Style your tasks with highlighting:

- Add highlighting HTML tags like `<mark>` and `<font>` to your tasks
- Visual emphasis on important tasks or task sections
- Full rendering support in Task Board view

{: .note }
> Make sure the Highlightr plugin is enabled for this feature to work properly.

## Frontmatter Tags Inheritance
{: .d-inline-block }
1.6.0
{: .label .label-blue }

Also known as **Virtual Tags**, this feature allows:

- Task Board automatically applies frontmatter tags from notes to all the inline-tasks within those notes
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
{: .d-inline-block }
1.5.0
{: .label .label-blue }

Task Board now exposes few APIs for other plugins or scripts to use directly:

- Programmatically open the Add or Edit Task modal
- Extend Task Board functionality in your own plugins
- Build custom workflows around task management

Read more here : [Task Board APIs](../How_To/HowToUseAPIs.md).