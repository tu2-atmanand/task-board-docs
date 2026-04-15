---
parent: Types of Columns
title: All Pending Tasks
nav_order: 10
---

# All Pending Tasks


This a special type of column, specially introduced after the requests of users to show all the pending tasks inside the column and then user can apply the [Advanced Column Filter](/docs/6_Features/7_Advanced_Column_Filter.md) to create a custom filtered view. 

There are few cases which are not possible through the already existing column types above, for such cases, we have this column type to filter the tasks based on the Advanced Column Filters, based on users choice.

## Properties

### **Column Name** 

The name of the column which you want to see on the column header.

### **Work limit**

This is a part of the modern Kanban methodology which helps you to limit the amount of tasks you should do parallely. For example, if your current column is filtering all the tasks which you have scheduled to do for today, and you have set the work limit for this column as 3. Then, if there are 4 or more [task item cards](/docs/7_Components/2_Task_Item_Card.md), in this column, the column will show a small warning sign to help you manage your workload efficiently.