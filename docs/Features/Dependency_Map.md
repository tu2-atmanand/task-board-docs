---
parent: Features
title: Dependency Map
nav_order: 16
---

# Dependency Map
{: .d-inline-block }
v1.8.0
{: .label .label-purple }

Also known as **Map View**, the Dependency Map feature provides a visual canvas-based representation of your tasks and their dependencies. It allows you to see the flow of work, identify bottlenecks, and manage complex sequential projects with a visual approach.

{: .warning }
> Few months ago, in one [GitHub ticket discussion](https://github.com/tu2-atmanand/Task-Board/issues/561), a serious issue has been found related to this feature.
> Basically, right now this feature store its map view data inside a `localStorage`. This is a very bad architecture to store such kind of important data. Hence will recommend to not make use of this for your important projects. The only issue you might encounter is the cards positions and sizes might revert back to default if something wrong happens to the `localStorage`, other than this there is no problem with this feature.
>
> But will recommend to use this feature cautiously until we will implement [the fix in version `2.0.0`](https://github.com/tu2-atmanand/Task-Board/milestone/13).


## Overview

This powerful visualization tool is based on the [**Dependency Flow Planning (DFP) Methodology**](/docs/Articles/Dependency_Flow_Planning-DFP.md), a revolutionary approach to project management that emphasizes child-to-parent task flows and strict dependencies. Specially useful for sequential projects.

With the Map View, you can:
- Visualize task dependencies as a flowchart on a digital canvas
- See how tasks connect and flow from one to another
- Identify project bottlenecks and workflow hurdles
- Organize and plan sequential projects more efficiently
- Track project progress visually in real-time


Besides this, how this feature helps the most in this plugin is through its live canvas functionality. Where, if you make any changes to the tasks from your vault, since Task Board will automatically scan those changes, this map view will be always be on its latest content, providing a live updates of your changes and maintaining a true source of your latest task status. If users are using Obsidian in an live environment for a team project, then this map view will provide a single source of truth of your project status.


## What is the Dependency Map?

The Dependency Map is a visual representation of how tasks relate to and depend on each other. Instead of viewing tasks in a traditional list format, the map view presents them as interconnected nodes on a canvas, allowing you to see:

- **Task Relationships**: How different tasks connect and depend on one another
- **Workflow Flow**: The logical sequence and flow of work through your project
- **Dependencies**: Clear visualization of which tasks block or enable other tasks
- **Project Structure**: The overall architecture and hierarchy of your project

This canvas-based approach is particularly effective for:
- Sequential project management
- Complex workflow planning
- Team collaboration and communication
- Live tracking and monitoring of project progress


## How to Use the Map View Feature

### Step 1: Enable Auto ID Assignment
> This is optional but **highly recommended**.

For the best experience, enable automatic ID assignment:

1. Open **Task Board Settings**
2. Navigate to the **General** tab
3. Enable **"Auto add unique id"**
4. This will automatically apply incremental numeric IDs to tasks as you interact with them

{: .note }
> Although this feature will work without this setting being enabled, but please note that, for any task to show up on the map view canvas, the task must have an ID property on it, to uniquely identify this task among all the other tasks from your vault.


**Why IDs are Important:**
- IDs are essential for identifying tasks on the canvas
- Task Board maps task positions and sizes to localStorage using the ID for persistent state management
- IDs enable smooth and consistent visual experience across sessions

### Step 2: Add Tasks to the Map

To add a task to the Map View you have basically three options. The first two options are automatic:

#### Option A: Using the Edit Task Modal

1. Open the [task editor](/docs/Features/Task_Editor.md) for any task.
2. Look for the **"Show on Map"** button.
3. Click the button
4. The system will automatically:
   - Apply an ID to the task (if it doesn't have one)
   - Display the task as a node on the Map View canvas

#### Option B: Manual ID Assignment

1. Open the map view using the view switcher drop-down available at the top-right corner in the Task Board tab.
2. Then you will notice a small button at the bottom-left corner as shown in the below image : 

3. This will open a small side-panel overlay where all your tasks which do not have ID property on them will be listed. You can also search for the task using the search bar. Then simply click on the task and it will be imported on the map. Please note, drag and dropping the card through this panel wont work.
4. Close this panel by either clicking outside the panel or using the close button. And you should see all your tasks which you imported arrange in a column like fashion at a certain location on the map, this will be usually at the (0,0) coordinates of the canvas.


#### Option C: Manual ID Assignment

1. Add an ID property to your task (format: `🆔 4` or similar)
2. Navigate to the Map View
3. The task will automatically appear on the canvas

### Step 3: Interact with the Canvas

Once tasks are on the Map View, you can:
- **Drag Tasks**: Move task nodes to organize your workflow
- **View Dependencies**: See connections between related tasks
- **Zoom & Pan**: Navigate the canvas to see your entire project
- **Edit Tasks**: Click on nodes to edit task details
- **Manage Layout**: Arrange tasks to reflect your project flow


## Best Practices

1. **Enable Auto ID Assignment**: Makes it easier to work with tasks on the map
2. **Use Meaningful IDs**: Choose ID schemes that make sense for your project. Will recommend to go with the default IDs added by this project, which are numeric incremental numbers, which also helps you to track the number of tasks you created through this plugin
3. **Organize Logically**: Arrange tasks on the canvas to reflect workflow
4. **Leverage Dependencies**: Use task dependencies to show relationships
5. **Regular Reviews**: Periodically review your map to ensure it reflects your current project state
6. **Team Collaboration**: Share your map view with team members for better communication

## Future Enhancements

The Map View feature is under active development. Future versions may include:

- Support for tasks without explicit IDs
- Enhanced visualization options
- Performance optimizations
- Additional interaction capabilities
- Integration with more metadata types

Stay tuned for updates and improvements!

## Link to Related Topics

- [Article on Dependency Flow Planning Methodology](/docs/Articles/Dependency_Flow_Planning-DFP.md)
- [Article on Dependency Flow Planning Methodology (DFP) X Kanban Methodology](/docs/Articles/DFP_and_Kanban_Methodology.md)