---
title: Vision
nav_order: 9
---

# Vision and Roadmap

Before diving into the vision of **Task Board**, let me first share my thoughts on task management within Obsidian.  

The two primary methodologies guiding the development of this plugin are:  

1. **Kanban Methodology** (with a unique twist)  
2. **GitHub Project Planning**  

## 1. Kanban Methodology  

Kanban methodology is a popular approach for task management. It involves organizing tasks as cards and arranging them into columns to represent certain shared properties. These columns could signify aspects such as project stages, due dates, priorities, or phases of a development cycle.  

You can prioritize tasks by their position within a column and use colors to represent specific attributes (e.g., tasks related to particular areas). Once organized on the Kanban board, your workflow becomes streamlined and visually easy to manage.  

### Challenges I Faced with Existing Plugins  

While Kanban methodology is great in theory, I encountered some limitations with existing plugins that disrupted my workflow:  

1. **Limited Task Descriptions**  
   - I often like to use short task titles, but many tasks require additional details, such as explanations, images, or links to other documents.  
   - While it’s possible to include these details within the card, it results in overly lengthy cards. Even with folding sections, the cards don’t look polished and require extra manual adjustments, distracting me from focusing on my workflow.  

2. **Editing Experience**  
   - Although the built-in editor in the Kanban plugin is excellent, it doesn’t provide the seamless experience of Obsidian’s live editor.  

3. **Lack of Automation**  
   - Kanban methodology is inherently static, meaning the user manually moves cards and updates their properties.  
   - While this works for simple projects, in complex and large-scale projects, dynamic workflows with automation become essential.  
   - This lack of automation is a significant limitation, and it’s where **GitHub Project Planning** shines.  

### Learning Resources  

To better understand Kanban methodology, I referred to this resource: [Kanban Methodology by Geeks for Geeks](https://www.geeksforgeeks.org/kanban-agile-methodology/).  

## 2. GitHub Project Planning  

GitHub Project Planning offers a more advanced and dynamic approach to task management. This is actually the same interface you will see when you visit the [Task Board GitHub Project Planing Kanban Board](https://github.com/users/tu2-atmanand/projects/2/views/1).  

### Key Features That Inspired Me  

1. **Improved Kanban Implementation**  
   - The basic Kanban principles are implemented exceptionally well, with a polished and intuitive user interface.  
   - The card design, in particular, inspired the design for Task Board cards.  

2. **Interactive Pop-Up Editor**  
   - Clicking on a card title opens a sleek pop-up where you can:  
     - Edit every task property effortlessly with just a few clicks.  
     - Maintain separate input fields for the task title and task description.  
     - Add comments, which are automatically timestamped.  
     - Track every change to the task, such as updates to tags or due dates. This is the power of journalizing your work while you were working in that specific task.

   - What’s even more exciting is the idea of integrating **Obsidian’s live editor** into this window. This would eliminate the need to switch between editor and preview modes, streamlining the workflow significantly.  

3. **Automation Through Workflows**  
   - GitHub Projects introduces workflows, which allow you to automate task management. For example:  
     - Automatically change a task's tag if it becomes overdue.  
     - Set predefined rules to streamline your project.  

   - While this might not appeal to every user, I find it transformative for managing complex projects. The possibilities for automation are endless and can significantly enhance productivity.  

### Filling the Gaps  

Existing plugins and even the Kanban methodology itself lack automation. This is where **Task Board** steps in, combining the visual organization of Kanban with the power of GitHub Project Planning to deliver a dynamic, automated task management experience.  

## Balancing Features and Performance  

Integrating these features into Task Board won’t make the plugin overly bloated. However, to ensure performance and cater to varying user preferences, I will:  

- Build all features as **optional** so users can enable or disable them as needed.  
- Focus on maintaining a lightweight and efficient plugin for all Obsidian users.  

## Use Case of This Workflow  

Let’s consider a scenario where I am working on three different projects or tasks—let’s call them **A**, **B**, and **C**.  

### The Challenge  

While working on **A**, I might realize that I need to find a better solution before proceeding further with its development or research. This leads me to start working on an alternate approach or improvement, which we can think of as a "sub-task" or "branch"—let’s call it **A-1**.  

Now, while **A-1** is being developed or researched, I don’t want my progress on the main task **A** to come to a halt. Instead, I want to continue advancing **A** while keeping track of the work being done on **A-1**.  

At the same time, similar situations might arise with the other tasks, **B** and **C**. For example:  

- While working on **B**, I may identify a need for additional sub-tasks like **B-1** or **B-2**.  
- For **C**, the same workflow might apply, creating branches like **C-1**.  

Even though these tasks (**A**, **B**, and **C**) are separate and independent, I often find **connections or dependencies** between them. For instance, while working on **A**, I might discover a useful link or insight that relates to **C**. This could lead to creating a new combined branch, or some form of cross-referencing between the two tasks.  

### The Desired Workflow  

The key requirement in this scenario is **seamless multitasking and tracking**:  

1. While I am actively working on **A**, I might need to create a new branch (**A-1**) for a specific sub-task or exploration.  
2. Even after creating **A-1**, my work on the main branch (**A**) should not stop or be interrupted.  
3. Simultaneously, I must keep recording my progress on **A-1** to ensure that all details are documented and organized.  

This approach allows me to handle complexity without losing track of my tasks, sub-tasks, or their interconnections.  

---

### The Vision  

This use case is the **foundation** I aim to build with this new plugin. It is designed to support dynamic workflows where:  

- Tasks can evolve into sub-tasks without interrupting the main workflow.  
- Progress across multiple tasks and their branches can be recorded efficiently.  
- Connections between tasks can be identified and managed seamlessly.  

With this workflow, I hope to enable users to tackle complex, multi-dimensional projects with greater flexibility and clarity.  
