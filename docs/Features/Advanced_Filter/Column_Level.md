---
parent: Advanced Filter
title: Column Level
nav_order: 4
---

# Column level advanced filter

Now that you have the complete understanding of how Advanced filter works from the [overview page](/docs/Features/Advanced_Filter/Overview.md). In this page, lets understand the various use-cases of applying the Advanced filter at view-level.

You have understood why we will use Board-level advanced filter. And you have understood why we will use view-level advanced filter. But, the reason why we will use the advanced filter for Kanban columns individually is a little different.

Kanban columns are used to see related tasks in a form of row as per the Kanban methodology. And the condition which decides which all tasks should be shown inside a particular column can be understood from the following page : [Type of kanban columns](/docs/Features/Type_of_Columns/Overview.md).

For a column, you cannot use an Advanced filter to organize your tasks, because columns are created using their specific configuration and for the specific workflow. 

For example, inside a Tag based workflow, you will usually have a columns of type [Tagged](/docs/Features/Type_of_Columns/Tagged.md). This column will show only the tasks which has a particular tag on them out of the task filtered by view-level advanced filter (if applied any).

So, on this column, if you apply a filter, that will hide some of the tasks from the entire view and you might not see those tasks in other columns and they will go unnoticed. Similarly, any newly added tasks which might not satisfy the applied advanced filter will be also hidden within the column. And the biggest issue here will be, [drag and drop feature](/docs/Features/Drag_Drop_Tasks.md) might not work as you expect it to work.


Hence, even though we have provided the Advanced filter at individual column level. Only use it in special cases where you temporarily want to see certain tasks from that column. An indicator will be shown in the column header, if an advanced filter is active for that column.

But use it carefully at column-level.


## How to apply column-level advanced filter ?

To access the advanced filter for a particular column, you can click on the "more options" button inside the columns header which will open a menu. Inside the menu you will find an option called "Configure column filtering". This will open the [Advanced filter menu](/docs/Components/Advanced_Filter_Menu_v2.md) for that specific column.