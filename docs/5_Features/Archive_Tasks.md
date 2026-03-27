---
parent: Features
title: Archive Tasks
nav_order: 8
---

# Archive Tasks

The Archive Tasks feature was introduced in version 1.5.0 and provides you with options to manage completed tasks without permanently deleting them. This is especially useful for maintaining a history of your work.

## Archive Options

Task Board offers two methods to archive your completed tasks:

### 1. Comment Out Tasks

When you archive a task using the comment-out method:
- The entire task content is converted to a comment in your markdown file
- The task becomes invisible in the Task Board but remains in your file
- You can easily restore the task by uncommenting it in your markdown file

**Example:**
```markdown
<!-- - [x] Completed task that is now archived -->
```

### 2. Move to Archive Note

With this method:
- Completed tasks are moved from their original location to a dedicated archive note
- You can specify which note to use as your archive
- Tasks maintain their format and all properties when moved
- Keeps your active task files clean while preserving task history

## How to Archive Tasks

1. **Configure Archive Settings**: Go to the Task Board settings and choose your preferred archive method
2. **Select Archive Location** (for Move to Archive Note method): Specify which note should be used as your archive
3. **Archive a Task**: When you delete a completed task from the board, it will be archived according to your settings

## Benefits of Archiving

- **Preserve History**: Keep a record of completed tasks for future reference
- **Clean Workspace**: Remove completed tasks from active view without losing them
- **Easy Restoration**: Restore archived tasks if needed
- **Project Documentation**: Maintain a complete history of what was accomplished

{: .note }
> Archiving is particularly useful for project management, allowing you to review completed work without cluttering your current task boards.

## Tips

- Set up a dedicated "Archive" folder in your vault for archived tasks
- Use date-based archive notes (e.g., "Archive-2025-01.md") to organize by time period
- Review your archive periodically to clean up or restore tasks
