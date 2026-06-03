---
parent: Advanced Filter
title: View Level
nav_order: 3
---

# View level advanced filter

Now that you have the complete understanding of how Advanced filter works from the [overview page](/docs/Features/Advanced_Filter/Overview.md). In this page, lets understand the various use-cases of applying the Advanced filter at view-level.

You might have already gone through the [Board level advanced filter page](/docs/Features/Advanced_Filter/Board_Level.md). Which explains in which situations we should/shouldn't use board-level advanced filter.

You will create different kinds of views as well as multiple views of the same kind inside your board as per your requirement. 

For example, I would like to see my project tasks in two different workflows : 
- Time based workflow
- Status based workflow

This helps me to visualize the tasks based on their due dates and the progress of the whole project.

Along with this, I also like to create views, to manage a sub-project, within the whole project. There are often times, when I can break-down the whole project into multiple small projects and work on them either parallely or sequentially. And since they all are a part of the same project, they should be present inside the board.

To do this, once all my tasks related to the specific projects has been filtered through the Board level advanced filter. Now, I can pass them through another advanced filter, which I can apply for a specific view. So that, this specific view can show me only a certain tasks which are related to a small area within the project. 

This way I can create multiple views and apply view-level advanced filter to work on smaller parts of the project.

## How to apply view-level advanced filter ?

This is straight forward. As we might often find ourselves to find only specific tasks inside the particular view, incase there are a lot of tasks inside your view, you should be allowed to access the advanced filter easily, hence, the Advanced filter for views accessible using the filter icon button inside the [view header](/docs/Components/Task_Board_Pane.md#view-header-section).

And since, Advanced filter is basically a collection of [Quick filters](/docs/Components/Advanced_Filter_Menu_v2.md#quick-filter), you can easily toggle any of your quick filters ON or OFF to filter out the specific tasks faster.


## Future scope

Lets go even one step further...
What if, you want to create a view to manage sub-sub-project. That is, you have already created a view to manage a sub-part of the whole project. But there might be cases, in a complex and huge projects, where you might want to create views to manage even granular level of your projects to manage your tasks efficiently.

### Easy workaround

Since, each board is basically a `.taskboard` file stored inside your file system. You can easily create folders and then sub-folders and inside those sub-folders you can create more boards (`.taskboard` files), one board under each sub-folder. This was you can easily and with less cognitive load.

### Views management

But... We also have a feature on the roadmap which will allow you to visualize your views just like a files inside a file-explorer and you can cerate virtual folders and manage your views accordingly.

This is a little heavy workload at present and there is no timeline when this feature will be released. Hence, the first workaround will help you to achieve the requirement for now.

You can read more about the feature request and track its progress here : [task-board-github/ticket-726](https://github.com/tu2-atmanand/Task-Board/issues/726)