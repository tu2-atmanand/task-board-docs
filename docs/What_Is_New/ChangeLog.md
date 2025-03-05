---
parent: What is new
title: Changelog
---

# Changelog

_In recent [Task Board releases](https://github.com/tu2-atmanand/Task-Board/releases)..._


## Task Board v1.2.2

This version is mainly focused on fixing the major bugs users faced and which were very critical to solve for smooth working of this plugin. all the fixes has been provided in this release as mentioned below.

### Bug Fixes 🛠

- Edit task popup modal was showing old content of the task, even after editing it through the plugin itself. Fixed ✅
- Task body content was getting duplicated after editing the task through plugin, as described in #106 . Fixed ✅ 
- Edit task modal properties section (right section) border was always white in all themes. Fixed ✅ 


I missed to provide this fixes sooner as I was working on a very interesting feature coming soon in this plugin. Thought of providing the fix in the coming release, but its always good idea to fix bugs before hand.

The next version (1.3.0) will be released by next week. Stay tuned !

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.2.1...1.2.2

---

## Task Board v1.2.1

### Bug Fixes 🛠

- Following issue has been fixed : #106 

### Other Changes 🔎

- Fixed the messed up text in the priority dropdown inside Edit Task popup.


**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.2.0...1.2.1

---

## Task Board v1.2.0 🥳

> A new introductory video on YouTube : [Task Board plugin - Introduction](https://youtu.be/ZizsPBuXW8g)

### ✨ Exciting New Features 🎉  

- **Performance Optimization**: Significant UI rendering optimizations, drastically improving plugin performance. Implemented by @tu2-atmanand in https://github.com/tu2-atmanand/Task-Board/pull/102.
- **Smooth Animations**: Added seamless animations for task cards and the description section without compromising performance.  
- **Open Task Board on Startup**: Introduced a new feature allowing the Task Board to open automatically when Obsidian starts.  

---

### 🛠 Bug Fixes  

- Resolved **Issue #84**: Fixed critical bugs affecting task functionality.  
- Resolved **Issue #53**: Addressed performance-related issues with the TaskItem component.  
- **Due Date Bug Fixed**: Auto-adding due dates now works correctly. The bug that changed task due dates to today when edited using the Edit Task pop-up has been resolved. ✅  
- **Add Column Window Fix**: Fixed a styling issue where the Add Column window appeared distorted. ✅  

---

### 🔎 Other Changes  

- **React Memoization**: Applied memoization techniques across the codebase for better performance.  
- **Code Organization**: Reorganized the codebase by moving components and functionality into new, structured files.  
- **Column Data Format Update**: Changed the format used to store `column` data for better consistency and scalability.  
- **React Dispatch Reduction**: Reduced reliance on React Dispatch for a more optimized state management approach.  
- **UI Enhancements**: Made the border of task cards lighter to reduce distractions and improve overall UI aesthetics.  
- **Prop Optimization**: Removed unnecessary props and optimized the component tree for efficient rendering.  
- **Obsidian Component Fix**: Replaced the incorrect use of `new Component` with proper ItemView integration from the Obsidian library.  
- **SessionStorage Removal**: Eliminated the use of `sessionStorage`. All data is now written and updated directly to disk.  
- **Language Translation Improvements**:  
  - Moved the Python script for auto language translation to the root directory.  
  - Converted keys in the language translation file from numeric to string for better readability and usability.  
- **Predefined Boards Update**: Made adjustments to the default board and column configurations to improve user experience.  

---

These updates bring significant improvements to performance, user experience, and functionality. Thank you for your support, and we hope you enjoy the new features in Task Board v1.2.0! 🎉  

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.1.1...1.2.0

---

## Task Board v1.1.1

### Bug Fixes 🛠

- Translate the newly added/updated strings. Fixed ✅

### Other Changes 🔎

- Migrated back to `vault.modify()`

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.1.0...1.1.1

---

## Task Board v1.1.0

### New Features 🎁

- The Edit and Delete buttons in the card footer will be only visible on card hover.
- You can now open only two copies of Task Board view, one is main window and one in detached window.
- **Ribbon Icon Indicator :** Ribbon icon will glow orange to indicate there is already an Task Board window opened either in main window or in separate detached window.
- **New Icon :** The plugin Icon has been changed.
- **Edit Button Mode :** Now you can select whether the edit button should open the Edit Task window, the note in tab(with three different ways) or hover preview.


### Bug Fixes 🛠

- Due date not showing under the preview in settings. Fixed ✅
- Lot of style fixes.
- Double priority emojis are coming when adding task using modal. Fixed ✅
- Only single window will be now opened in Main window or detached window.
- The data was not updating properly and not deleting the task content from the note. Fixed ✅


### Other Changes 🔎

- Moved some of the hardcoded styles into styles.css.
- Few more strings has been translated into other languages.
- All the setting names in the Board Config Modal has been changed to match the UI of global settings.



**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.0.2...1.1.0

---

## Task Board V1.0.2 🥳

### Exciting New Features 🎉
* The UI of setting tab changed to have multiple tabs to group similar setting for easier navigation.

### Other Changes
* Language translated.
* Fixes assigned by moderator by @tu2-atmanand in https://github.com/tu2-atmanand/Task-Board/pull/91

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.0.1...1.0.2

---

## Task Board - V1.0.1

### Bug Fixes
- Resolve the issue of settings not loading during initial installation. (Silly Mistake 😋)
- Few CSS styles fixes.

### Other Changes
- Optimize few coding practices as per Obsidian Plugin Guidelines.
- Translate the updated strings to other languages.

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.0.0...1.0.1


---

## Task Board 1.0.0

I am excited to announce the first official release of Task Board, to make it available on the Obsidian Plugin Marketplace.🥳🎉

### Release Overview

This initial release marks the transition from private development to public availability. Future updates will adhere to Semantic Versioning standards.

### Known Limitations and Considerations

While the plugin has been thoroughly tested, you might encounter the following aspects during usage (rare) :

- Desktop-only support: Mobile compatibility is currently under development.
- Theme compatibility: Some themes might not be fully compatible, you might feel the Task Board View do not blends well with the theme.
- Rare functionality issues: In exceptional cases, intended functionalities might not execute as expected.

If you encounter any of these issues, please report them using the [how to create request](https://tu2-atmanand.github.io/task-board-docs/Advanced/HowToCreateRequest.html) docs.

### Future Development and Contributions

A structured development plan is underway to integrate remaining functionalities for it to give what it is meant for. We invite interested individuals to join our development team and contribute to accelerating progress. Explore contribution opportunities : [Contribute to this project](https://github.com/tu2-atmanand/Task-Board?tab=readme-ov-file#how-to-contribute).

Thank you for using Task Board!🙏💖