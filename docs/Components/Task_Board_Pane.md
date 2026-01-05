---
parent: UI Components
title: Task Board Pane
nav_order: 1
---

# Task Board Pane

This is the complete View which you will see when you will open Task Board in a new tab or in a new window.

The View consists of various sections as can be seen in the below image :

![Task Board UI Legend](../../assets//TaskBoardUIBreakLegend.png)

## View Header Section

This is the panel of any normal view. In this Bar you will able to see the current name of the active pane, which is the Task Board. 

### Header Features

On the right side of the header, you will find several important buttons:

- **Search Button** (Added in v1.6.0): Click the search icon to open a search bar and quickly find tasks by their content. The cursor automatically focuses in the search input field for quick access.

- **View Switcher** (Added in v1.6.0): A dropdown menu that allows you to switch between different view modes or board layouts.

- **Scan Vault Button**: Opens the [Scan Vault Window](../Features/Scan_Vault_Feature.md) to rescan your vault for tasks. A new command (v1.3.0) also provides quick access to this feature.

- **Add Task Button**: Opens the Add New Task modal to create a new task. You can add tasks to the active file or choose a specific file using the file suggester (enhanced in v1.5.0).

- **More Options Button**: Access additional options and settings for the Task Board view.

### Board Progress Bar (Added in v1.6.0)

The header also displays a progress bar showing task completion statistics:
- Total number of tasks in the board
- Number of completed tasks
- Visual progress indicator
- Auto-hides on small screens for a cleaner look (v1.6.11)

## Boards Tab Section

In this section you will able to see the Tab buttons with the name of the board on them. If you have created multiple boards, there will be multiple tabs in horizontal direction. Clicking on any one, will open that specific board in the Active Board section.

**New in v1.6.0:** You can now re-order boards in the Board Configuration modal. This allows you to organize your boards by priority or move your default board to the top.

On the right side of this section there are two button :

- **Configure Board :** This button will open the [Configure Board Window](../How_To/HowToUseBoardSettings.md), to change the settings of the currently active board. You can also able to see the settings of other boards in the same window as well as a tab for [Global Settings](../How_To/HowToUseGlobalSettings.md).

- **Refresh Board :** This button helps you to refresh the board with the latest data or to solve any UI anomaly you might see for few Task Items. In normal usage you might not to use this button. This button is very useful when the [Real-Time Scanning](../How_To/HowToUseGlobalSettings.md#real-time-scanning) option is **OFF** and you are doing the [manual scanning](../Features/Auto_Scanning_Files.md#manual-scanning).

## Active Board Section

In this section you will be able to see all your columns of the board in order, the way you organized them in the Board Configuration. In side the Columns you will be able to see all your tasks as a [Task Item Card](./Task_Item_Card.md) as applicable. The tasks will be placed in the respective columns based on the [column criteria](./Types_Of_Columns.md).

### Column Features

**Column Header** (Enhanced in v1.6.0):
- Displays the column name
- Shows task count for each column
- Allows drag-and-drop to reorder columns

**Auto-hide Empty Columns** (Added in v1.5.0): Columns with no tasks can be automatically hidden based on your settings, providing a cleaner board view.

**Performance Optimizations** (v1.2.0 and later): Significant UI rendering optimizations have been implemented to improve board performance, especially for boards with many tasks.
