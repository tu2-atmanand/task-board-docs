---
parent: Plugin Settings
title: Formats
nav_order: 8
---

# Formats Settings

The Formats tab controls date formats, time formats, and timezone handling throughout Task Board. Consistent formatting ensures compatibility with other plugins.

## Universal date

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Start date<br>Scheduled date<br>Due date | Due date |

This plugin supports multiple kinds of date with their unique significance which satisfies various requirements for your tasks management. For example, created date, start date, scheduled date, etc.

But, there are mainly three dates which you will mostly going to use while day to day working with your tasks. These are Start date, Scheduled date and Due date. In Task Board, there are various functionalities, where it needs a date on your tasks for those functionalities to work and through this setting you are instructing this plugin to use this specific date when Task Board will try to apply that functionality.

For example, if you have enabled the [daily notes plugin compatibility feature](/docs/6_Features/15_Plugin_Integrations/9_Daily_Notes_Plugin.md), then the name of the daily note (which will be mostly a date value), will be assigned as the scheduled date to all the inline-tasks within that specific daily note.

 Hence, its necessary that you select the date which is most significant for you as the universal date in this plugin.


## Date Format

| Input Field | Default |
|---|---|
| Text Input | yyyy-MM-dd |

Specify the format for all date fields throughout Task Board. This format is used for:
- Due dates
- Start dates
- Created dates
- And all other date properties

Uses `date-fns` library format patterns:
- `yyyy` - Calendar year (2024)
- `MM` - Month (01-12)
- `dd` - Day of month (01-31)

{: .note }
> Keep this format consistent with your Daily Notes file naming convention for the Daily Notes compatibility to work correctly.

For all valid date format patterns, see: [date-fns Format Documentation](https://date-fns.org/docs/format)

## Date-Time Format

| Input Field | Default |
|---|---|
| Text Input | yyyy-MM-dd/HH:mm |

Specify the format for date-time values (date + time). This format applies to:
- Task completion timestamps
- Task creation timestamps
- Other date-time properties

{: .warning }
> Do not confuse with date-only format. Use 'HH' for 24-hour format or 'hh' for 12-hour format.

## First Day of the Week

{: .d-inline-block }
Future feature
{: .label .label-yellow }

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday | Monday |

This setting is reserved for future features and upcoming plugin integrations. Currently not actively used.

## Task Completion in Local Time

{: .d-inline-block }
Future feature
{: .label .label-yellow }

| Input Field | Default |
|---|---|
| Toggle | ON |

This setting is reserved for future implementation. When enabled in a future version, task completion timestamps will use your local timezone.

## Show UTC Offset for Task Completion

{: .d-inline-block }
Future feature
{: .label .label-yellow }

| Input Field | Default |
|---|---|
| Toggle | OFF |

This setting is reserved for future implementation. When enabled, task completion timestamps will include UTC offset information (e.g., +05:30).
