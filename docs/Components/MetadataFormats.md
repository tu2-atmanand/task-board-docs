---
parent: Components
title: Metadata Formats
nav_order: 5
---

# Metadata Format

Task Board supports different types of formats to add the metadata to your tasks.

**Metadata includes :**  

- Status  
- Due date  
- Time duration  
- Priority  
- Tags  
- Completion time-date  

More properties coming soon...  

---

### **Status**  
{: .d-inline-block }

New (v1.3.0)
{: .label .label-green }

The **status** of a task indicates its current state. It helps in tracking progress and managing workload efficiently.  

✅ Possible statuses:  
- **Pending** → Task is yet to be started.  
- **In Progress** → Task is currently being worked on.  
- **Completed** → Task has been finished.  
- **Blocked** → Task cannot be completed due to some issue.  

**Example:**  
A task with "In Progress" status means it is actively being worked on, while "Blocked" means something is preventing it from completion.  

---

### **Due Date**  
The **due date** specifies the deadline for completing a task. It helps in prioritizing tasks based on urgency.  

✅ How it works:  
- Tasks **due today** will be highlighted for immediate action.  
- Overdue tasks (past due dates) will be marked accordingly.  
- Future due dates help in planning upcoming work.  

**Example:**  
If today is **March 5, 2025**, and a task has a due date of **March 10, 2025**, then it is due in 5 days.  

---

### **Time Duration**  
The **time duration** represents the estimated or actual time needed to complete a task. This helps in better scheduling and workload management.  

✅ Possible uses:  
- Helps in estimating how long a task might take.  
- Can be used to compare estimated vs. actual time spent on a task.  

**Example:**  
A task may have a **duration of 2 hours**, meaning it is expected to take around 2 hours to complete.  

---

### **Priority**  
The **priority** level defines how important and urgent a task is. This helps in deciding which tasks should be completed first.  

✅ Priority Levels:  
- **High** → Critical tasks that need immediate attention.  
- **Medium** → Important but not urgent tasks.  
- **Low** → Tasks that can be done later.  

**Example:**  
A deadline-related task may have a **High priority**, while an optional research task may have a **Low priority**.  

---

### **Tags**  
Tags are labels that help categorize and organize tasks. Multiple tags can be added to a task for better filtering and searching.  

✅ Uses of tags:  
- Helps in grouping related tasks together.  
- Makes searching and filtering tasks easier.  

**Example:**  
A task with the tags **#work** and **#meeting** can be found when searching for either "work" or "meeting" related tasks.  

---

### **Completion Time-Date**  
This field records the **exact date and time** when a task was completed. It helps in tracking productivity and reviewing past work.  

✅ Benefits:  
- Provides insights into when tasks were finished.  
- Helps in calculating task completion rates over time.  

**Example:**  
A task marked as completed on **March 4, 2025, at 2:30 PM** means it was finished at that exact time.  

---

## Compatible Plugin Format

You can choose one of the following options in the Task Board setting to keep the format of metadata globalized throughout your vault. You can see the supported format and the corresponding plugin option from below table :

| Plugin/Setting option  | Due date            | Time duration                             | Priority              | Completion time-date                |
| ---------------------- | ------------------- | ----------------------------------------- | --------------------- | ----------------------------------- |
| Task Board (Default)   | 📅[2024-10-31]      | ⏰[21:10 - 23:10]                          | ⏫                     | ✅ 2021-10-31T21:52:22               |
| Tasks                  | 📅 2024-10-31       | ⏰21:10 - 23:10                            | ⏫                     | ✅ 2021-10-29                        |
| Day Planner            | Any                 | 09:00 - 10:00 (At the start of the task)  | Any                   | Any                                 |
| Dataview               | [due:: 2024-10-31]  | Any                                       | [priority:: highest]  | [completion:: 2021-10-31T21:52:22]  |
| Obsidian Native        | @due(2024-10-31)    | Any                                       | Any                   | @completion(2021-10-29)             |

- You also have the option to mix these formats with one another. For example, say you dent like to see the emojis for priority, you can use other format, and that will still work.
- **Any** mean, for this field, you can use any type of format from that column, for the specific plugin/setting option you have selected.
