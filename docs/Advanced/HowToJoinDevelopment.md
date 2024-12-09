---
parent: Advanced Topics
title: Join the plugin Development
---

# How to join the plugin development

Advanced {: .label .label-yellow }

To contribute for development of this project on github, I have made few fixed repositories for now, which have their specific intent.

The complete workflow can be tracked from the [Task Board GitHub Project](https://github.com/users/tu2-atmanand/projects/2).

You can go through which issue/feature has been worked on at present, which issues are ready to be implemented and which issues has not been assigned at present to anyone or haven't been started yet.

If you feel like, you can work on any issue which has not been assigned to any one. Then open the issue, go to the end and add a new comment by tagging the project admin and mention that you want to start working on this issue. Also ensure that, no one else has commented the same, else it will be same work being done by two people.

After mentioning this you can directly start working on the issue by [creating a fork]() of the project and then creating a new branch from the `pluginTesting` branch.

---

## Fixed Branches

### Main

- This branch will only contain the code for publishing. This branch will only accept merge request through `pluginTesting` branch. First a proper testing should be done in the pluginTesting branch to merge changes to main branch. This will be done by the project admin.

### pluginTesting

- This branch will be always on the latest working code. After any new functionality implementation has been done or any bug has been resolved, it will be always merged to this branch.

- After the new merge, a thorough testing will be done on this branch, to test whether the new additions are working as expected. After the admin has tested everything a commit will be added as : "New changes working".

- You are requested to create a new branch from this commit, to start your development. Since this is the checkpoint that everything has been working as expected.

- While submitting a Pull Request, please ensure that you are submitting the PR on this branch and not on the main branch.
  - After the admin has reviewed your contribution, the PR will be accepted and will be merged into the `pluginTesting`.
  - All the necessary changes will be done. Remember, if the feature you have suggested doesn't goes well with the overall plugin, then it will be removed at this stage.
  - After proper testing, a commit will be made with the comment : "New changes working" as mentioned in the above point.

### cleanupToRelease

This branch is to be used, after every planned issue for the upcoming release/milestone has been achieved and after testing, everything is working. Create this branch from the `pluginTesting` branch to clean up the code and make it ready for releasing.

In this branch :

- Will remove all the console statements.
- All development code, delete unnecessary comments.
- Write better comments.
- If any strings has been changed, translate those updated strings to other languages.

---

## Criteria for creating a new branch

While creating new branches, please follow the below criteria to maintain a common ground for everyone to understand the branches better.

### For working on a feature

If you are creating any branch to integrate a new feature (an issue which has feature label). Then while naming your branch, start the name with **feat-** followed by the short name of the feature. For example if you are creating a branch to integrate drag and drop feature. Then the branch name will be : **feat-dragNdrop**.

### For solving a bug

If you are creating any branch to fix/solve any bug. then start the name of the branch with **bug-** followed by short name of the bug.

### For enhancing an existing feature

If you want to improve any existing feature or UI then you can create a branch whose name should start with **enha-**.

### For optimizing an old functionality

If you want to create a branch to

- Optimize some existing code.
- Find a better algorithm for the old working code.
- Use some different better libraries to do the same thing.

Create a branch with the name starting with **opti-** followed by the short name of what you are trying to achieve.
