---
parent: Plugin Settings
title: Properties
nav_order: 3
---

# Properties Tab

Under this setting tab, you will find all the settings to configure the tasks properties which are used by both, inline-task and task-note.

## Custom statuses

In this setting you are adding a new and unique status for your task, inline-tasks as well as task-notes.

Under this setting you will see first all your current statuses as list items. Each item will show the information about the custom status. At the bottom of this list you will find two buttons :
- **Import from tasks plugin** : This custom statuses feature works similar to the one present inside the Tasks plugin. Hence, if you have already configured custom statuses for your inline-tasks in that plugin, you can easily import all of them to Task Board, through this single button.
- **Add new status** : This button will open a modal so you can configure various characteristics related to the custom status. In following section you will find all these characteristics.

### Characteristics

While adding a new custom status or editing an existing one, you basically configure the following characteristics related to the status : 
- Status symbol (only applicable for inline-tasks)
- Status name
- Status type
- Next status symbol to cycle

### Features

This **custom statuses** setting provides nice features as explained below : 

1. **Act like a scanning filter :** Only the inline-tasks whose checkbox symbols you have configured inside this setting will be scanned by the Task Board. This helps you to ignore certain type of checkbox items which you dont want to be get scanned as tasks.
2. **Status cycling :** You can create a nice automation workflow using this setting, just like how Jira and other professional project management softwares work. When you click on the checkbox of the task, it can move from one status to another, exactly the way you have configured it inside this setting. Additionally, if you have setup a Status based workflow Kanban board, then you will notice the task is moving from one column to another, in a flow.
3. **Provide contextual meaning to your statuses** : Since, this setting will work for inline-tasks as well as task-notes. For task-note frontmatter you will see the name of the status instead of the symbol, giving a professional software like feel.