---
parent: Features
title: Task card menu
nav_order: 21
---

# Task Card Menu
{: .d-inline-block }
v1.10.0
{: .label .label-blue }

## Overview

The **Task Card Menu** is a context menu that appears when you right-click on a [task card](/docs/7_Components/2_Task_Item_Card.md) in your board. On smartphones and tables, you can open this menu by long-pressing on the task card.

It provides quick access to common task operations without leaving the Kanban view, including editing properties, opening related files, and managing the task's associated note.

This menu centralizes all task-related actions into one convenient location, making it faster to manage tasks without switching contexts or opening modals.

## Menu Structure

The task card menu is organized into three main sections with labeled categories:

### Properties Section

Quick access to modify core task properties without opening the full task editor.

### Status

**Action**: Update task completion status

**Submenu opens with all available statuses:**
- Each status displays with its checkbox symbol and color coding
- Shows which status is currently applied to the task
- Click any status to instantly change the task's status

**Examples:**
- Change "TODO" (☐) to "In Progress" (◐)
- Mark task as "Done" (✓)
- Change to "Cancelled" (✗)

**What happens**: Task status updates in the markdown file and immediately refreshes in the board view.

### Priority

**Action**: Set or change task priority

**Submenu options depend on your configuration:**
- Low Priority
- Medium Priority
- High Priority
- Urgent Priority
- (Custom priority levels if configured)

Click any priority to instantly apply it to the task.

**What happens**: Task's priority property updates, and it may move to a different column if [priority-based columns](../6_Features/5_Type_of_Columns/0_index.md) are configured.

### Start Date

**Action**: Set when the task should begin

**Opens date picker modal** with:
- Calendar to select a date
- Clear button to remove the date
- Today/Tomorrow shortcuts

Use this to indicate when you plan to start working on the task.

### Scheduled Date

**Action**: Set when the task is scheduled for

**Opens date picker modal** for scheduling dates

Distinct from Start Date—useful if you want to distinguish between when to start and when the task is scheduled.

### Due Date

**Action**: Set the task deadline

**Opens date picker modal** to select a deadline

This is the primary deadline field, visible in most task displays. Sets urgency for task completion.

### Reminder

**Action**: Set a date and time reminder for the task

**Opens date/time picker modal** with:
- Calendar date selection
- Time selection (hours and minutes)
- Clear button to remove reminder

When the reminder time arrives, Obsidian will notify you (if [reminders are enabled](../8_Settings/0_index.md)).

---

### Task Actions Section

Operations related to the task itself.

### Copy Task Title

**Action**: Copy the task's title text to clipboard

**One-click copying** of just the task text (without checkbox, dates, or other formatting)

**Useful for:**
- Sharing the task description
- Pasting into messages or documents
- Quick reference without the markdown syntax

**Feedback**: You'll see a notice confirming "Task title copied successfully"

### Open Task Editor

**Action**: Open the full task editing modal

Opens the [Task Editor](../6_Features/4_Task_Editor.md) modal where you can:
- Edit task title and properties
- Add descriptions and notes
- Modify all fields comprehensively
- See side-by-side markdown preview

This is the same editor you'd open by double-clicking the task card.

### Open Task Editor in (Submenu)

Flexible ways to open the task editor in different layouts:

**Right Split**
- Opens task editor in a split panel to the right of your board
- Keep the board visible while editing
- Useful for updating multiple tasks

**New Window**
- Opens task editor in a floating window
- Smallest footprint option
- Good for dual monitors or precise positioning
- Window remembers its position

---

### Note Actions Section

Operations related to the file containing the task.

### Open Note

**Action**: Open the task's source note file

**Opens in**: Main editor tab (replaces current active tab)

View or edit the entire note that contains this task. Useful when you need to see tasks in their note context.

### Open Note to Right

**Action**: Open the task's source note file in a split panel

**Opens in**: Split panel on the right side

View the note side-by-side with the Task Board. Great for:
- Reviewing task context
- Editing the note while keeping board visible
- Cross-referencing other tasks in the same file

### More Note Actions (Advanced Submenu)

Extended file operations that Obsidian provides:

**Copy Path**
- Copies the file path to clipboard
- Useful for references or documentation

**Open in Default App**
- Opens the note file in your system's default markdown/text editor
- Allows editing outside of Obsidian if needed

**Show in System Explorer**
- Opens your operating system's file explorer
- Navigate to the file location directly
- Useful for moving, organizing, or viewing files

**Reveal File in Navigation**
- Highlights the file in Obsidian's file explorer panel
- Shows you where the note is located in your vault structure

**Move File To...**
- Opens a dialog to move the note to a different folder
- Reorganize your vault structure without leaving Task Board
- Helpful for archiving or reorganizing tasks

**Bookmark...**
- Creates a bookmark/shortcut to this file
- Quick access from Obsidian's sidebar bookmarks

**Scan Tasks from This File**
- Re-runs [Vault Scanner](../6_Features/9_Vault_Scanner.md) on this specific file
- Useful when:
  - You manually edited the file and want to resync
  - The board seems out of sync
  - You've added new tasks to the file

**Open in New Window**
- Opens the note in a separate, independent Obsidian window
- Full Obsidian interface in a new window
- Good for side-by-side work on different files

**Open in Hover Editor**
- Opens a floating preview/editing window within Obsidian
- Lightweight alternative to full editor
- Quick edits without leaving current context

**Start Presentation**
- Activates Obsidian's presentation mode for this note
- Present the note as a slideshow
- Useful for sharing or reviewing

**New Drawing**
- Creates an embedded drawing in the note using Excalidraw (if installed)
- Add visual diagrams alongside your tasks

**Rename Note**
- Opens a dialog to rename the file
- Enter new name (extension added automatically)
- File is renamed in your vault
- Note: Task references update automatically

**Delete Note**
- Moves the note to system trash
- Asks for confirmation
- All tasks in that note are removed from the board
- Note: Files can be recovered from trash

{: .warning }
> Deleting a note will remove all tasks from that file. Make sure, whether you want to delete just the single inline-task or the whole parent note which contains that inline-task.

## Common Workflows

### Quick Task Update
1. Right-click task card
2. Click "Status" and change to "In Progress"
3. Click "Due Date" and set deadline
4. Menu closes, task updates instantly
5. No modal required

### Edit Task with Context
1. Right-click task card
2. Click "Open Task Editor"
3. Make detailed edits in the modal
4. Context and full task properties visible
5. Save and return to board

### Review Note and Task
1. Right-click task card
2. Click "Open Note to Right"
3. View full note in split panel
4. See where task fits in the document
5. Edit note if needed

### Update After Manual Edit
1. You manually edited the note in another app
2. Right-click any task from that note
3. Click "More note actions" → "Scan tasks from this file"
4. Board refreshes with latest changes
5. Resync complete

### Archive Tasks by Moving File
1. Right-click task card
2. Click "More note actions" → "Move file to..."
3. Select archive folder
4. Tasks move with the file
5. Kept for reference but removed from active board

## Submenu Navigation

When a menu item has a submenu (indicated by an arrow `>`):

1. Hover over or click the item to open its submenu
2. The submenu appears to the right or left (depending on space)
3. Click on any submenu option to execute that action
4. Menu closes after selection

**Fast navigation**: You can move between submenus by moving your mouse left/right without clicking.

## Smart Features

### Context-Aware Options

The "More note actions" submenu is populated by Obsidian's native file menu. Depending on installed plugins and settings, you may see additional options beyond those listed here.

### Status Display

When viewing the Status submenu, the currently applied status shows a visual indicator so you know what's already set.

### Date Picker Enhancement

Date fields (Start Date, Scheduled Date, Due Date) all use the same date picker with:
- Single date selection
- Clear/remove date option
- Quick access buttons (Today, Tomorrow, etc.)

### Markdown-Safe Operations

All operations in this menu update only the specific task property being edited. You can:
- Edit task properties without affecting other markdown in the file
- Use this menu alongside manual markdown editing
- Remain safe knowing [Safe Guard](../6_Features/14_Safe_Guard.md) protects you

## Performance Tips

- **Right-click only once** - The menu appears at click location; don't need to right-click multiple times
- **Use dragging for reorganization** - For moving tasks between columns, use [Drag & Drop](../6_Features/17_Drag_Drop_Tasks.md) instead
- **Batch updates** - Update multiple properties quickly through the menu rather than opening full editor each time
- **Note operations for bulk changes** - Move, rename, or delete notes affect all tasks in that file at once

## Keyboard & Accessibility

- **Right-click** - Standard context menu trigger (works on all platforms)
- **No keyboard shortcuts** - Menu must be opened by right-clicking
- **Submenu navigation** - Mouse-based only (use arrow keys if your OS supports menu navigation)
- **Touch devices** - Long-press on task card (behavior depends on browser/device)

## Troubleshooting

**Menu doesn't appear**
- Make sure you're right-clicking directly on the task card
- Check that right-click isn't being intercepted by another plugin
- Try reloading the Task Board view

**Menu options are grayed out**
- Some options depend on task state or configuration
- For example, move/delete appear only if the source file is accessible
- Check plugin settings to enable features

**Changes don't appear immediately**
- Wait a moment for the file to be written
- The board should refresh automatically within 1-2 seconds
- If not, try scrolling or opening a different board and returning

**"More note actions" submenu is empty**
- The file may not be accessible
- Ensure the source note file exists in your vault
- Try "Scan tasks from this file" to resync