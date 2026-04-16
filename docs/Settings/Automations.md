---
parent: Plugin Settings
title: Automations
nav_order: 7
---

# Automations Tab

The Automations tab contains settings to automate task management workflows, reducing manual work and improving efficiency.

## Edit button action

| Input Field | Options | Default |
|---|---|---|
| Dropdown | **Task Editor (Modal)** - Opens task in floating dialog<br>**Task Editor (Tab)** - Opens task in a new tab<br>**Task Editor (Window)** - Opens task in external window<br>**Open note in new tab** - Opens source file in new tab<br>**Open note in right split** - Opens source file in right panel<br>**Open note in new window** - Opens source file in new OS window<br>**Open note in hover-preview** - Shows file in hover preview | Task Editor (Modal) |

Control what happens when you click the Edit button on a task card. Choose between:
- Editing within the plugin's Task Editor (recommended for quick edits)
- Opening the source markdown file in various Obsidian locations
- Viewing in hover preview

## Double click card action

| Input Field | Options | Default |
|---|---|---|
| Dropdown | None<br>Task editor (window)<br>Open note in new tab<br>Open note in right split<br>Open note in new window<br>Open note in hover-preview | None |

Using this setting you can configure the action you want to have when you double click on the [task item card](/docs/Components/Task_Item_Card.md).


## Restrict task completion to child-tasks and sub-tasks

| Input Field | Default |
|---|---|
| Toggle | OFF |

This is a nice feature which helps you to restrict from marking any task as complete until its sub-tasks and child-tasks has been marked as completed.

## Auto add selected universal date

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, the current universal date (selected in General settings) is automatically assigned to new tasks created via the "Add New Task" modal.

## Auto Add Created Date

| Input Field | Default |
|---|---|
| Toggle | ON |

When enabled, today's date is automatically added as the created date when you create a new task through the "Add New Task" modal.

{: .note }
> This only applies to tasks created via the Task Board plugin. Tasks added directly to markdown files won't get created dates unless you add them manually.


## Auto Add Completed Date

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, the current date-time is automatically added to the completion date property when you mark a task as complete.


## Auto Add Cancelled Date

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, the current date-time is automatically added to the cancelled date property when you mark a task as cancelled.

## Daily notes plugin compatibility

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, the name of your daily note, which must be a proper date value, will be virtually applied as the [universal date](./Formats.md#universal-date) to the task.

See : [Daily notes plugin integration](/docs/Features/Plugin_Integrations/Daily_Notes_Plugin.md).


## Day Planner Plugin Compatibility

| Input Field | Default |
|---|---|
| Toggle | OFF |

This setting will only allow you to enable itself, if the Day planner plugin is installed and enabled.

When enabled:
- Task times display according to Day Planner format in markdown
- Changes in Day Planner reflect in Task Board
- Timeline integration becomes available

See : [Day planner plugin integration](/docs/Features/Plugin_Integrations/Day_Planner_Plugin.md).

## QuickAdd Plugin Compatibility

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, allows integration with QuickAdd plugin for creating tasks through QuickAdd workflows.

See: [QuickAdd Plugin Integration](/docs/Features/Plugin_Integrations/QuickAdd_Plugin.md)


## Push notification compatibility

| Input Field | Options | Default |
|---|---|---|
| Dropdown | None<br>Reminder plugin<br>Obsi app | None |

Using this setting you can decide the format of the reminder property to use, to maintain a good integration with the other plugins/services you are using to get push notification functionality.

See : [Push notification services integration](/docs/Features/Plugin_Integrations/Notification_Services_Integration.md).