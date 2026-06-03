---
parent: Plugin Settings
title: All UI
nav_order: 2
---

# All UI Tab

The All UI tab controls the visual appearance and layout of the Task Board interface and task cards.

## Task card style

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Tasks plugin emoji<br>Bases card style | Tasks plugin emoji |

Using this setting you can change the look of the [Task item card](/docs/Components/Task_Item_Card.md).


## Clean task title for inline-tasks
{: .d-inline-block }
v1.3.0
{: .label .label-green }

| Input Field | Default |
|---|---|
| Toggle | ON |

When enabled, task title is rendered without any embedded metadata/properties in the [task card title](/docs/Components/Task_Item_Card.md#task-title) for a cleaner appearance. This has been specially provided since we already have the [selective property hiding feature](/docs/Components/Task_Item_Card.md#selectively-hide-properties). So, incase if you want to see your properties separately inside the task card, you can enable this feature.

{: .new-title }
> Pro Tip
>
> Disabling this feature might improve the rendering performance. It will be very insignificant, but still helps in rendering.

## Width of Task Card

| Input Field | Default |
|---|---|
| Text Input | 300px |

Set the width of individual task cards in pixels. Enter values with the "px" suffix (e.g., "350px").

In [Map View](/docs/Features/Dependency_Map.md), card widths are individually adjustable.

## Show Column Scroll Bar

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, scrollbars appear on columns that exceed the viewport height. If you prefer cleaner look within your board, disable this feature and all the column scrollbars will be hidden.


## Edit button action

| Input Field | Options | Default |
|---|---|---|
| Dropdown | **Task Editor (Modal)** - Opens task in floating dialog<br>**Task Editor (Tab)** - Opens task in a new tab<br>**Task Editor (Window)** - Opens task in external window<br>**Open note in new tab** - Opens source file in new tab<br>**Open note in right split** - Opens source file in right panel<br>**Open note in new window** - Opens source file in new OS window<br>**Open note in hover-preview** - Shows file in hover preview | Task Editor (Modal) |

Control what happens when you click the Edit button on a task card. Choose between:
- Editing within the plugin's Task Editor (recommended for quick edits)
- Opening the source markdown file in various Obsidian locations
- Viewing in hover preview

## Double click card action

| Input Field | Options | Default |
|---|---|---|
| Dropdown | None<br>Task editor (window)<br>Open note in new tab<br>Open note in right split<br>Open note in new window<br>Open note in hover-preview | None |

Using this setting you can configure the action you want to have when you double click on the [task item card](/docs/Components/Task_Item_Card.md).

## Tag Colors

Assign custom colors to specific tags for visual organization. Tags with custom colors display with your chosen color across the board.

## Tag Color Indicator Type

| Input Field | Options | Default |
|---|---|---|
| Dropdown | **Tag Text** - Color applied to tag text<br>**Tag Background** - Color applied behind tag<br>**Card Background** - Color applied to entire card background | Tag Text |

Choose to which component the custom tag colors you have configured below, should be applied to. Changing this setting will allow you to have different board UIs.

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
- **Color picker :** A custom color picker popover will appear when you will click on this button.
- **Color Value**: Hex color code in RGBA format
- **Delete Button**: Remove the custom color to revert to theme default

{: .note }
> Custom tag colors help visually organize tasks, especially when multiple tags are assigned to a single task.
