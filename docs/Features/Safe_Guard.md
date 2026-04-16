---
parent: Features
title: Safe Guard
nav_order: 14
---

# Safe Guard

## Overview

The **Safe Guard** feature is a critical data protection mechanism in Task Board that prevents accidental data loss when task content becomes misaligned between what Task Board has cached and what currently exists in your vault files.

This feature acts as a safety checkpoint when you attempt to save changes to a task, ensuring that you don't inadvertently overwrite important modifications that may have been made to your tasks outside of Task Board (by another plugin, manual editor edits, or sync operations).

To understand the complete UI of this Safe Guard feature and to also understand it better using an example, see the following wiki : [Content compare modal](/docs/Components/Content_Compare_Modal.md).

## Why This Matters

When you edit a task in Task Board, the plugin stores the task content in its internal cache. However, your vault file is a living document that can be modified in various ways:

- **External Plugin Changes**: Other Obsidian plugins may modify task content
- **Manual Edits**: You might edit the task directly in your note editor
- **Sync Operations**: If you use cross-device sync, changes might occur on other devices
- **File System Changes**: Direct modifications outside of Obsidian

Without Safe Guard, Task Board could overwrite these external changes without warning, leading to potential data loss. Safe Guard detects these mismatches and gives you the control to decide which version of the content to keep.

{: .warning }
> Safe Guard protects your data by asking for confirmation when it detects unexpected changes. Disabling this feature could lead to unintended data loss.

## How It Works

### Normal Task Update Flow

When you save changes to a task, Task Board follows this process:

1. **Content Verification**: Compares the cached task content with the current content in your file
2. **Match Detection**: 
   - If content matches exactly → Task is safely updated
   - If differences are whitespace-only → Task is safely updated (auto-corrected)
   - If meaningful differences exist → Safe Guard modal appears

### Safe Guard Modal

When Safe Guard detects a content mismatch, it displays a **"Content mismatch detected"** modal with three versions of your task:

**Left Panel: "Content you just edited"**
- The version you just modified in Task Board
- This is what you intended to save

**Right Panel: "Current content in your note"**
- The actual content currently in your vault file
- This may have been changed outside of Task Board

**Highlighted Differences**:
- **Red highlights**: Show differences from the Task Board cache perspective
- **Green highlights**: Show differences from your recent edits perspective
- This makes it easy to spot what changed and where

### Your Options

You have two choices:

| Option | Action | Result |
|--------|--------|--------|
| **Use this** | Keep your edited version | Task Board saves your changes, replacing file content |
| **Keep this as it is** | Keep the current file version | Your Task Board edits are discarded, file content is preserved |
| **Abort** | Cancel the operation | No changes are made to either version |

{: .note }
> Choose **"Abort"** if the differences don't make sense to you. Then manually scan the file using Task Board's file scanner to resync the content.

## Debug Information

The Safe Guard modal includes a **Debug Info** section at the bottom that shows:

- **Task Board Cache**: What Task Board believed was the original content
- **Current content in your note**: What actually exists in your file now

This debug information helps you understand why the mismatch occurred and is useful for troubleshooting or reporting issues to developers.

## When Safe Guard Doesn't Appear

Safe Guard remains silent in these cases:

- ✓ No changes made to the task
- ✓ File content matches cached content exactly
- ✓ Differences are only whitespace/formatting (automatically handled)
- ✓ Safe Guard feature is disabled in settings

## Managing Safe Guard

### Disabling Safe Guard

If you find Safe Guard interferes with your workflow or creates too many prompts:

1. Go to **Task Board Settings** → **General** tab
2. Disable the **"Safe Guard Feature"** toggle
3. Task Board will proceed with updates without asking for confirmation

{: .warning }
> Disabling Safe Guard means Task Board will overwrite file content without checking for external changes. Use this only if you're confident about your workflow and file modifications.

### Re-enabling Safe Guard

To re-enable Safe Guard:

1. Go to **Task Board Settings** → **General** tab
2. Enable the **"Safe Guard Feature"** toggle
3. Safe Guard protection is activated again

## Best Practices

1. **Keep Safe Guard Enabled**: Leave this feature on as a safety net, especially if you use multiple plugins or edit tasks manually

2. **Review Differences**: When Safe Guard appears, carefully read the highlighted differences to make an informed choice

3. **Check Debug Info**: If you're unsure about a mismatch, review the debug information before making a decision

4. **Report Unexpected Patterns**: If Safe Guard appears frequently for the same file without obvious reasons, consider reporting it to help improve the plugin