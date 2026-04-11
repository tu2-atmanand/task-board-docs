---
parent: Plugin Settings
title: All UI
nav_order: 2
---

# All UI Tab

The All UI tab controls the visual appearance and layout of the Task Board interface and task cards.

## Task card style


## Clean task title for inline-tasks
{: .d-inline-block }
v1.3.0
{: .label .label-green }

| Input Field | Default |
|---|---|
| Toggle | ON |

When enabled, task titles display without any embedded metadata/properties in the task card body for a cleaner appearance. This pairs well with the header and footer toggles to create different visual styles for your board.

## Width of Task Card

| Input Field | Default |
|---|---|
| Text Input | 300px |

Set the width of individual task cards in pixels. In Map View, card widths are individually adjustable. Enter values with the "px" suffix (e.g., "350px").

## Show Column Scroll Bar

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, scrollbars appear on columns that exceed the viewport height. Enabling this uses a small amount of column width for the scrollbar.

## Tag Color Indicator Type

| Input Field | Options | Default |
|---|---|---|
| Dropdown | **Tag Text** - Color applied to tag text<br>**Tag Background** - Color applied behind tag<br>**Card Background** - Color applied to entire card background | Tag Text |

Choose how custom tag colors are displayed. When using "Tag Text", opacity is automatically reduced to 0.2 for better text readability.

## Tag Colors

Assign custom colors to specific tags for visual organization. Tags with custom colors display with your chosen color across the board.

### Adding Custom Tag Colors

1. Click **"Add tag color"** button
2. Enter the tag name (e.g., `#important`)
3. Use the color palette to select a color
4. Set the opacity value (0 to 1, e.g., 0.4)
5. Confirm to save

### Managing Tag Colors

For each custom tag color you see:
- **Preview**: Visual sample of how the tag appears in task card headers
- **Tag Name**: The tag being customized (not editable once created)
- **Color Value**: Hex color code in RGBA format
- **Delete Button**: Remove the custom color to revert to theme default

{: .note }
> Custom tag colors help visually organize tasks, especially when multiple tags are assigned to a single task.
