# How to join the plugin development

To contribute for development of this project on github, I have made few fixed repositories for now, which have their specific tasks.

The complete workflow can be tracked from the Task Board GitHub Project.

You can go through which issue/feature has been worked on at present, which issues are ready to be implemented and which issues has not been assigned at present to anyone or havent been started yet.

If you feel like, you can work on any issue which has not been assigned to any one. Then open the issue, go to the end and add a new comment by taggin the project admin and mention that you want to start working on this project. Also ensure that, no one else has commented the same, else it will be same work being done by two people.

After mentioning this you can directly start working on the issue by [creating a fork]() of the project and then creating a new branch from the `pluginTesting` branch.

---

## Fixed Branches

### Main

- This branch will only contain the code for publishing. This branch will only accept Pull request or merge request through `pluginTesting` branch. First a proper testing should be done in the pluginTesting branch to merge changes to main branch.

### pluginTesting

- This branch will be always on the latest working code. After any new functionality implementation has been done or any bug has been resolved, it will be alwats merged to this branch.

- After the new merge, a thorogh testing will be done on this branch, to test whether the new additions are working as expected and can be moved on further. After the admin has tested everything a commit will be added to specify the same. After that you can create a new branch from this point of commit to work on a new issue. And the admin will also go for merging new Pull Request to this branch and the process will continue.

### cleanupToRelease

This branch is to be used, after every planned issue for the upcoming release/milestone has been achieved and after testing, everything is working. Create this branch from the `pluginTesting` branch to clean up the code and make it ready for releasing.

In this branch :

- Will remove all the console statements.
- All development code, delete unncesary comments.
- Write better comments.
- If any strings has been chaged, translate those updated strings to other languages.

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
