---
parent: UI Components
title: Metadata Formats
nav_order: 5
---

# Metadata

Metadata also known as task properties are the different properties you assign to your tasks for better management, filtering and giving more information to your tasks.

**Task board supports following Metadata :**  

- ID
- Status  
- Priority  
- Tags  
- Start time and End time
- Reminder
- Start date-time
- Scheduled date-time
- Due date-time
- Completion date-time
- Cancelled date-time
- Depends on

More properties coming soon...  

---

## **ID**  
{: .d-inline-block }
(v1.7.0)
{: .label .label-green }

IDs are very important part of any data-object you want to store efficiently. Hence, Task Board has adopted the mechanism to assign a unique incremental numeric ID to each task, so its very easy to refer as well as precisely find them inside huge note content. Similarly, IDs can be assigned to task-note in its frontmatter for easier fetching the task from the cache.

Its highly recommended to make use of this feature to assign IDs to your task. Please enable the "Auto add unique ID" setting, so this plugin can automatically assign IDs to your tasks.

IDs are very important for the following features to work properly : 
- Map view.
- Manual sorting in columns.

---

## **Status**  
{: .d-inline-block }
(v1.3.0)
{: .label .label-green }

The **status** of a task indicates its current state. It helps in tracking progress and managing workload efficiently.  

✅ Examples :  
- **TODO [ ]** → Task is yet to be started.
- **Ready to start [<]** → Independent tasks which can be started anytime.
- **In Progress [/]** → Task is currently being worked on.
- **In Review [?]** → Tasks which has been completed, but yet to be tested (useful in development projects workflow).
- **Completed [x] or [X]** → Task has been finished.  
- **Cancelled [-]** → Tasks which are no longer important and will not be worked on.

These are only few examples which will be available for you in the fresh install of this plugin. Later you can configure as many statuses as you want along with creating a status cycles to build a strong tasks/projects management workflow.

---

## **Due Date**  
The **due date** specifies the deadline for completing a task. It helps in prioritizing tasks based on urgency.  

✅ How it works:  
- Tasks **due today** will be highlighted for immediate action.  
- Overdue tasks (past due dates) will be marked accordingly.  
- Future due dates help in planning upcoming work.  

**Example:**  
If today is **March 5, 2025**, and a task has a due date of **March 10, 2025**, then it is due in 5 days.  

---

## **Time Duration**  
The **time duration** represents the estimated or actual time needed to complete a task. This helps in better scheduling and workload management.  

✅ Possible uses:  
- Helps in estimating how long a task might take.  
- Can be used to compare estimated vs. actual time spent on a task.  

**Example:**  
A task may have a **duration of 2 hours**, meaning it is expected to take around 2 hours to complete.  

---

## **Priority**  
The **priority** level defines how important and urgent a task is. This helps in deciding which tasks should be completed first.  

✅ Priority Levels:  
- **High** → Critical tasks that need immediate attention.  
- **Medium** → Important but not urgent tasks.  
- **Low** → Tasks that can be done later.  

**Example:**  
A deadline-related task may have a **High priority**, while an optional research task may have a **Low priority**.  

---

## **Tags**  
Tags are labels that help categorize and organize tasks. Multiple tags can be added to a task for better filtering and searching.  

✅ Uses of tags:  
- Helps in grouping related tasks together.  
- Makes searching and filtering tasks easier.  

**Example:**  
A task with the tags **#work** and **#meeting** can be found when searching for either "work" or "meeting" related tasks.  

---

## **Completion Time-Date**  
This field records the **exact date and time** when a task was completed. It helps in tracking productivity and reviewing past work.  

✅ Benefits:  
- Provides insights into when tasks were finished.  
- Helps in calculating task completion rates over time.  

**Example:**  
A task marked as completed on **March 4, 2025, at 2:30 PM** means it was finished at that exact time.  

---

# Metadata Format

Task Board supports different types of formats to add the metadata to your tasks.

## Compatible Plugin Format

You can choose one of the following options in the Task Board setting to keep the format of metadata globalized throughout your vault. You can see the supported format and the corresponding plugin option from below table :

| Plugin/Setting option | Priority             | Time duration                            | Created date           | Start date           | Scheduled date           | Due date           | Completion time-date               |
| --------------------- | -------------------- | ---------------------------------------- | ---------------------- | -------------------- | ------------------------ | ------------------ | ---------------------------------- |
| Task Board (Default)  | ⏫                    | ⏰[21:10 - 23:10]                         | ➕2024-10-31            | 🛫2024-10-31         | ⏳2024-10-31              | 📅2024-10-31       | ✅2021-10-31T21:52:22               |
| Tasks                 | ⏫                    | ⏰ 21:10 - 23:10                          | ➕ 2024-10-31           | 🛫 2024-10-31        | ⏳ 2024-10-31             | 📅 2024-10-31      | ✅ 2021-10-29                       |
| Dataview              | [priority:: highest] | [time:: 21:10 - 23:10]                   | [created:: 2024-10-31] | [start:: 2024-10-31] | [scheduled:: 2024-10-31] | [due:: 2024-10-31] | [completion:: 2021-10-31T21:52:22] |
| Obsidian Native       | Any                  | @time(21:10 - 23:10)                     | @created(2024-10-31)   | @start(2024-10-31)   | @scheduled(2024-10-31)   | @due(2024-10-31)   | @completion(2021-10-29)            |
| Day Planner           | Any                  | 09:00 - 10:00 (At the start of the task) | Any                    | Any                  | Any                      | Any                | Any                                |


- You also have the option to mix these formats with one another. For example, say you dont like to see the emojis for priority, you can use other format, and that will still work and Task Board will still scan them. But, if you are using the edit task modal of this plugin to edit the task, then the content will be sanitized to follow only one kind of format throughout, based on the format you have selected in the settings.
- **Any** mean, for this field, you can use any type of format from that column, for the specific plugin/setting option you have selected.
