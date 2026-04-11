---
parent: Task Formats
title: Inline task
nav_order: 2
---

# Inline Task

Also knows as **checklist item** or **checkbox item**, which are placed inside your notes as normal content but with special formatting. Throughout this wiki, will refer these kinds of tasks as "`inline-tasks`".

Task Board supports all kinds of checklist item formats. That is any formatted line which Obsidian renders as a checkbox element will be considered as a inline-task. Whether it may start with characters like '- [ ] ', '* [ ]', '+ [ ]' or even numbers like '1.[ ]', '1)[ ]', etc. These checklist item can even be indented using multi-level indentation.

## The Checkbox Pattern

All kinds of checkbox formats which are supported by Obsidian and rendered as checkbox items will be supported by Task Board. Below are the knows formats which are rendered as checkbox items : 

```md
- [ ] This is a normal task.
+ [ ] This is also a normal task.
* [ ] This is another normal task.
1. [ ] This is a numbered task.
1) [ ] This is a numbered task with a different format.
```

As well as indented tasks with any level of indentation will be scanned by Task Board. It can be inside a codeblock also.

{: .warning}
>Limitation
>
>The only limitation right now is, all checklist items inside a codeblock will be considered as a single line tasks. That is, tasks inside codeblocks cannot have sub-tasks and description to them. See the below example. 

```md
> ![NOTE] A Code Block
> This is a code block
> - [ ] This is a single line task.
>   - [ ] This is not a sub-task to the above task but its an individual task and will be scanned by Task Board as a separate task item.
>   This is a simple indented line and not the description of the above task.
```


## Task Title

This is the main title of any task. Most of the users would like to have a simple one liner task. It is advisable that while creating any task, give a short one line title to your task. If you want to explain what this task is about, you can add/elaborate it inside the **Description**.

These are all the properties you want to apply to the task. At present there are few main properties supported by Task Board and new properties will be added in the future.

## Task Metadata

Also know as the **task properties**. Task Board supports different types of formats to add the metadata to your inline-tasks.

You can choose one of the following options in the [Task Board setting](/docs/8_Settings/4_Inline_tasks.md#supported-plugin-formats) to keep the format of metadata globalized throughout your vault. You can see the supported plugin options and their corresponding formats from the below table :


| Plugin/Setting option    | ID         | Priority                         | Time duration                             | Created date            | Start date            | Scheduled date            | Due date            | Reminder                      | Completion date                    | Cancelled date                    | Depends on              |
| ------------------------ | ---------- | -------------------------------- | ----------------------------------------- | ----------------------- | --------------------- | ------------------------- | ------------------- | ----------------------------- | ---------------------------------- | --------------------------------- | ----------------------- |
| **Task Board (Default)** | 🆔224      | ⏫ or [priority:: 0-5]            | ⏰21:10 - 23:10                            | ➕2024-10-31             | 🛫2024-10-31          | ⏳2024-10-31               | 📅2024-10-31        | 🔔2024-10-30T10:30            | ✅2021-10-31T21:52:22               | ❌2021-10-31T21:52:22              | ⛔225, 226               |
| **Tasks**                | 🆔 224     | ⏫                                | ⏰ 21:10 - 23:10                           | ➕ 2024-10-31            | 🛫 2024-10-31         | ⏳ 2024-10-31              | 📅 2024-10-31       | 🔔 2024-10-30T10:30           | ✅ 2021-10-29                       | ❌ 2021-10-31T21:52:22             | ⛔ 225, 226              |
| **Dataview**             | [id:: 224] | [priority:: 2]                   | [time:: 21:10 - 23:10]                    | [created:: 2024-10-31]  | [start:: 2024-10-31]  | [scheduled:: 2024-10-31]  | [due:: 2024-10-31]  | [reminder:: 2024-10-30T10:30] | [completion:: 2021-10-31T21:52:22] | [cancelled:: 2021-10-31T21:52:22] | [depends-on:: 225, 226] |
| **Obsidian Native**      | @id(224)   | @priority(2)                     | @time(21:10 - 23:10)                      | @created(2024-10-31)    | @start(2024-10-31)    | @scheduled(2024-10-31)    | @due(2024-10-31)    | @reminder(2024-10-30T10:30)   | @completion(2021-10-29)            | @completion(2021-10-31T21:52:22)  | @dependson(225, 226)    |



- You also have the option to mix these formats with one another. For example, say you dont like to see the emojis for priority, you can use other format, and that will still work and Task Board will still scan them. But, if you are using the edit task modal of this plugin to edit the task, then the content will be sanitized to follow only one kind of format throughout, based on the format you have selected in the settings.
- **Any** mean, for this field, you can use any type of format from that column, for the specific plugin/setting option you have selected.



## Task Body

The Description section and the sub-tasks combined are called the **task body**.

- Always ensure  to have atleast one-level of indentation for any line to be considered as the part of the task body.
- Also, there should not be any empty line inside the task body, otherwise, the part after the empty line will be considered as a separate content even though it has an indentation. So, this criteria can be used to separate other content from the task content.

### Description

The description is basically the further elaboration of the task or even the sub tasks. You can explain as much as you want inside description, add images or attach documents. The description must be created by adding atleast one level indentation compared to the task title.

### Sub Tasks

To Create a subTasks for the main task, its is important that, there has to be atleast one Level indentation and there should not be any empty lines between the task title and the sub-tasks.

You can have any number of sub-tasks and with multi-level-indentation. For example:

```md
- [ ] Adding a new task to show multi-level sub-tasks | 📅 2024-10-29 #Test #Bug
    - [ ] This is a First level sub-Task.
        - [ ] This is a Second level sub-task.
            - [ ] This is a Third level sub-Task.
                - [ ] This is a Fourth level sub-Task. And so on.
            - [ ] This is another Third level sub-Task.
                - [ ] This is another Fourth level sub-Task. And so on.
```

## Point to remember

- At present, adding properties to sub-tasks is not possible. If you would like to do so. You shall convert your specific sub-task into to child-task, so that it can be shown as a separate card.

