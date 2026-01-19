---
parent: How To
title: Use APIs
nav_order: 8
---

# Task Board APIs

## Overview

Task Board exposes a public API that allows other Obsidian plugins to integrate with Task Board functionality. This API enables external plugins to programmatically create and manage tasks without directly modifying markdown files.

## Getting the API

To use the Task Board API in your plugin, you need to access it through the Obsidian app's plugin registry:

```typescript
// In your plugin's onload method or in your scripts
const taskBoardPlugin = this.app.plugins.plugins["task-board"];
const taskBoardApi = taskBoardPlugin?.taskBoardApi;

if (!taskBoardApi) {
  console.error("Task Board plugin not found or API not available");
  return;
}

// Now you can use the API
const taskContent = await taskBoardApi.addNewTask(false);
```

## API Methods

### `addNewTask(isTaskNote: boolean, filePath?: string): Promise<string>`

Opens a modal dialog to create a new task. The user can configure the task properties, and the method returns the formatted task content when saved.

#### Parameters

- **`isTaskNote`** (boolean, required)
  - If `true`: Opens a Task Note creation interface. Task Notes are dedicated markdown files in your vault that represent a single task. They store additional task metadata in the file's frontmatter.
  - If `false`: Opens an inline task creation interface. Inline tasks are created as task items within existing markdown files using the `- [ ] Task text` format.

- **`filePath`** (string, optional)
  - Specifies the file path where the task should be created or edited
  - For Task Notes: If provided, the task will be created/edited at this location. If omitted, the default Task Note location from plugin settings will be used.
  - For Inline tasks: If provided, the task will be added to this specific file. If omitted, the current active note will be used.
  - Path should be relative to vault root (e.g., `"path/to/file.md"`)

#### Return Value

Returns a `Promise<string>` that resolves to:

- **Formatted task content** (non-empty string): The task was successfully created and saved. The string contains the properly formatted task content ready to be written to a file.
- **Empty string** (`""`): The user cancelled the task creation without saving. No task was created.
- **Error message** (string starting with "Error"): An error occurred during task creation. The string contains details about what went wrong.

#### Examples

##### Example 1: Create a Task Note

```typescript
const taskContent = await taskBoardApi.addNewTask(true);

if (taskContent === "") {
  console.log("User cancelled the task creation");
} else if (taskContent.startsWith("Error")) {
  console.error("Failed to create task:", taskContent);
} else {
  console.log("Task created successfully!");
  console.log("Task content:", taskContent);
}
```

##### Example 2: Create an Inline Task in a Specific File

```typescript
const filePath = "Projects/MyProject/README.md";
const taskContent = await taskBoardApi.addNewTask(false, filePath);

if (taskContent) {
  // Write the task to the file
  const file = this.app.vault.getAbstractFileByPath(filePath);
  if (file instanceof TFile) {
    const currentContent = await this.app.vault.read(file);
    await this.app.vault.modify(file, currentContent + "\n" + taskContent);
  }
}
```

##### Example 3: Create a Task Note at a Specific Location

```typescript
const noteLocation = "Archive/Tasks/2025-01.md";
const taskContent = await taskBoardApi.addNewTask(true, noteLocation);

if (taskContent && taskContent !== "") {
  // Task was created at the specified location
  new Notice("Task Note created successfully!");
}
```

##### Example 4: Complete Workflow with Error Handling

```typescript
async function createTaskFromCommand() {
  const taskBoardPlugin = this.app.plugins.plugins["task-board"];
  
  if (!taskBoardPlugin?.taskBoardApi) {
    new Notice("Task Board plugin is not available");
    return;
  }

  try {
    const taskContent = await taskBoardPlugin.taskBoardApi.addNewTask(false);
    
    if (taskContent === "") {
      console.log("Task creation was cancelled by user");
      return;
    }
    
    if (taskContent.startsWith("Error")) {
      new Notice(`Failed to create task: ${taskContent}`);
      return;
    }
    
    // Successfully created, add to current file
    const activeFile = this.app.workspace.getActiveFile();
    if (activeFile) {
      const content = await this.app.vault.read(activeFile);
      await this.app.vault.modify(activeFile, content + "\n" + taskContent);
      new Notice("Task added successfully!");
    }
  } catch (error) {
    console.error("Unexpected error:", error);
    new Notice("An unexpected error occurred");
  }
}
```

## Task Content Format

When a task is successfully created, the returned string contains the formatted task content. The format depends on whether it's a Task Note or inline task:

### Inline Task Format
```
- [x] Buy groceries @today #personal
```

### Task Note Format
The task note is created as a markdown file with YAML frontmatter containing task metadata:

```markdown
---
title: Buy groceries
status: TODO
priority: Medium
tags:
  - personal
dueDate: 2025-01-20
---

Task description and content goes here.
```

## Plugin Compatibility

The Task Board API requires:
- **Obsidian Version**: 1.0.0 or later
- **Task Board Version**: 1.4.0 or later

## Error Handling

When calling the API, always handle the different return states:

```typescript
const result = await taskBoardApi.addNewTask(true);

// Check for cancellation (user closed modal without saving)
if (result === "") {
  console.log("Operation cancelled");
  return;
}

// Check for errors
if (result.startsWith("Error") || result.includes("error")) {
  console.error("Operation failed:", result);
  return;
}

// Result contains task content
console.log("Success:", result);
```

## Best Practices

1. **Always check for plugin availability**
   ```typescript
   const taskBoardApi = this.app.plugins.plugins["task-board"]?.taskBoardApi;
   if (!taskBoardApi) {
     new Notice("Task Board plugin is required");
     return;
   }
   ```

2. **Handle all return states**
   - Check for empty string (cancellation)
   - Check for error strings
   - Process valid task content

3. **Validate file paths**
   - Use relative paths from vault root
   - Use proper path separators (`/`)
   - Verify file existence before operations

4. **Provide user feedback**
   - Use `Notice` for user-facing messages
   - Log errors to console for debugging
   - Display meaningful error messages

5. **Consider performance**
   - The modal is asynchronous; wait for completion
   - Don't block the UI during task creation
   - Handle cancellation gracefully

## Troubleshooting

### "Task Board plugin not found"
- Ensure Task Board plugin is installed
- Check that Task Board is enabled in Community Plugins
- Verify the plugin ID is correct: `"task-board"`

### Empty string returned unexpectedly
- This is normal when the user cancels the modal
- Check for `result === ""` to handle cancellations

### Task content not being created
- Verify the file path is correct and writable
- Ensure the file exists (for inline tasks)
- Check browser console for detailed error messages

### Type errors in TypeScript
- Import `TFile` from `obsidian` for file operations
- Use proper Obsidian API types for vault operations
- Check that your plugin's TypeScript target is ES6 or later

## Future API Expansion

Potential future API additions may include:
- Task editing and deletion methods
- Task querying and filtering
- Bulk task operations
- Custom board creation and configuration
- Task event listeners