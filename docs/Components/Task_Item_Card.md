---
parent: Components
title: Task Item Card
nav_order: 3
---

# Task Item Card

These is the card which you see inside the column under any specific board.

![Task Item Card](../../assets/TaskItemLegend.png)

## Header

The Header section of this card will consists of the following three things :

**1. Priority :** You will be able to see the priority of the task which you gave to this task.

**2. Tags :** All the tags you have given to this task will be show here in horizontal aligned style.

**3. Card Drag Icon :** Upcoming Feature ...

## Task Title

This is the main content of the task, the short summary. You can give any type of formatting as normally you give in markdown format.

## Sub Tasks

This section will show you all your sub-task of the main task. They will be arranged in vertical position, one below the other, as you have placed them in the markdown file, same order will be preserved. These sub-tasks will have their own checkboxes to change their status and they will be indented from the main task.

This section will also show multi-level indented sub-tasks as well in the same order, as they appear in the markdown file. The indented length will be changed based on the layout.

## Task Description

By default the Task Description content will be hidden. You will see a light colored text `Show Description`. This is actually a clickable text, and once you click on this text, the Description Section will expand.

The Description content is kept hidden by default is because, there can be a lot of content inside the description for the task, and keeping in visible will consume a lot of board area, which will defeat the methodology of a Kanban Board. Whenever you want to take a look at the content of the Description of any specific task, you can expand it and read the content or make use of the links from the content.

Another thing is, the content will be compressed, that, is the indentation of the content lines will be removed to save space. The idea here is to just show the content and not to worry about the formatting much, although all the other formatting will be applied like bold, italic, etc. The indentation is removed to again, show all the content in as much less area as possible. You can look at the actual content by opening the [Edit Task Window](./EditTaskWindow.md) or by directly opening the markdown file.

## Footer

The Footer section will show the following three task properties :

**1. Task Start and End Time (Duration) :** There will be a clock icon followed by the start and end time of the task will be shown. From this you will be able to find out the duration of the task.

**2. Task Due Date :** After the Task Duration, you will be able to see the Due date of the task separated from the Duration value by a Pipe symbol. The Due Date will be mention using a Calender Icon before its value.

**3. Button Section :** On the far right in this section, you will able to see two main button, first one is the `Edit Task` button, which will open the Edit Task Window and the second button is `Delete Task`, which will simply delete the task from the board as well as the content will also be removed from the parent markdown file.
