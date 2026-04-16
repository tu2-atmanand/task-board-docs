---
parent: Plugin Integrations
title: Notification Services
nav_order: 8
---

## Notification Services Integration

Task Board is aware of the following external Applications which provides a system level notifications for the tasks/reminders you have added in your notes : 

- [VaultMate App](https://vaultmate.app/) (Android and IOS)
- [Notifiann App](https://github.com/pericles-tpt/notifian?tab=readme-ov-file) (Android)

Read below section to understand how Task Board provides the integration with each of these applications and services.

## VaultMate App

This is app is available on Android and IOS platform. It scans all the tasks from your vault and shows them inside its own interface.

The way this app works is, when you add a reminder property to your task through this app first checks if a scheduled date property is already present or not. If its already present it will keep it as it is. If a scheduled date property is not present, it will add today's date as the scheduled date property and it will add the time value in the following format : `(@11:10)`. So, if : 
- You are using the Tasks plugin format, then two properties will be added to your inline-task : ⏳ 2026-04-05 (@11:10)
- You are using Dataview plugin format, then only one property will be added to your inline-task : `[scheduled:: 2026-04-05T11:10:01]`.

*The date and date-time format is configurable.

To make this process of adding reminders to your tasks simpler, when you will select the "VaultMate" option in the Push notification compatibility setting, Task Board will add the reminder property the same way VaultMate app add it. And when your tasks will be synced inside the VaultMate app, the notification will be automatically generated through the app.


## Notifian App

Coming soon...