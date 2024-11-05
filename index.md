---
title: Home
layout: home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---

# **Task Board** plugin Documentation

## Topics

- [01 - Installation](./docs/Installation.md)
- [02 - Getting Started]({% link docs/Getting_Started.md %})
- [03 - Features]({% link docs/Features/index.md %})
- [04 - Examples]({% link docs/Examples/index.md %})
- [05 - How to do Anything]({% link docs/How_To/index.md %})
- [06 - FAQs]({% link docs/FAQs/index.md %})

## What is Task Board?

[**Task Board**](https://github.com/tu2-atmanand/Task-Board) is an Obsidian plugin to view and manage all your task in a much more efficient Kanban Board format. Easily manage your tasks throughout your vault.

![Task Board Thumbnail](./assets/TaskBoardThumbnail.png)

Understand the complete UI of Task Board from here : [Task Board Pane]({% link docs/Features/Task_Board_Pane.md %})

## **How Does it work ?**

- This plugin scans tasks from all or the [filtered](./docs/Features/Filters_for_Scanning.md) Markdown file from your whole vault and show them on a Kanban type Board.
- You can edit the task directly from the Task Board, without opening the Markdown file.
- Add task to currently opened files using a pop-up window.

## **How to start ?**

**STEP 1 :** First install the plugin : [Installation]({% link docs/Installation.md %})

**STEP 2 :** Learn how to start using the plugin, initial setup : [Getting Started]({% link docs/Getting_Started.md %})

**STEP 3 :** Go through various examples : [Examples]({% link docs/Examples/index.md %})

**STEP 4 :** Understand all the features to use the plugin efficiently : [Features]({% link docs/Features/index.md %})

> For any queries try to find your answer here : [Frequently Asked Questions]({% link docs/FAQs/index.md %})

<script> const toggleDarkMode = document.querySelector('.js-toggle-dark-mode'); jtd.addEvent(toggleDarkMode, 'click', function(){ if (jtd.getTheme() === 'dark') { jtd.setTheme('light'); toggleDarkMode.textContent = 'Preview dark color scheme'; } else { jtd.setTheme('dark'); toggleDarkMode.textContent = 'Return to the light side'; } }); </script>
