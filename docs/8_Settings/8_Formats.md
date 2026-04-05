---
parent: Plugin Settings
title: Formats
nav_order: 8
---

# Formats Settings

The Formats tab controls date formats, time formats, and timezone handling throughout Task Board. Consistent formatting ensures compatibility with other plugins.

## Universal date


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
