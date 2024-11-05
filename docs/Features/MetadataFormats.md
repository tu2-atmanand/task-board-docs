---
parent: Features
title: Metadata Formats
---

# Metadata Format

Task Board supports different types of formats to add the metadata to your tasks.

**Metadata includes :**

- Due date.
- Time duration.
- Priority.
- Tags.
- Completion time-date.

More properties coming soon...

## Compatible Plugin Format

You can choose one of the following options in the Task Board setting to keep the format of metadata globalized throughout your vault. You can see the supported format and the corresponding plugin option from below table :

| Plugin/Setting option | Due date           | Time duration                            | Priority               | Tags  | Completion time-date               |
| --------------------- | ------------------ | ---------------------------------------- | ---------------------- | ----- | ---------------------------------- |
| Task Board (Default)  | 📅[2024-10-31]     | ⏰[21:10 - 23:10]                         | ⏫                      | #test | ✅ 2021-10-31T21:52:22              |
| Tasks                 | 📅 2024-10-31      | ⏰21:10 - 23:10                           | ⏫                      | #test | ✅ 2021-10-29                       |
| Day Planner           | Any                | 09:00 - 10:00 (At the start of the task) | Any                    | #test | Any                                |
| Dataview              | [due:: 2024-10-31] | Any                                      | [priority:: highest] * | #test | [completion:: 2021-10-31T21:52:22] |
| Obsidian Native       | @due(2024-10-31)   | Any                                      | Any                    | #test | @completion(2021-10-29)            |

- You also have the option to mix these formats with one another. For example, say you dont like to see the emojies for priority, you can use other format, and that will still work.
- **Any** mean, for this field, you can use any type of format from that column, for the specific plugin/setting option you have selected.

*Under Development
