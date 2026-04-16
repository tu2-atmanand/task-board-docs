---
parent: Plugin Integrations
title: Reminder plugin
nav_order: 7
---

# Reminder Plugin Integration
{: .d-inline-block }
1.4.0
{: .label .label-blue }

Link to the plugin : [Reminder plugin](https://github.com/uphy/obsidian-reminder).

{: .note }
> This plugin only works on desktop. For smartphone system level notification, check out the following wiki : [Notification services](./Notification_Services_Integration.md)

Task Board integrates with reminder plugin to help you never miss a deadline. Reminder plugin, helps you to get a system level notifications, as long as the Obsidian is opened in your desktop, it may not need to be active all the time.


## How the Reminder plugin works

To have a proper integration with this plugin, first we will need to understand how the Reminder plugin works...

Reminder plugin supports different kinds of formats to add the reminder date or date-time property. But Task Board only supports one of the format, by default. This is also the default format of the Reminder plugin. 

You can set reminders by putting (@YYYY-MM-DD HH:mm) to the inline-task :
```md
- [ ] Task 1 (@2021-09-15 20:40)
```

When time is omitted : 
```md
- [ ] Task 1 (@2021-09-15)
```
When you omit the time, reminder will be notified at default the default start time which is 9am.

## How to enable the integration

**Step 1 :** Open the Task Board setting and navigate to the "Automations" tab.

**Step 2 :** Now under the "Compatible plugins" section, search for the *Push notification compatibility* setting.

**Step 3 :** For this setting, select the **Reminder plugin** from the options.

Now, when you will open the [Task Editor](/docs/Features/Task_Editor.md), you should see a new input fields under the [properties section](/docs/Components/Task_Editor.md#right-section) to also add a reminder. And when you will add a reminder value, it will be added as per the above format, the former one.


{: .new-title }
> Announcement
> 
> We have a new feature on roadmap, using this feature, the Desktop system-level notifications will be supported out of the box in Task Board : [tu2-atmanand/task-board#761](https://github.com/tu2-atmanand/Task-Board/issues/761).
>
> After this feature, you will only need to care about which [notification service](/docs/Features/Plugin_Integrations/Notification_Services_Integration.md) to chose, to have mobile push notification functionality.