---
parent: UI Components
title: Task Formats
nav_order: 1
---

# Task Formats

There are two kinds of tasks in Obsidian : 
- [Inline Tasks](#inline-tasks)
- [Note per Tasks](#note-per-tasks)

Task Board supports both kinds of tasks.


## Inline Tasks

Also knows as checklist items or checkbox items, which are placed inside your notes as normal content but with special formatting. Throughout this wiki, will refer these kinds of tasks as "`inline-tasks`".

Task Board supports all kinds of checklist item formats. That is any formatted line which Obsidian renders as a checkbox element will be considered as a inline-task. Whether it may start with characters like '- [ ] ', '* [ ]', '+ [ ]' or even numbers like '1.[ ]', '1)[ ]', etc. These checklist item can even be indented using multi-level indentation.

### The Checkbox Pattern

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


### Task Title

This is the main title of any task. Most of the users would like to have a simple one liner task. It is advisable that while creating any task, give a short one line title to your task. If you want to explain what this task is about, you can add/elaborate it inside the **Description**.

### Task Metadata

These are all the properties you want to apply to the task. At present there are few main properties supported by Task Board and new properties will be added in the future.

> Read the following wiki understand all the task properties and their formats in detail :[Task Metadata](/docs/6_Features/3_MetadataFormats.md)


### Task Body

The Description section and the sub-tasks combined are called the **task body**.

- Always ensure  to have atleast one-level of indentation for any line to be considered as the part of the task body.
- Also, there should not be an empty line inside the task body, otherwise, the part after the empty line will be considered as a separate content even though it has an indentation. So, this criteria can be used to separate other content from the task content.

#### Description

The description is basically the further elaboration of the task or even the sub tasks. You can explain as much as you want inside description, add images or attach documents. The description must be created by adding atleast one level indentation compared to the task title.

#### Sub Tasks

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


## Note per Tasks

This is a new idea which got popularized through the TaskNotes plugin. Read this docs from TaskNotes to learn more : [The Note-Per-Task Approach](https://tasknotes.dev/core-concepts/). Throughout this wiki, will refer these kinds of tasks as "`task-notes`".

Task Board also adheres to the same concepts and provides various features to manage your task-notes. Also refer the following wiki to learn more about the integration of Task Board with TaskNotes plugin : [TaskNotes plugin integration](/docs/6_Features/15_Plugin_Integrations/8_TaskNotes_Plugin_Integration.md).