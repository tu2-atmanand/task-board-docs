---
parent: Features
title: Bug Reporter
nav_order: 20
---

# Bug Reporter

## Overview

The **Bug Reporter** is a built-in diagnostic system designed to capture, log, and help you report issues when Task Board encounters problems. It serves two critical functions:

1. **For Users** - Easily collect and submit bug reports with complete system context, as well as get solution if provided in the report.
2. **For Developers** - Gather comprehensive debugging information including system state, plugin versions, and exact error messages

When an error occurs, you'll see a notification that lets you review the details and prepare a report for the developers. All reported bugs are automatically logged to your vault for documentation and export.

## Why This Matters

Software bugs are inevitable. The Bug Reporter ensures that when you encounter a problem:

- **Nothing is lost** - Complete error context is automatically captured
- **Developers have context** - System information helps identify root causes faster
- **Your privacy is protected** - You can review and sanitize any personal information before submitting
- **Issues are tracked** - All bugs are logged locally with timestamps for reference

Without this feature, you'd need to manually note down error details and try to remember what your system configuration was—the Bug Reporter handles this automatically.

## How It Works

### When a Bug Is Detected

1. **Notification appears** - A banner notification pops up indicating an error occurred
2. **Once per bug** - The same bug won't show the notification twice (de-duplication by bug ID)
3. **You can view details** - Click "Show Error" to open the detailed [Bug Reporter modal](/docs/Components/Bug_Reporter_Modal.md)
4. **Click ignore** - Or dismiss it if you prefer

### Bug Notification Notice

When Task Board detects an error, you see this notice:

```
[i] An error has been encountered within Task Board. Click below to view error details.
[Button: Show Error] [Button: Ignore this bug]
```

{: .note }
> The same bug won't show twice during a session. If you dismiss it, future instances of that exact bug won't notify you again (until you close and open Obsidian application again).

### Bug Reporter Modal

If you click "Show Error", a detailed modal opens showing:

**BUG ID**
- Unique identifier for this type of bug
- Used by developers to track specific issues

**Message for User**
- Human-readable explanation of what went wrong
- May suggest workarounds or next steps

**Error Message**
- The technical error details
- Contains the exact exception or failure message

**Context**
- Where in the code the error occurred
- Which function or operation was running
- Helps developers locate the problem quickly

**System Information**
- Obsidian version and build
- OS and platform information
- List of all enabled plugins and their versions
- Other environment details

**Additional Information Section**
- Instructions for reporting the bug
- Two options: Email or GitHub

Learn more about the UI of this modal in the following wiki : [Bug reporter modal](/docs/Components/Bug_Reporter_Modal.md).

## Reporting a Bug

Once you have the Bug Reporter modal open, follow these steps:

### Step 1: Review the Report

Read through the error information, especially the "Error Message" section. This helps you understand what went wrong.

### Step 2: Check for Personal Information

Examine the "System Information" and "Error Message" sections for any personal data:

- File names or vault paths that contain private information
- User names or email addresses
- Sensitive file content in the error message

{: .warning }
> **Privacy**: If you find personal information in the report, you **must replace it** before submitting. The Bug Reporter cannot automatically detect and remove all personal data.

### Step 3: Copy the Report

Click the **"Copy Report"** button to copy the entire bug report to your clipboard.

The report is formatted as markdown, making it easy to paste into GitHub or email.

### Step 4: Submit to GitHub

**Preferred Method** - Public GitHub Issue (faster fixes, visible to community)

1. Click the GitHub issue link in the modal (or navigate to [New GitHub Issue](https://github.com/tu2-atmanand/Task-Board/issues/new))
2. Paste the bug report into the issue description
3. Add any additional context:
   - Steps to reproduce the bug
   - Screenshots/screen recordings
   - When the bug started occurring
   - Any workarounds you've discovered
4. Click "Create issue"

### Step 5: Submit via Email

**Alternative Method** - Direct to Developer

1. Copy the report (as above)
2. Email to [sanketgauns8@gmail.com](mailto:sanketgauns8@gmail.com)
3. Include:
   - A descriptive subject like "Task Board Bug: [brief description]"
   - Steps to reproduce
   - Screenshots if helpful
4. The developer will prioritize and follow up


## Log File Management

### Where Logs Are Stored

Bug reports are automatically saved to:

```
.obsidian/plugins/task-board/task-board-logs.log
```

This file contains:

- **System Information** - Updated each time the log file is modified
- **Recent Bug Reports** - The last 20 bugs encountered
- **Timestamps** - When each bug occurred
- **Versions** - Task Board version when each bug was reported

### Accessing Your Logs

You can directly see the log file inside the plugin config directory.

1. Open your vault folder in a file explorer
2. Navigate to `.obsidian/plugins/task-board/`
3. Open `task-board-logs.log` in a text editor

But will recommend to instead export your logs in the method explained in the next section.

### Exporting Logs

To export your bug logs for sharing:

1. Go to **Task Board Settings** → [General settings tab](/docs/Settings/General.md)
2. Find [Export Logs setting](/docs/Settings/General.md#export-logs) and click on the **Export** button for this setting.
3. Choose a location to save the file:
   - **Desktop** - File picker opens to select folder
   - **Web** - Browser's default download folder
4. File is saved as `task-board-logs.txt`

You can then email this exported file to the developer or attach it to a GitHub issue for additional context.

### Log File Cleanup

- Only the **last 20 bug reports** are kept to prevent the log file from growing too large
- Older logs are automatically removed when new bugs are reported
- System information is refreshed each time a new bug is logged

## System Information Collected

The Bug Reporter captures the following to help debugging:

| Information | Purpose |
|---|---|
| Obsidian version | Identify version-specific issues |
| Operating System | Platform-dependent behavior |
| Enabled Plugins | Plugin conflicts or incompatibilities |
| Plugin Versions | Version-specific interactions |
| Task Board Version | When the bug was reported |
| Build info | Debug vs. release builds |
| Other environment data | Sandbox mode, installer type, etc. |

{: .note }
> None of this system information contains your vault content or personal files—only metadata about your Obsidian setup.

## Privacy & Data Handling

### What Is Stored

✓ Error messages and stack traces  
✓ System metadata and versions  
✓ Timestamps and bug IDs  
✓ Context about where errors occurred  

### What Is NOT Stored

✗ Your vault name or path (removed before storage)  
✗ Task content or file names  
✗ Passwords or credentials  
✗ Folder structures or file contents  

### Before Reporting

**Always review the bug report** for personal information:

1. File paths that reveal folder structure
2. Specific file names with sensitive info
3. Error messages that quote your task content
4. Any other personal/business-sensitive data

Replace these with generic placeholders (e.g., "my-vault" instead of your actual vault name).

## Deduplication Policy

### How It Works

Task Board tracks which bugs have already notified you during the current session:

- When a bug occurs, its ID is checked against a list of already-shown bugs
- If the same bug ID appears again, **no notification is shown**
- The bug is still logged to the log file for your records
- The deduplication list resets when you reload Task Board or close Obsidian

### Why This Matters

Prevents notification fatigue if:
- A bug occurs repeatedly in a loop
- You're troubleshooting and triggering the same error multiple times
- Multiple tasks trigger the same underlying issue

### Bypassing Deduplication

To see notifications for the same bug again:
1. Reload Obsidian application (close and reopen the Obsidian)
2. Now, try to replicate the issue again.

## Troubleshooting

**"Bug Reporter modal won't open"**
- Try reloading the Task Board view
- Close and reopen Obsidian
- Check that the plugin is properly installed

**"I can't find my log file"**
- Check `.obsidian/plugins/task-board/task-board-logs.log`
- Make sure you're showing hidden folders (.obsidian is hidden)
- Try exporting logs instead—they'll save to a visible location

**"Same bug notification keeps appearing"**
- Reload Task Board or restart Obsidian to reset deduplication
- Or dismiss the notification each time

**"Log file is too large"**
- Export and backup the file first
- Only the last 20 bugs are kept, so the file shouldn't grow indefinitely
- Consider deleting the old exported backup to free space

## Best Practices

1. **Report early** - Don't wait if you encounter a bug; report it while you remember the steps
2. **Include steps to reproduce** - This helps developers fix issues faster
3. **Add context** - When was the bug first seen? What were you doing?
4. **Screenshots help** - If you can capture the UI state when the error occurred
5. **Check GitHub first** - Your bug may already be reported; search before creating a duplicate
6. **Review for privacy** - Always scan the report for personal information before sending
