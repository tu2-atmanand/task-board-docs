---
parent: Features
title: Marking Task Complete
nav_order: 3
---

# Marking Task Complete

This although being a simple feature, it does a real-time changes to the parent markdown file.

There are basically two things happening when you click on the main checkbox of any [Task Item Card](../Components/Task_Item_Card.md).

## Task Card moves

Once you click on the main checkbox of the of any task, it will be first move from its original column to the the column of type **Completed**.

## Updating Markdown file

The second this which will happen is, the status of the checkbox will be updated inside the parent markdown file of the task. So the pattern `- [ ]` will change to `- [x]`.

{: .new-title }
> Upcoming Feature
>
> At present this functionality is very basic, but in future release this page will be updated with the upcoming features, when you will be able to change the status of the checkbox with different types of emojis.
>
> The second biggest feature will be Task Actions, when if the checkbox is clicked of a task item belonging to a specific column, it will be moved to a destination column and not the default **completed** column type.
