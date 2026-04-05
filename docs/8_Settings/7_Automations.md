---
parent: Plugin Settings
title: Automations
nav_order: 7
---

# Automations settings

### Edit button mode

| Input Field | Dropdown Options                                                                                                                          | Default Value                |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Dropdown    | Use Task Editor feature<br>Open note in new tab<br>Open note in right split<br>Open note in new window<br>Open note in hover preview | Use Task Editor feature |

### Auto add due date to tasks

| Input Field   | Default Value |
|---------------|---------------|
| Toggle Button | ON            |

This option help you add due date automatically if you havent entered any value for the due input field inside the [Add/Task Editor](../Components/EditTaskWindow.md). This feature only works when you are adding a new task using the Window provided by this plugin.

{: .note }
> When you will be editing a task and if the task do not have any due date set to it, this feature will auto-assign today's date as a due date to that task. So keep this in mind if you have enabled this feature. If you do not want this functionality, you can disable this.

## Compatibility for other plugins

Task Board supports compatibility options, so that it can work with other plugins seamlessly. This helps the developer and the users, so that we don't re-build the wheel, instead use what is already existing, which also gives lot of freedom to the users to use Obsidian efficiently.

### Day planner plugin compatibility

| Input Field   | Default Value |
|---------------|---------------|
| Toggle Button | OFF           |

[Day Planner plugin](obsidian://show-plugin?id=obsidian-day-planner) is an amazing plugin because of its timeline feature and calender feature. You can easily make changes from the this plugin and the changes will be reflected back to the Task Board. Also, once you set time to your plugins, it will be shown inside the timeline. Enable or disable this feature if you have installed the plugin.

### Daily Notes plugin compatibility

| Input Field   | Default Value |
|---------------|---------------|
| Toggle Button | ON            |

Daily notes is a core plugin, using which you create daily notes. Since the files you create have a name like a date, for example if your today's file is `2024-11-1.md`, then you can use this feature for considering all the tasks under this file which do not have a due date set to them in their metadata to schedule for today itself. That is inside the [Task Item Card](../Components/Task_Item_Card.md) you will see that the tasks under the daily note file, will be given the due date as per the name of that file, even if you haven't provided or forgot to provide a due date for it. This is very helpful since, its obvious that, if you have added any task under today daily file, then that file has been due for today. If you do not like this functionality, you can disable this feature, in which case you will be required to set the due date yourself, either from the Task Editor or manually, using plugins like [Tasks](obsidian://show-plugin?id=obsidian-tasks-plugin).
