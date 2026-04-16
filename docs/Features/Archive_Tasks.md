---
parent: Features
title: Archive Tasks
nav_order: 12
---

# Archive Tasks

The Archive Tasks feature provides you with options to manage completed tasks without permanently deleting them. This is especially useful for maintaining a history of your work.

## How to Archive Tasks

1. **Configure Archive Settings**: Go to the Task Board settings and
   1. **For inline-tasks :** Under the [Inline tasks setting tab](/docs/Settings/Inline_tasks.md#file-for-archived-tasks), select the path of the note where your archived tasks should be moved.
   2. **For task-notes :** Under the [Task notes setting tab], configure the path of the folder where all your archived task-notes should be moved.
2. **While deleting :** When you will try to delete a task using either the delete button on the [task item card](/docs/Components/Task_Item_Card.md) or through the right-click menu, you will see a third button called **Archive instead**.
3. **Through right-click menu :** You will also find an option inside the [task card menu](/docs/Features/Task_Card_Menu.md) to archive the specific task.


## For inline-tasks

Task Board offers two methods to archive your inline-tasks:

### 1. Comment Out Tasks

This will only happen if you have set the value of the "[File for archived tasks](/docs/Settings/Inline_tasks.md#file-for-archived-tasks)" setting as empty.

When you will archive the task, it will be simply commented out inside the same note, like this : 
**Example:**
```markdown
%%  - [x] Completed task that is now archived %%
```

This will help you to hide this task in Obsidian's live editor and reading mode. But when you will switch to the source mode, you will still able to see the content there. It will be just simply kept hidden to your eyes.


### 2. Move to Archive Note

This will be possible when you have set a correct path to a archived inline-tasks note inside the "[File for archived tasks](/docs/Settings/Inline_tasks.md#file-for-archived-tasks)" setting.

With this method:
- Completed tasks are moved from their original location to a dedicated archive note
- You can specify which note to use as your archive
- Tasks maintain their format and all properties when moved
- Keeps your active task files clean while preserving task history

## For task-notes


## Benefits of Archiving

- **Preserve History**: Keep a record of completed tasks for future reference
- **Clean Workspace**: Remove completed tasks from active view without losing them
- **Easy Restoration**: Restore archived tasks if needed
- **Project Documentation**: Maintain a complete history of what was accomplished
- **Optimize Performance :** Archived task files are note scanned by Task Board, which boosts its performance during vault scanning.

{: .note }
> Archiving is particularly useful for project management, allowing you to review completed work without cluttering your current task boards.

## Best Practices

- Set up a dedicated "Archive" folder in your vault for archived tasks
- Use date-based archive notes (e.g., "Archive-2025-01.md") to organize by time period
- Review your archive periodically to clean up or restore tasks

{: .note }
> Another best practices to follow inside Obsidian is to have atomic notes. So, archiving all the inline-tasks inside a same note will make it very huge over time and it might be even difficult to manage and read for the user. Also, its performance will be degraded. 
> 
> To solve this issue, we have a new feature on roadmap to have a "Archived inline-tasks folder" instead of a single file and then all your inline-tasks will go to a specific note inside this folder with the note's name as the month-year name.
>
> Follow the development status of this feature here : [tu2-atmanand/task-board#702](https://github.com/tu2-atmanand/Task-Board/issues/702).