---
parent: Plugin Integrations
title: TaskNotes plugin
nav_order: 4
---

## TaskNotes Plugin Integration
{: .d-inline-block }
1.9.0
{: .label .label-blue }

Link to the plugin : [TaskNotes plugin](https://github.com/callumalpass/tasknotes).

TaskNotes plugin popularized the idea of creating note-per-task. For each of your task you should create a new note where the title and all the properties of the task are stored inside the frontmatter of the note. And any additional information about the task such as description, sub-tasks, etc. can be added as the body of the note.

Additionally, this plugin has some very nice features such as integrated calendar, integration with online calendar services, pomodoro etc.

For users to use this features of TaskNotes together with Task Board plugin, we have a strong integration.

Task Board has provided the following functionalities to achieve this integration : 

- **Frontmatter formatting setting** : You will find this setting under the "Task notes" inside the plugin's setting tab where you can configure the frontmatter property names, so they remain compatible with the TaskNotes configurations. This will make sure that, all the task-notes are read and updated property by both these plugins at the same time maintaining a standard format for the frontmatter.
- **Add new task-note command** : In the command palette you will find a command with the name "`Task Board: Add new task-note`". Using this command you can easily create a new task-note which will be also compatible with TaskNotes plugin.


## Limitation

At present, Task Board does'nt support the following features hence, these features compatibility will not work as expected from Task Board : 

- **Recurring task-notes** : Task Board will not read or make use of the recurring property set inside the frontmatter of your task-notes. Also, there is no easy way right now to provide an integration with TaskNotes to manage recurring tasks. Hence, any operations done on recurring tasks through Task Board will not work for task-notes.