---
parent: Plugin Settings
title: Map View
nav_order: 6
---

# Map View Tab

The Map View tab contains settings specific to the [Map view feature](../6_Features/16_Dependency_Map.md).

## Render only visible nodes

| Input Field | Default |
|---|---|
| Toggle | OFF |

This project uses the [ReactFlow library](https://reactflow.dev/) to create this Map view. And this library has a nice option to allow whether to render all the nodes at once when the view is initialized or only render the nodes which are visible inside the viewport.

This setting has been specially provided, so that users can see if there is any improvement when the setting is enabled or disabled. Based on the users feedback, in the future the plugin will remove this setting and make the behavior which provides a smoother experience as the default one.


## Mouse wheel behavior

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Zoom<br>Pan | Zoom |

Different canvas based softwares have their own controls. This setting allows users to change the default behavior, so they can have the same mouse controls which they mostly use in other softwares.


## Canvas background style

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Default<br>Transparent<br>Dots<br>Lines<br>Cross | Default |

This setting allows to change the background style of the canvas. The default option means a plain color as per the background of other panes inside the Obsidian. Try changing this setting to see how the background looks in different styles in your theme.


## Map orientation layout

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Horizontal<br>Vertical | Horizontal |

Tasks map, is basically how you arrange your tasks in sequential order to indicate the flow of your workflow. From child task to parent task to grand parent task and so on...

This setting will help you to decide whether you want to go from left-to-right(Horizontal) or from top-to-bottom(Vertical).

**Horizontal :** The right side of a child-task will be connected to the left side of a parent-task.

**Vertical :** The bottom side of a child-task will be connected to the top side of a parent-task.

If you like to have a reverse order, please [request this feature](/docs/10_Advanced/2_HowToCreateRequest.md) to the developer.


## Link arrow direction

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Child to parent<br>Parent to child<br>Both way | None |

Different dependency based graphs have their own nomenclature for arrows which connects the main task to their depends-on(child) tasks.

This setting helps you to get the same UI layout, so you dont feel confused if this methodology is a little different from how you like to see your dependency graph.


## Link style

| Input Field | Options | Default |
|---|---|---|
| Dropdown | Straight<br>Step<br>Smooth step<br>Curved | Curved |

Use this setting to change the look of the connections. Each style will give a slightly different feel. Try the different available styles to choose which one best works for you.


## Animate links

| Input Field | Default |
|---|---|
| Toggle | OFF |

Enabling this setting will animate your links with a nice flowing animation, which goes from child-task to the parent task. This helps you to understand how your work is flowing and in which direction you should proceed to complete your tasks.


## Show minimap

| Input Field | Default |
|---|---|
| Toggle | OFF |

A small minimap is available within the map view. This minimap has a lot of features beside just seeing the complete overview of your canvas. Using this minimap you can also navigate within the canvas by simply dragging within the minimap using the left mouse button. Enable or disable this setting to show or hide this minimap inside your map view.