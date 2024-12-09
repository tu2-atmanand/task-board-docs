---
parent: Components
title: Types of Columns
nav_order: 2
---

# Types of Columns

There are the following 6 types of columns you can create inside a board. Based on the properties of the columns, you will see the specific [tasks item card](./Task_Item_Card.md) in these columns under the Task Board.

## Undated

This column will contain only the tasks which do not have due date set to them.

### Properties

- **Column Name :** To create this column you only need to enter the name of the column, which will be visible on the column bar. If you want to see all the tasks, which are not been scheduled yet, then you can create this column and schedule them easily.

## Dated

This column will contain all the tasks which has a due date value. You can create a combination of **Dated** type of column, but first we need to understand the properties we have to enter to create a **Dated** column as explained below.

### Properties

- **Column Name :** The name of the column which you want to see on the Column header.
- **From :** This should be a number, either negative, positive or zero. This basically will specify, a number which is mapped to a relative date. For example, 0 means its today's date, -1 means yesterday's date and 1 means tomorrow's date. So, its just a mapping of dates relative to today's date.
- **To :** Similar to the **From** value, this value will specify the end date of the range you are creating.

Using these above two values you are creating a range of dates. For example, if you want to create a **Dated** column, in which you want to see all the tasks which has a due date of today's and tomorrow's. Then the **From** value will be 0 and the **To** value will be 1, since 0 is today's date and 1 is tomorrow's date. So, you have created a range from today to tomorrow for the column.

Here is a table for you to understand how you can create a column to with a range to show the specific tasks you want:

| From | To | Range                                                                      |
|------|----|----------------------------------------------------------------------------|
| 0    | 0  | All the tasks which have today's date as due date.                         |
| 1    | 1  | All the tasks which have tomorrow's date as due date.                      |
| -1   | -1 | All the tasks which had yesterday's date as the due date. (overdue tasks)  |
| 1    | 7  | All the tasks which are scheduled for next 7 days, starting from tomorrow. |
| -1   |    | All the overdue tasks.                                                     |
| 1    |    | All the tasks scheduled for future, starting from tomorrow.                |

{: .note }
> Observe that, the **To** field for the last two column in above table has been kept empty. Empty field indicates and infinity value, which means, if you want to display all tasks starting from tomorrow going upto infinity in future, you can just leave the field empty or enter a zero, that will work as well.
>
> You might also find out that, while entering 0 in the field, it keeps the field empty, thats a normal behavior in obsidian and it will work as expected, as per the above column.

## Tagged

Also known as `namedTagged`. This column will contain all the tasks which has been tagged with the specific tag name you have added in the property of this column.

### Properties

- **Column Name :** The first property will be as usual the name of the column which you want to see on the column header.
- **Tag Name :** This is the name of the tag, which you will going to give for multiple tasks in your vault. For example, if you are giving a tag as `#bug` to many tasks, and you want to see all this tasks under one column, then this is the type of column for you. You will have to enter the value `bug` for this input field.

## Untagged

Intuitively, this column will show you all the tasks, which has not been provided by any tag. If you would like to see all the un-tagged tasks, so that you can assign them tags later, which will be much easier from the [Edit Task Window](./EditTaskWindow.md), then you can create this column.

### Properties

- **Column Name :** The only property for this type of column is the name of the column.

## Other Tags

Now, after you have understood what are **Untagged** and **Tagged** column, there might be case, where you have given a tag to many tasks and you haven't created a **Tagged** type of column for this tasks, then these tasks wont be shown on the board at all, since they also do not fall under the **Untagged** column type criteria. For all these tasks, you can create a **Other Tags** type of column, to show all this tasks under this column

### Properties

- **Column Name :** The only property for this type of column is the name of the column.

## Completed

This type of column will show you all the tasks, which has been marked as completed. So, you will notice that, all the task item card under this column will have a different fields inside their Footer. Since you have marked the task as complete, you will see the time-date value when you marked this task as complete as can be seen from the below image.

![CompletedtaskUnderCompletedColumn](../../assets/CompletedtaskUnderCompletedColumn.png)

### Properties

- **Column Name :** The first property will be as usual the name of the column which you want to see on the column header.
- **Max Items :** This is a number value you want to enter to set a limit to the number of task item cards you want to see under this column. This has been kept to limit the number of tasks rendered under this column, because over a time, you might complete lot of tasks, and if you haven't deleted these tasks from you vault, then they will be getting appended under this column and will increase the load time of the board, hence setting a limit will help you to show only the latest completed tasks.

# Upcoming New Column types

## Priority

Coming Soon...

## Week Column

Coming Soon...
