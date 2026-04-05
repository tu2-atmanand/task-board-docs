---
parent: Features
title: Metadata Formats
nav_order: 3
---

# Metadata Format

Task Board supports different types of formats to add the metadata to your tasks.

## Compatible Plugin Format

You can choose one of the following options in the Task Board setting to keep the format of metadata globalized throughout your vault. You can see the supported format and the corresponding plugin option from below table :

| Plugin/Setting option | Priority             | Time duration                            | Created date           | Start date           | Scheduled date           | Due date           | Completion time-date               |
| --------------------- | -------------------- | ---------------------------------------- | ---------------------- | -------------------- | ------------------------ | ------------------ | ---------------------------------- |
| Task Board (Default)  | ⏫ or [priority:: 0-5]                   | ⏰[21:10 - 23:10]                         | ➕2024-10-31            | 🛫2024-10-31         | ⏳2024-10-31              | 📅2024-10-31       | ✅2021-10-31T21:52:22               |
| Tasks                 | ⏫                    | ⏰ 21:10 - 23:10                          | ➕ 2024-10-31           | 🛫 2024-10-31        | ⏳ 2024-10-31             | 📅 2024-10-31      | ✅ 2021-10-29                       |
| Dataview              | [priority:: highest] | [time:: 21:10 - 23:10]                   | [created:: 2024-10-31] | [start:: 2024-10-31] | [scheduled:: 2024-10-31] | [due:: 2024-10-31] | [completion:: 2021-10-31T21:52:22] |
| Obsidian Native       | Any                  | @time(21:10 - 23:10)                     | @created(2024-10-31)   | @start(2024-10-31)   | @scheduled(2024-10-31)   | @due(2024-10-31)   | @completion(2021-10-29)            |
| Day Planner           | Any                  | 09:00 - 10:00 (At the start of the task) | Any                    | Any                  | Any                      | Any                | Any                                |


- You also have the option to mix these formats with one another. For example, say you dont like to see the emojis for priority, you can use other format, and that will still work and Task Board will still scan them. But, if you are using the edit task modal of this plugin to edit the task, then the content will be sanitized to follow only one kind of format throughout, based on the format you have selected in the settings.
- **Any** mean, for this field, you can use any type of format from that column, for the specific plugin/setting option you have selected.
