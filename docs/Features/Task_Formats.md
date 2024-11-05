---
parent: Features
title: Task Formats
---

# Task Formats

This plugin only works for a specific type of tasks, which are in a particular format.

The following image will help you to understand the nomenclature to read this documentation efficiently and understand the parts of a Task.

< Image >

## The Checkbox Patter

Obsidian supports three types of pattern to create a checkbox or in other words a task item as shown below  :

```md
- [ ] 
+ [ ] 
* [ ] 
```

But this plugin only works for the first kind of checkbox or detects any line as task, if it starts with the following patter :

```md
- [ ] 
```

So, if you want the plugin to not detect any of your task and consider the task as normal text, then you can use the other types of formats. This even works for sub-task. Any sub-tasks with the patter other than supported by this plugin, will be considered as a description content for the task and will be shown under the Description section and not as a sub-task.

## Sub Tasks

To Create a subTasks for the main task, its is important that, there has to be atleast one Level indentation and there shouldnt be any empty lines between the main task or the task title and the sub-task.

- If you are adding multiple tasks one after the another, then those will be considered as different tasks but if you have added a body to a new task, then the next task should be after an empty line from the last task.

## Task Description
