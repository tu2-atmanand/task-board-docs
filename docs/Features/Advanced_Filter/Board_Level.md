---
parent: Advanced Filter
title: Board Level
nav_order: 2
---

# Board level advanced filter

Now that you have the complete understanding of how Advanced filter works from the [overview page](/docs/Features/Advanced_Filter/Overview.md). In this page, lets understand the various use-cases of applying the Advanced filter at board-level.

As you know, after this plugin scans all your tasks from your whole vault, which are allowed through the [Filters for scanning](/docs/Features/Filters_for_Scanning.md), of course. The tasks are cached inside a json file.

Now, there might be tens of thousands of tasks inside your vault. Some of them might be related to a specific project or area in your life, other tasks might be simply daily chores tasks created inside your daily notes, etc.

Task Board plugin, helps you to manage multiple projects inside your same vault. Along with projects, it also encourages to organize your related tasks which might be related to a specific area in your life at a single place.

To do this, you basically create different boards for each of your projects. Now, to ensure that the specific board should only show you the specific tasks which are related to this project you will basically going to apply the Advanced Filter to your board. As simply as that!

The reason why I am saying is this because, you also have the ability to NOT apply board-level advanced filter and can directly proceed to apply [view-level advanced filter](/docs/Features/Advanced_Filter/View_Level.md). Because, incase, if you want to create a particular view inside your board, which should show you tasks which might not be related to the project, then you can apply a particular filter to the other views present inside the board, so that those views can show you only the tasks related to the particular project and for the other view, you can apply a different filter to see those un-related tasks.

But, this plugin would not recommend this to organize your work properly. But, still, there are workflows where we often find ourselves in such situations where you can make use of only the view-level filters and avoid using board-level filters.

## How to apply board-level advanced filter ?

Since, we will rarely going to change the board-level filters and mostly find ourselves changing the view-level filters. The button to configure board-level filter has been placed inside the [Board config modal](/docs/Components/Board_Config_Modal.md), under the "**Board settings**" tab.

You should find a configure button which will open the [Advanced filter menu](/docs/Components/Advanced_Filter_Menu_v2.md) in a form of modal.