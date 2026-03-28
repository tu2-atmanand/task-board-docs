---
parent: Features
title: Task Editor
nav_order: 4
---

# Task Editor

This custom component gives user the ability to add new task or edit an existing task in various ways as well as assists with managing properties/[metadata](../Components/MetadataFormats.md) for tasks in a way that is compatible with your other plugins, as well as how you have it configured in the plugin's global settings.

To understand the complete UI of this component, read the following wiki : [Task Editor UI](../6_Components/3_TaskEditor.md).


## Ways to Add a Task

### 1. **Add to Current File** 
The plugin provides a command to add new task to the currently opened markdown file at the cursor position.

Command : `Task Board : Add new task in current note`

> Please note that before running the command, place your cursor in the editor where you want to add the task. For running the command its important that you are focusing inside an active editor.

### 2. **Add to Pre-defined File**

Add tasks to a default note you've specified in settings, from anywhere in Obsidian. For this you can either use the following command...

Command : `Task Board : Add new task`

Command : `Task Board : Add new task-note`

Or you can make use of the `Add new task` button ![Add new task button](../../assets/add_new_task_icon.png) present at the top right corner inside the board.

### 3. **Add to Any File**

After you have opened the Task Editor, you also have the option to use the file suggester in the component to choose any file in your vault to add the task to. The task will be added at the end of the note.

### 4. **QuickAdd Integration**

Select from different QuickAdd choices to add tasks using templates or macros. Using QuickAdd plugin, the combinations are endless on how you want to add the task and where you want to add.

< Gif showing how to add a task >

> _Note: A hotkey can be assigned to all these commands functionality in the "Hotkey" section found in Obsidian's general settingns._


## Ways to Add a Task

This component will be specially useful when you want to edit a particular task but don't want to open the source file. You can make use of this component to quickly edit a specific property of the task.

There are two ways to open this component to edit an existing task : 

1. **Task Card Button** : Hover over the card and then you will notice a small edit icon at the bottom right corner of the task card. Click on that button which should open this component for that specific task.
2. **Right-click menu** : Right click on the card and then select the "Task editor" option. You will also find two additional options, which will allow you to open this Task Editor component as a Obsidian tab or as a pop-out window.

## Features

Below are some of the main features this component provides...

### Live Editing Features
{: .d-inline-block }
v1.5.0
{: .label .label-blue }

The Task Editor now provides:

- **Live Editor**: A full Obsidian live editor is embedded in this component so you get all the normal features of the note editor.
- **Dual View**: Switch between raw editor and live preview
- **Tag Suggester**: Easily add tags with autocomplete
- **Syntax Highlighting**: Better visibility of task properties
- **Real-time Validation**: Immediate feedback on task format

### Task properties you can add

You can add the following properties to the task :
- Task title, sub-task and description inside the editor.
- Status (v1.3.0)
- Start and End time.
- Created date, Due date, scheduled date, start date (v1.5.0)
- Priority level
- Tags (with tag suggester in v1.5.0)
- Reminder (v1.4.0)
- Child tasks (Dependencies or blocked-by tasks) (v1.8.0)


### Task Property Insertion
{: .d-inline-block }
v1.6.0
{: .label .label-blue }

Task properties can also be added at the cursor position instead of only being appended at the end of the task. This gives you more control over task formatting. Simply place your cursor where you want the specific property to be added and then add the property from the input field.

### Safe Editing
{: .d-inline-block }
v1.6.0
{: .label .label-blue }

Task Board now includes a [safeguard feature](./Safe_Guard.md) that performs proper content matching before updating your files. A [Content Compare modal](../6_Components/5_Content_Compare_Modal.md) shows you the changes before they are applied, ensuring you never lose content accidentally.