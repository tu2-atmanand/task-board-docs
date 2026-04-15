---
parent: Types of Columns
title: Dated
nav_order: 3
---

# Dated

This column will contain all the tasks which has a due date value. You can create a combination of **Dated** type of column, but first we need to understand the properties we have to enter to create a **Dated** column as explained below.

## Properties

### **Column Name** 

The name of the column which you want to see on the Column header.

To filter tasks based on their specific date, you need to enter **two values** to set the date range:  

### **From**
The starting number of days from today of this range.

### **To** 
The ending number of days from today of this range.

{: .note }
> Remember, this values of **From** or **To** are relative-dynamic dates. Which means, today is the reference point, which is set to 0. So if you want to go in future you have to keep adding one. And if you want to go in past, keep subtracting one.

### **Date type**
The type of the date, similar to the [universal date](/docs/8_Settings/8_Formats.md#universal-date). When you will create fresh new column, the date which you have set inside the universal date setting will be applied here, which you can easily change. This specific date property which you going to select here, should be present on the task for it to appear inside this column.

### **Work limit**

This is a part of the modern Kanban methodology which helps you to limit the amount of tasks you should do parallely. For example, if your current column is filtering all the tasks which you have scheduled to do for today, and you have set the work limit for this column as 3. Then, if there are 4 or more [task item cards](/docs/7_Components/2_Task_Item_Card.md), in this column, the column will show a small warning sign to help you manage your workload efficiently.


## **Key Rule**

- If a task's **due date falls within** the selected range of days, it will be displayed.
- **No "infinity" concept** anymore. Instead, if you want to see **all future** or **all overdue** tasks, just enter a **large number** in the range.

##### **How to Set Your Date Range**

|**Goal**|**From**|**To**|**Explanation**|
|---|---|---|---|
|See **only today's** tasks|0|0|Tasks due **today** only.|
|See **yesterday's** tasks|-1|-1|Tasks due **1 day ago**.|
|See **tomorrow's** tasks|1|1|Tasks due **1 day ahead**.|
|See **next 7 days**|1|7|Tasks due from **tomorrow to the next 7 days**.|
|See **past 7 days** (overdue)|-7|-1|Tasks due **in the last 7 days but not today**.|
|See **all future tasks**|1|300|Tasks due **from tomorrow up to 300 days ahead**.|
|See **all overdue tasks**|-300|-1|Tasks due **in the last 300 days but not today**.|
|See **all tasks (past & future)**|-300|300|Tasks from **past 300 days to the next 300 days**.|


## **Examples**

**Example 1: Filtering Today's Tasks**

📌 **You enter:**

- **From = 0**
- **To = 0**

✅ **Shows tasks due today only.**


**Example 2: Filtering Tasks Due in the Next 3 Days**

📌 **You enter:**

- **From = 1**
- **To = 3**

✅ **Shows tasks due tomorrow, day after tomorrow, and 3 days from now.**


**Example 3: Filtering All Overdue Tasks**

📌 **You enter:**

- **From = -300**
- **To = -1**

✅ **Shows tasks that were due in the past 300 days (excluding today).**


**Example 4: Filtering All Future Tasks**

📌 **You enter:**

- **From = 1**
- **To = 300**

✅ **Shows tasks that are due from tomorrow onwards, up to 300 days ahead.**