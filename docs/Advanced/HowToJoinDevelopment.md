---
parent: Advanced Topics
title: Join the plugin Development
nav_order: 5
---

# How to join the plugin development
{: .d-inline-block }

Advanced
{: .label .label-yellow }

To contribute for development of this project on github, I have made few fixed branches for now, which have their specific intent.

The complete workflow and roadmap can be tracked from the [Task Board GitHub Project](https://github.com/users/tu2-atmanand/projects/2). From this roadmap kanban view, you will able to find which issues are pending for the upcoming release, which issues are being currently worked on and which issues has been completed and are ready for review.

If you feel like, you can work on any issue which has not been assigned to any one. Then open the issue, go to the end and add a new comment by tagging the project admin and mention that you want to start working on this issue. Also ensure that, no one else has commented the same, else it will be same work being done by two people.

After mentioning this you can directly start working on the issue by creating a fork of the project and then creating a new branch from the latest code.

---

## Fixed Branches

### `Main` branch

This branch will only contain the code which has been published in the production build. This branch will not going to accept any directly branches. This main branch will only accept pull requests for either small changes like updating the docs and for small bug fixes. For major changes like feature implementation, it should be first merged in the dedicated [version release branch](#version-release-branch), and only after thorough testing, it will be merged into this main branch.


### Version release branch

This branch will going to contain all the finalized code planned to be released for the upcoming version release. For example, if the next upcoming major version is `1.10.0`. Then you will see a branch with the name `release-v1.10.0`. After a specific feature, which has been planned for the release `1.10.0` has been completed, it will be merged into this branch. Later, once all planned features has been completed, this branch will going to contain the latest code for the upcoming major version release.

At the end, after every planned changes has been completed :
- Will remove all the console statements.
- All development code, delete unnecessary comments.
- Write better comments.
- If any strings has been changed, translate those updated strings to other languages.
- And finally, this version release branch will be merged into the `main` branch for version release.

{: .new-title }
> Important
>
> It is highly recommended that you create your branch from this "version release branch", so that you can have the latest code and your pull request can be merged easily. Because, sometimes a lot of changes has been done in these "version release branches", hence working on the latest code will be beneficial.
>
> Additionally, you may keep an eye on the "In progress" column under the [roadmap kanban board](https://github.com/users/tu2-atmanand/projects/2), to know which feature is being actively worked on and it will be associated with the specific feature branch, with the latest code.
>
> Once you have submitted your pull request, the admin can then decide whether to release your changes in the upcoming version release or for future releases.


### `pluginTesting` branch

This branch has been specially created to do through testing and may contain extra test files. This branch may or may not be on the latest code, but it will be occasionally used for the latest code testing.

The admin may use this branch as well to first merge your code in this branch, test it thoroughly with the existing features and once everything has been found to be working, your PR will be finally merged in the production code.

The main idea is, after any big changes has been performed, for example a big feature has been implemented in its dedicated branch. Then, will merge these feature into this `pluginTesting` branch first and will perform through testing on this new feature as well as its integrity with the rest of existing feature. Once everything has been found to be working. Will give a green light to merge this feature branch to the "[version release branch](#version-release-branch)".

---

## Nomenclature for branches

While creating new branches, please follow the below criteria to maintain a common ground for everyone to understand the branches better.

### For working on a feature

If you are creating any branch to integrate a new feature (an issue which has feature label). Then while naming your branch, start the name with **feat-** followed by the short name of the feature. For example if you are creating a branch to integrate drag and drop feature. Then the branch name will be : **feat-dragNdrop**.

### For solving a bug

If you are creating any branch to fix/solve any bug. then start the name of the branch with **fix-** followed by short name of the bug.

### For enhancing an existing feature

If you want to improve any existing feature or UI then you can create a branch whose name should start with **enha-**. This will be for small enhancements or mainly for UI enhancements. For big enhancements, like changing some algorithm in the background to make the things work faster, you may go for creating an optimization branch as explained below.

### For optimizing an old functionality

If you want to create a branch to

- Optimize some existing code.
- Find a better algorithm for the old working code.
- Use some different better libraries to do the same thing.

Create a branch with the name starting with **opti-** followed by the short name of what you are trying to achieve.
