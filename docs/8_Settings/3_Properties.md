---
parent: Plugin Settings
title: Properties
nav_order: 3
---

# Properties Settings

The Properties tab allows you to configure which task properties Task Board recognizes and uses. Here you can enable/disable different property types that the plugin will scan for and display.

## Available Task Properties

Task Board supports the following task properties:

| Property | Emoji | Format Example | Purpose |
|---|---|---|---|
| ID | 🆔 | `🆔 4` | Unique identifier for tasks (required for Map View) |
| Tags | # | `#tag` | Categorize tasks with multiple tags |
| Priority | 🔺 | `🔺 High` | Task urgency level |
| Start Date | 🛫 | `🛫 2024-01-01` | When task work should begin |
| Scheduled Date | ⏳ | `⏳ 2024-01-01` | When task is scheduled |
| Due Date | 📅 | `📅 2024-01-01` | Task deadline |
| Completion Date | ✅ | `✅ 2024-01-01` | When task was completed |
| Cancelled Date | ❌ | `❌ 2024-01-01` | When task was cancelled |
| Created Date | ➕ | `➕ 2024-01-01` | When task was created |
| Time | ⏰ | `⏰ 09:00-10:00` | Scheduled time block for task |
| Reminder | @ | `@(12:30)` | Time-based task reminder |
| Recurring | 🔁 | `🔁 every 2 weeks` | Task recurrence pattern |
| On-Completion | 🏁 | `🏁 delete` | Action to perform when task completes |
| Dependencies | ⛔ | `⛔ taskid1, taskid2` | Tasks that must complete first |

## Enabling/Disabling Properties

Use the toggles in this section to:
- **Enable** properties you want Task Board to recognize and scan
- **Disable** properties to ignore them during scanning

Disabling unused properties can improve scanning performance.