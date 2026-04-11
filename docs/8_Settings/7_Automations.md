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


## Restrict task completion to child-tasks and sub-tasks


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



## Day Planner Plugin Compatibility

| Input Field | Default |
|---|---|
| Toggle | OFF |

{: .warning }
> [Day Planner plugin](obsidian://show-plugin?id=obsidian-day-planner) integration has a known issue. Consider using alternatives.

When enabled (if Day Planner is installed):
- Task times display according to Day Planner format in markdown
- Changes in Day Planner reflect in Task Board
- Timeline integration becomes available

## QuickAdd Plugin Compatibility

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, allows integration with [QuickAdd plugin](obsidian://show-plugin?id=quickadd) for creating tasks through QuickAdd workflows.

See: [QuickAdd Plugin Integration](../6_Features/15_Plugin_Integrations/3_QuickAdd_Plugin.md)


## Push notification compatibility



