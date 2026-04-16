---
parent: Plugin Integrations
title: Tasks plugin
nav_order: 3
---

## Tasks Plugin Integration
{: .d-inline-block }
1.5.0
{: .label .label-blue }

Link to the plugin : [Tasks plugin](https://github.com/obsidian-tasks-group/obsidian-tasks).

Task Board maintains strong compatibility with the Tasks plugin for the following features :

- **Custom statuses** : Task Board has its own setting to configure custom statuses. But in the same setting, this plugin also provides an option to easily import all the "Custom statuses" configurations from the Tasks plugin's [status system](https://publish.obsidian.md/tasks/Getting+Started/Statuses/About+Statuses).


All the other common task properties are supported by Task Board to have a full integration. **Except two properties**...

{: .warning }
> At present Task Board dont support the following properties natively, neither it allows to enter these properties to the tasks, hence it is dependent on the Tasks plugin so that users can use them for inline-tasks. Task Board integrates well with the Tasks plugin's API so that all the below feature can still work through this plugin : 
> - **Recurring tasks** :  Using this property you can configure to create a new task after the specified recurrence interval when you will mark the task as complete.
> - **On-Completion** : This property helps you to decide what happens to the task when it is marked as completed (through checkbox or by changing the status of the task to COMPLETED status type).