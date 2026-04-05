---
parent: Plugin Integrations
title: Introduction
nav_order: 1
---

# Plugin Integrations

Task Board integrates seamlessly with several popular Obsidian plugins to enhance your task management workflow. These integrations allow you to leverage the features of multiple plugins together.

Please find below various plugins and external services and applications to which Task Board provides solid integration.

## [Tasks plugin](https://github.com/obsidian-tasks-group/obsidian-tasks)

Since this is the most popular plugin for inline-tasks, Task Board has provided full compatibility with this plugin. Most importantly, Task Board depends on this plugin for two feature, "**recurring-tasks**" and "**on-completion property**", to work for inline-tasks, which are not supported inside Task Board natively. Additionally, you can also import your custom statuses from Tasks plugin.

Read more here : [Tasks plugin integration](./2_Tasks_Plugin.md).

## [QuickAdd plugin](https://github.com/chhoumann/quickadd)

QuickAdd plugin's integration boost the productivity of Task Board plugin. Since, through QuickAdd plugin, you can easily add content to any note at any specific place you want. Easily create such "choices" inside QuickAdd plugin, then easily use these "choices" inside the [Task Editor](../4_Task_Editor.md) so your new tasks can go to the specific note. You also have the option to [set a default QuickAdd "choice" in the setting](../../4_How_To/6_HowToUseGlobalSettings.md).

Read more here : [QuickAdd plugin integration](./3_QuickAdd_Plugin.md).

## [Day Planner plugin](https://github.com/ivan-lednev/obsidian-day-planner)

Day planner plugin helps you to add time duration to your tasks. When you will enable the integration for this plugin, Task Board will start adding the time duration property to the start of the inline-task in the same format, so these tasks works correctly in the Day planner plugin's features.

Read more here : [Day Planner plugin integration](./4_Day_Planner_Plugin.md).

## [Reminder plugin](https://github.com/uphy/obsidian-reminder)

Reminder plugin helps you to get system level notifications on your desktop. When you select the integration of this plugin in the Task Board's setting, the reminder property will be added as per this plugin's setting, so the reminder can be created easily.

Read more here : [Reminder plugin integration](./5_Reminder_Plugin_Integration.md).


## Notification services

Obsidian application doesnt allow any system level notification directly on smartphone devices, hence plugins also cannot have the power to provide system level notifications. But, there are few external applications/services which are specifically build for Obsidian to get nice notifications for the tasks/reminders you have added in your notes.

Read more here : [Notification Services Integration](./6_Notification_Services_Integration.md)


## [Highlightr plugin](https://github.com/chetachiezikeuzor/Highlightr-Plugin)

Highlightr plugin basically helps to highlight the specific content in your notes using HTML based color styling. To support this format, Task Board correctly identifies such content and ignores it, so there is no interference from both this plugin. For that matter, any plugin which makes use of the `<mark>` HTML tag will work properly inside Task Board.

Read more here : [Highlightr plugin integration](./7_Highlightr_Plugin_Integration.md).


## [TaskNotes plugin](https://github.com/callumalpass/tasknotes)

TaskNotes plugin has popularized the idea of note-per-task. A lot of users has adopted this idea to manage their tasks. Although, Task Board plugin had [already proposed a similar idea](https://github.com/tu2-atmanand/Task-Board/issues/33) long before the release of this plugin and Task Board dont encourage its users to create a note directly for each task. But after looking at the popularity of this idea, Task Board has decided to provide a strong integration with TaskNotes plugin. 

This plugin has a lot of very nice features, such as integrated calendar and integration with external calendar services, etc. Hence, this integration allows you to leverage the features of TaskNotes plugin along with Task Board features.

Read more here : [TaskNotes plugin integration](./8_TaskNotes_Plugin_Integration.md)

## Task Board API

Task Board now exposes few APIs for other plugins or scripts to use directly:

- Programmatically open the Add or Edit Task modal
- Extend Task Board functionality in your own plugins
- Build custom workflows around task management

Read more here : [Task Board APIs](./9_TaskBoardAPIs.md).