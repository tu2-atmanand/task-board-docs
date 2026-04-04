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

- Task Board automatically applies frontmatter tags from notes to all the inline-tasks within those notes
- Filter tasks by note-level tags without adding tags to individual tasks
- Cleaner task syntax while maintaining powerful filtering capabilities

### How It Works

If your note has frontmatter like:
```yaml
---
tags: [project, urgent]
---
```

All tasks in that note will inherit these tags and can be filtered accordingly in your board.
