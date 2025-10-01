---
parent: What is new
title: Changelog
---

# Changelog

_In recent [Task Board releases](https://github.com/tu2-atmanand/Task-Board/releases)..._


## Task Board v1.6.11

### New Features 🎁

- Move cursor to focus inside the search input field, after clicking search icon | #347 
- Auto-hide board progress bar on small screens or screen resize for clean look.
- Dont show keyboard while opening the `AddOrEditTaskModal` on phones. | #334
- The cache file path setting has been changed from Multi-Suggest text field to drop-down field.

### Bug Fixes 🛠

- Filter polarity is not set to **Deactivate** state while creating new board. (#346) | Fixed ✅
- Adjust the height based on platform and window height. (#239) | Fixed ✅
- The cache file path setting throws error while entering a custom path. | Fixed ✅


### Other Changes 🔎

- Multiple small UI fixes and enhancements.


**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.10...1.6.11

---

## Task Board v1.6.10


### Bug Fixes 🛠

- Indexes of default boards are starting from 1 (#340 ). Fixed ✅


**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.9...1.6.10

---

## Task Board v1.6.9


### Bug Fixes 🛠

- View breaks when board config is empty for selected board index. Fixed ✅
- Few logical flaws in "Filters for scanning". (#345) Fixed ✅


### Other Changes 🔎

- Passing `plugin.app` instead of Obsidian app for better plugin integrity with the app.
- Pass the boardConfig modal itself instead of passing the activeBoardIndex.
- Better user-friendly messages has been added when the board doesn't have columns, etc.

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.8...1.6.9

---

## Task Board v1.6.8


### New Features 🎁

HUGE OPTIMIZATION : The tasks cache will now be loaded from RAM instead of DISK. Reduced a lot of DISK read-write operations.


### Bug Fixes 🛠

- Tasks cache is not getting updated when either file or folder is renamed, moved or deleted. (#338) | Fixed ✅
- After re-scan, collected tasks are not shown in the modal. | Fixed ✅
- After deleting boards, the indexes of the other boards are not updating properly. (#340) |  Fixed ✅
- Tasks cards flowing out, when Column Scroll bar is in hidden state through the setting. (#239) | Fixed ✅
- An extra empty line is always added in the file after editing the task. | Fixed ✅
- Tags with '-' symbol are not picked up as tags. (#340) | Fixed ✅
- Not able to change the date-type for **Undated** columns in Board Config Modal. | Fixed ✅
- The board name tab buttons are unresponsive in Board Config Modal. | Fixed ✅


### Other Changes 🔎

- `debounce` will be now loaded from the `obsidian` package instead of a separate package. Reduced the plugin size ⇾ Improving load time.


### Acknowledgement

A huge thanks to all the following users of Task Board for reporting these issues and collaborating continuously, for testing the bugs and the features. Because of this active interactions, I even found more flaws, which has been fixed.

- @holloway87
- @Buddinski88
- @ksdavidc
- @pcause
- @Paining1
- @itpropaul

Also, thank you to all those who has reached out to me on different platforms to report bugs and suggest ideas.

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.7...1.6.8

---

## Task Board v1.6.7

### New Features 🎁

- Use the indentation value from Obsidian setting instead of using tab as the default indentation. | #333 

### Bug Fixes 🛠

- Task doesnt save inside the new selected file when QuickAdd plugin is enabled. Fixed ✅ | #298 
- Scan filters are not working properly when **"Only scan this"** option has been selected. Fixed ✅ 
- Tasks with indentation is being scanned, which causes issues afterwards. Fixed ✅ 
- On-completion property has not been handled properly. Fixed ✅ | #337 
- Universal date value is taken from daily note name instead of task line. Fixed ✅ | #335
- Few language file names and their language codes are not matching Fixed ✅ | #336

### Other Changes 🔎

- Spelling correction in description inside the menifest.json file.
- Update License name inside package.json file.
- Added `en.json` file for making the language translation process easier. 
- Updated the docs for language translation contributions : [How to contribute to language translations](https://tu2-atmanand.github.io/task-board-docs/docs/Advanced/Contribution_For_Languages/).


**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.6...1.6.7

---

## Task Board v1.6.6

### New Features 🎁

- A new filter in "Filers for scanning" for scanning files based on their frontmatter. | #185 


### Bug Fixes 🛠

- Filters for scanning donot work properly when all filters are used simultaneously. #312 | Fixed ✅
- Tasks with tags which are in uppercase are being not scanned. #327 | Fixed ✅
- A slightly different format for time range breaks the view. #328 | Fixed ✅
- Empty tasks are being scanned again in the latest version. #205 | Fixed ✅


### Other Changes 🔎

- Few function name changes.

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.5...1.6.6

---

## Task Board v1.6.5

## Bug fixes 🛠

- Bug Reporter modal is shown too many times for renderHeader error. Fixed ✅
- The filters for scanning do not refresh, after we edit them. | Fixed ✅
- Path filtered column is not filtering tasks from a single note selected in setting. | FIxed ✅


### Other changes 🔎

- Take the universalDate selected by user as the default date while creating a new column | #326
- Few function names changes and arguments name changes.

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.4...1.6.5

---

## Task Board v1.6.4

### Bug fixes 🛠

- Plugin is unable to load on fresh install. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.3...1.6.4

---

## Task Board v1.6.3

### Bug Fixes 🛠

- Load failure in mobile when loading the plugin. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.2...1.6.3

---

## Task Board v1.6.2

### Bug Fixes 🛠

- Can't open plugin settings on mobile. Fixed ✅
- Avoid unnecessary re-renders while moving cards across columns.

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.1...1.6.2

---

## Task Board v1.6.1

### Bug Fixes 🛠

- Plugin is unable to load on few devices. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.6.0...1.6.1

---

## Task Board v1.6.0 🎉

### New Features 🎁

- **Huge improvement in load time :** Now download/update the language translation file on demand. No more bundling all the language files with the plugin bundle. Plugin bundle size has been reduced by a great factor to improve the load time. | #284
- **Safe Guard :** Never lose your content. Proper content match will be done before updating your content. A new Content Compare modal to see the changes.
- **Path filtered column :**  A new type of column to filter out all the tasks from a specific file in the column. | #269
- **Re-order boards :** Now change the order of the boards inside Board Configure modal. Move default board on top. | #238 
- **Frontmatter tags inheritance :** Get your notes frontmatter tags applied to the tasks within the notes. (also known as **Virtual tags**) | #268 
- **Search tasks :** A new search bar to search your tasks on the board for content only. (filters coming soon) | #77
- A new setting to select the notification service you want to use, and get the same formatting while adding reminder property. | #289 
- **Task count statistics :** Get tasks count in the whole board with a progress bar and task count for each column in column header. | #258
- **Card UI :** More card customizations to show and hide sub-tasks and description sections by default and with sub-tasks progress bar when hidden | #257
- Change the tasks cache file location, `tasks.json`, from the plugin configuration folder to anywhere inside the vault. Very helpful and essential in case you sync your vault on multiple devices. | #296 
- A new reminder input field, to select date-time value in the format you want. Add reminder at any time on any date. | #289
- Add the task property at the cursor position, instead of always appending it at the end of the task. | #281 
- A better modal to enter the **Scanning Filters** with suggestions and improved UI/UX of the setting. | #282


### Bug Fixes 🛠

- Changes made in Raw Editor doesnt reflects inside Live Editor. | Fixed ✅
- Add the missing English translations strings. | Fixed ✅
- The content goes hidden while adding a task in **Add new task modal**. | Fixed ✅
- Second board is not showing up while switching board. | Fixed ✅

### Other Changes 🔎

- Upgraded all packages to latest.
- Changed various settings location in setting tab.
- Now the file will be rescanned after the task has been written to the file to maintain the consistency of the data on board and in the file.
- This version has done huge amounts of code optimization and code refactoring.
- The input fields for adding priority in the column configuration has been converted to a drop-down selector.
- A ton of function name changes for better code readability.
- Changed the compoenent names and added the view switcher drop-down in header.


### New Contributors
* @luisllamasbinaburo made their first contribution in https://github.com/tu2-atmanand/Task-Board/pull/270

### Contributions

* Added frontmatter inheritance by @luisllamasbinaburo in https://github.com/tu2-atmanand/Task-Board/pull/270
* Added path filtered column by @luisllamasbinaburo in https://github.com/tu2-atmanand/Task-Board/pull/271
* Added reorder boards by @luisllamasbinaburo in https://github.com/tu2-atmanand/Task-Board/pull/272
- Russian translation file ([ru.json](https://github.com/tu2-atmanand/Task-Board/blob/main/src/utils/lang/locale/ru.json)) has been updated by @sakkir91. | #303

Additionally, a big shout-out to the following contributors for helping me with testing the bugs, suggesting improvements and keeping the community active : 
- @Paining1 
- @craziedde 
- @yeqiongtianmang 
- @JasonSwindle 

And thank you to all those who had reached out to me on various other platforms for feedback and suggestion for improvement of this plugin.❤


**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.5.2...1.6.0

---

## Task Board v1.5.2

### Bug Fixes 🛠

- Editor inside task body not refreshing after saving. Fixed ✅
- QuickAdd plugin integration is not working as expected. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.5.1...1.5.2

---

## Task Board v1.5.1

### Bug Fixes 🛠

- Add/Edit task modal keeps opening on the startup. Fixed ✅
- Unable to create new board. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.5.0...1.5.1

---

## Task Board v1.5.0 🎉

### New Features 🎁

- Live Embedded Editor inside Add or Edit task modal. | #50
- **Bug Reporter** : A new modal to get better error information and collect bug report faster. | #204
- **Add task from anywhere to any note** : Set a default note to add new task from anywhere or choose the file directly from the modal using file suggester. | #142, #193, #212
- **QuickAdd plugin integration :** Create different *QuickAdd choices* and select any one from the modal to add your task wherever you want.
- Re-scan vault indicator on plugin update. | #182
- **Scheduled**, **Start** and **Created** date properties has been added for better Tasks plugin integration.
- **Recurring tasks** integration using Tasks plugin API. | #15
- A very first **Task Board API** for accessing the `Add or Edit task modal`. | #192
- Strike-out styling for completed sub-tasks in the Task Item Card. | #216
- Automatically hide columns with no tasks. | #183
- **Archive tasks** instead of deleting them by commenting out the complete task content. Or move them to a separate *archive note*. | #115
- Scroll to the exact location of the tasks in the note and highlight the first line of the task. | #206
- Cancelled date property integration.
- New type of column to filter out tasks with similar task status. | #151
- New type of column to filter out all the tasks with same task priority value. | #152
- A tag suggester in the *Add or Edit task modal*. | #264
- Show note name in the Task Item Card header. | #147


### Bug Fixes 🛠

- The *Tagged* name and other input fields loose focus after typing one letter in Board config modal | #240
- Add new task in current file not working as expected. | #255
- Column type names are not shown as per the Docs inside Board Config modal. | #276
- Crypto library is not available on mobile phones.
- Add column modal open unexpectedly while switching boards.
- `pickr` library is not working as expected when the *Highlightr* plugin is disabled.
- Few UI Improvements and fixes.
- Removed the limit on tag character length. | #279
- Wrap column row properties inside the Board Config modal to wrap properly on small screens. | #266


### Other Changes 🔎

- Rename file `TaskItemProps.ts` to `TaskItem.ts`.
- Created separate classes for every community plugin integration for better accessibility.
- Renamed `syncSettings` function to `migrateSettings`.
- New language translations and updated few old ones.
- Removed the Completion date format setting. From this version onwards, a universal date format will be used for all the tasks.
- `universalDate` concept has been introduced instead of `dueDate` concept.

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.4.2...1.5.0

---

## Task Board v1.4.2

### Bug Fixes 🛠

- **Highlightr** plugin integration is not working properly. Fixed ✅
- **Reminder** plugin integration is not working properly. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.4.1...1.4.2

---

## Task Board v1.4.1

### Bug Fixes 🛠

- "otherTags" column is not showing tasks with all tags other than named tags. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.4.0...1.4.1

---

## Task Board v1.4.0 🎉 | Mobile Support

> YouTube video for this release : https://youtu.be/R3gHqyHi71w

### New Features 🎁

- **Mobile Support :** Task Board now supports mobile devices and small screens after a lot of UI/UX improvements (#78).
- **Reminder plugin compatibility :** Easily add a reminder to any plugin using the same due date and scheduled time values (#85).
- **Highlightr plugin compatibility :** Now users can add highlighting HTML tags, such as `<mark>` and `<font>`  to style their tasks(#200).
- **Card background color based on tag :** A new way to using your tag color to locate the tasks easily using their background color (#104).
- Outline shadow for Task Item cards (#66).
- The due indicator bar color will now going to also consider the scheduled time to change its color. A new color, 'blue' has been added to indicate the start of the task. (#80)
- Added `data-column-type`, `data-column-tag-name` and `data-column-tag-color` as the new *data attributes* for the column component, so different themes can now give better support (#191).
- Task Board will now use **pickr** package to provide a better color picker and **sortablejs** for giving better experience for updating the tag color priority (#118).

### Bug Fixes 🛠

- Tasks starting with numbered bullets has too much left padding (#201). Fixed ✅
- Tasks plugin format not working properly to detect scheduled time property (#197). Fixed ✅
- Completion Emoji is visible even for tasks with no completion date property. Fixed ✅
- "Undated" option is not present in the drop for choosing column type in **Add column modal** (#219). Fixed ✅
- Task Item cards duplicates in **"otherTags"** type column even after populating in a **"namedTag"** type column (#190). Fixed ✅

### Other Changes 🔎

- Add sub-task button will now going to add the new sub task at the bottom of the list, unlike on top. (#168)
- "Save" button will be now hidden when switched to "global setting" tab from the Board Config Modal.
- Migrated to `sortablejs` package for achieving the drag and sort functionality for changing tag color order and columns order.
- Cleaned up unused packages and other minor optimizations .
- Moved the `TaskBoardSettingTab.ts` file to "Settings" directory.
- Changes in the Russian translation. by @sakkir91 in https://github.com/tu2-atmanand/Task-Board/pull/230


### New Contributors
* @sakkir91 made their first contribution in https://github.com/tu2-atmanand/Task-Board/pull/230


**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.3.2...1.4.0

---

## Task Board v1.3.2

### Bug Fixes 🛠

- Clicking on edit button inside hover modal is opening another hover modal instead of opening edit task window. Fixed ✅
- Loading screen stucks, when the board config is empty. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.3.1...1.3.2

---

## Task Board v1.3.1

### Bug Fixes 🛠

- The board config data corrupts after re-scanning the vault. Fixed ✅

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.3.0...1.3.1

---

## Task Board v1.3.0 🎉

> YouTube video for this release : https://youtu.be/lTDf0nZmZgM

### New Features 🎁

- **Status for Tasks :** A new property for adding status to your tasks, similar to the one from [Tasks plugin](https://publish.obsidian.md/tasks/Getting+Started/Statuses/About+Statuses).
- **Robustness :** Task Board is not robust enough to work with all your custom task formats. No need to restrict yourself anymore with the pipe symbol (|) functionality to separate your task properties (metadata). Write your tasks the way you want in your notes and Task Board will preserve the format.
- **Confirmation Popup :** After adding any property in the Edit task modal, a confirmation popup will be shown if you accidentally close the modal without saving. #92
- Emojis support for the checkboxes with different statuses. Shout out to [@ITS-Theme](https://github.com/SlRvb/Obsidian--ITS-Theme) for the [Alternate Checkbox CSS Snippet](https://github.com/SlRvb/Obsidian--ITS-Theme/blob/main/Snippets/S%20-%20Checkboxes.css).
- Improved integration with Tasks plugin, to get the same options for setting the task status.
- A new setting option to hide the metadata from task title inside the Task Item card for a clean look.
- A new command to access the "Scan vault window" easily.

### Bug Fixes 🛠

- Dated columns not able to segregate tasks and they appear one day off, as discussed in #130. Fixed ✅
- All bugs discussed in the issue #119. Fixed ✅
- Priority was not detected properly. Fixed ✅
- zh-CN language wasn't detecting due to mismatch of lang code mapping. Fixed ✅

### Other Changes 🔎

- Changed the way how dated columns range works. No more support for infinity. Please refer this : https://tu2-atmanand.github.io/task-board-docs/docs/Components/Types_Of_Columns/#dated
- Improved toggle button and description area in the Task card.
- Improved checkbox animation.
- Updated props of various functions.
- Task Board will now be using [Obsidian Typings](https://fevol.github.io/obsidian-typings/) for better APIs support.
- Improved the fresh install welcome screen with better instructions.
- Made the border of Task Item cards a little lighter.
- Due date property can now support both formats *2025-03-07* and *07-03-2025*.
- Loading animation while opening the view.
- Enhanced the language translations for `es.ts`. Credit goes to @Patxi080
- Enhanced the language translations for `zh-CN.ts`. Credit goes to @erduotong

### New Contributors
* @Patxi080 made their first contribution in https://github.com/tu2-atmanand/Task-Board/pull/148
* @erduotong made their first contribution in https://github.com/tu2-atmanand/Task-Board/pull/164

**Full Changelog**: https://github.com/tu2-atmanand/Task-Board/compare/1.2.2...1.3.0

---

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