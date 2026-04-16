---
parent: Features
title: Task properties
nav_order: 2
---

# Task properties

**Task Metadata** also known as task properties are the different properties you assign to your tasks for better management, filtering and giving more information to your tasks.

**Task board supports following Metadata by default :**  

- ID
- Status  
- Priority  
- Tags  
- Time duration
- Created date
- Start date
- Scheduled date
- Due date
- Reminder
- Completion date-time
- Cancelled date-time
- Depends on

More properties coming soon...  

Below section will explain each of the default supported properties by Task Board. To understand how they will appear inside your notes when you add these properties to your inline-tasks please refer the following wiki : [Task properties format for inline-tasks](/docs/Features/Task_Formats/Inline_Task.md#task-metadata).

---

## **ID**  
{: .d-inline-block }
(v1.7.0)
{: .label .label-green }

IDs are very important part of any data-object you want to store efficiently. Hence, Task Board has adopted the mechanism to assign a unique incremental numeric ID to each task, so its very easy to refer as well as precisely find them inside huge note content. Similarly, IDs can be assigned to task-note in its frontmatter for easier fetching the task from the cache.

Its highly recommended to make use of this feature to assign IDs to your task. Please enable the "Auto add unique ID" setting, so this plugin can automatically assign IDs to your tasks.

IDs are very important for the following features to work properly : 
- [Map view](/docs/Features/Dependency_Map.md)
- Manual sorting in columns

---

## **Status**  
{: .d-inline-block }
(v1.3.0)
{: .label .label-green }

The **status** of a task indicates its current state. It helps in tracking progress and managing workload efficiently.

### Examples :  
- **TODO [ ]** → Task is yet to be started.
- **Ready to start [<]** → Independent tasks which can be started anytime.
- **In Progress [/]** → Task is currently being worked on.
- **In Review [?]** → Tasks which has been completed, but yet to be tested (useful in development projects workflow).
- **Completed [x] or [X]** → Task has been finished.  
- **Cancelled [-]** → Tasks which are no longer important and will not be worked on.

These are only few examples which will be available for you in the fresh install of this plugin. Later, with multiple task statuses and configuring them to cycle from one status to another using the [Custom statuses setting](/docs/Settings/Properties.md#custom-statuses), you can create a nice automation workflow board.

---

## **Priority**  
The **priority** level defines how important and urgent a task is. This helps in deciding which tasks should be completed first.  

### Priority Levels:  
- **Highest** → Critical tasks that need immediate attention. 
- **High** → Important but not urgent tasks.
- **Medium** → A normal priority task, neither important nor a task to be ignored.  
- **Low** → Tasks which can be ignored if there are higher priority tasks on the plate.  
- **Lowest** → Tasks that can be done later. 

**Example:**  
A deadline-related task may have a **High priority**, while an optional research task may have a **Low priority**.  

---

## **Tags**  
Tags are labels that help categorize and organize tasks. Multiple tags can be added to a task for better filtering and searching.  

### Uses of tags:  
- Helps in grouping related tasks together.  
- Makes searching and filtering tasks easier.  

**Example:**  
A task with the tags **#work** and **#meeting** can be found when searching for either "work" or "meeting" related tasks.  

---

## **Time Duration**  
The **time duration** represents the estimated or actual time needed to complete a task. This helps in better scheduling and workload management.  

### Possible uses:  
- Helps in estimating how long a task might take.  
- Can be used to compare estimated vs. actual time spent on a task.  

**Example:**  
A task may have a **duration of 2 hours**, meaning it is expected to take around 2 hours to complete.  

---

## **Created Date**

This date can help you to understand when and what time the particular task was created. This property will be specially useful, if you want to sort your tasks based on the time they were created.

{: .note }
> At present, only date value is allowed for this task property. In future, we will be able to extend this property to have date-time value


---

## **Start Date**

The **start date** specifies the time when you are supposed to start working on the particular task. It help in balancing your time-workload bandwidth so you can simultaneously work on other tasks as well.

This might be useful for a particular kind of tasks which extends over days. For other tasks, you can use the scheduled date.

### How it works:  
- Tasks which are required to be **started today** can be filtered inside a custom column.  
- As well as, if you have added start time property to your tasks, then you can also sort the tasks which you are supposed to start today.

---

## **Scheduled Date**

There will be a little confusion between start date property and this scheduled date property. For most of the workflows and tasks, you can basically use both these date properties synonymously.

### How it works: 

A small difference would be, you can say, you want a specific task to be done at the specific point in time. For example, lets say we have the below two tasks : 
```md
- [ ] Discuss the gravitational waves during the group meeting.
- [ ] Create a draft for the gravitation waves research paper.
```

The first task, should be done when your group meeting will going to start. Which means, if you have added a reminder to this task, then the reminder should go off only on that specific day. But, the second task will going to take few days to complete, hence, you should better assign a start date to this task and possibly give a due date, by when you should finish completing the draft of the research paper.

---

## **Due Date**  
The **due date** specifies the deadline for completing a task. It helps in prioritizing tasks based on urgency.  

### How it works:  
- Tasks **due today** will be highlighted for immediate action.  
- Overdue tasks (past due dates) will be marked accordingly.  
- Future due dates help in planning upcoming work.  

**Example:**  
If today is **March 5, 2025**, and a task has a due date of **March 10, 2025**, then it is due in 5 days.  

---

## **Completion Date-time**  

This field records the **exact date and time** when a task was completed. It helps in tracking productivity and reviewing past work.  

### Benefits:  
- Provides insights into when tasks were finished.  
- Helps in calculating task completion rates over time.  

**Example:**  
A task marked as completed on **March 4, 2025, at 2:30 PM** means it was finished at that exact time.  

---

## **Cancelled Date-time**

Similar to the completion date property, this property records the **exact date and time** when a task was marked as cancelled. It will help you to get this extra information on what specific time you marked the task as cancelled. Might not be that useful with just the property for now, but will be very useful, once the [task activity tracking feature](/docs/Features/Task_Activity_Tracking.md) has been enabled. 

### Benefits:  
- Provides insights into when you decided not to work on the task any further.  
- Helps in calculating task cancellation rates over time.  

---

## **Depends on**

This is a very special property which is added by the task dependency feature. This feature basically allows you to set dependencies to your current task. Also known as **blocked-by** property.

For example, consider the following three inline-tasks in a single note or in different notes : 
```md
- [ ] Boil the rice. 🆔111
- [ ] Cook the chicken as per the flavour. 🆔112
- [ ] Add chicken inside the rice. 🆔113 ⛔111, 112
```

Here you may see, the first two tasks should be completed first to start working on the third task. You possibly cannot start the third task until the first two tasks has been finished. Hence, we have added the first two tasks as the dependencies for the third task. So, you are saying the third task is **dependent on** the first two tasks.

### Time-Based Dependencies

Task dependencies in project management are primarily categorized into **four time-based relationships** that dictate the sequence of work: **Finish-to-Start (FS)**, **Start-to-Start (SS)**, **Finish-to-Finish (FF)**, and **Start-to-Finish (SF)**. 

These relationships define how the start or finish dates of one task (the successor) rely on another (the predecessor):

|Dependency Type|Definition|Common Example|
|---|---|---|
|**Finish-to-Start (FS)**|Task B cannot start until Task A is completed.|Development must finish before QA testing begins.|
|**Start-to-Start (SS)**|Task B cannot start until Task A starts.|Testing begins once development starts.|
|**Finish-to-Finish (FF)**|Task B cannot finish until Task A is completed.|Final documentation completes when development completes.|
|**Start-to-Finish (SF)**|Task B cannot finish until Task A starts.|Night shift cannot end until the day shift starts.|

Most projects primarily utilize **Finish-to-Start** relationships as the default for sequential workflows, while **Start-to-Start** and **Finish-to-Finish** are often used for parallel work-streams or tasks that must conclude simultaneously.

You might want to check out the [Dependency Flow Planning (DFP) methodology](/docs/Articles/Dependency_Flow_Planning-DFP.md) which utilizes the **Finish-to-Start** approach. And the [map view feature](/docs/Features/Dependency_Map.md) has implemented the same in this plugin.

---

## **Custom properties**

{: .new-title }
> Announcement
> 
> In future, you will be able to add your custom properties to your tasks. Following is the ticket for this feature : [tu2-atmanand/task-board#688](https://github.com/tu2-atmanand/Task-Board/issues/688).
>
> As well as, using this new feature, you should be able to decide whether you want date value or date-time value to each of your date related task properties.