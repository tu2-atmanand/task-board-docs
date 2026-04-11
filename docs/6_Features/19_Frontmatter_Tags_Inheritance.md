---
parent: Features
title: Frontmatter Tags Inheritance
nav_order: 19
---

## Frontmatter Tags Inheritance
{: .d-inline-block }
1.6.0
{: .label .label-blue }

Also known as **Virtual Tags**, this feature allows:

- Task Board automatically apply the tags from the frontmatter of the note to the inline-tasks present within that note, virtually.
- Filter tasks by note-level tags without adding tags to individual inline-tasks.
- Cleaner task syntax while maintaining powerful filtering capabilities

### How It Works

Lets understand this with an example. Say you have the following note:
```md
---
tags: [project, urgent]
---

Some note content.
- [ ] A task without any tag.
- [ ] Another task without any tag scheduled for today. 
```

Then this will appear inside the board as : 

![Virtual tags example](/assets/VirtualTagsExample.png)

Notice here that, the tags do not have any color styling also, since they are read-only tags, you will not be allowed to update them. These virtual tags will be mostly used for filtering the tasks.
