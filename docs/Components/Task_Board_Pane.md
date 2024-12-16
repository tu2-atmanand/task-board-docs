---
parent: Components
title: Task Board Pane
nav_order: 1
---

# Task Board Pane

This is the complete View which you will see when you will open Task Board in a new tab or in a new window.

The View consists of various sections as can be seen in the below image :

![Task Board UI Legend](../../assets//TaskBoardUIBreakLegend.png)

## View Header Section

This is the panel of any normal view. In this Bar you will able to see the current name of the active pane, which is the Task Board. On the right side in this bar, you can see the `Scan Vault` button, which will open the [Scan Vault Window](../Features/Scan_Vault_Feature.md). After that there is a `More Options` button.

## Boards Tab Section

In this section you will able to see the Tab buttons with the name of the board on them. If you have created multiple boards, there will be multiple tabs in horizontal direction. Clicking on any one, will open that specific board in the Active Board section.

On the right side of this section there are two button :

- **Configure Board :** This button will open the [Configure Board Window](../How_To/HowToUseBoardSettings.md), to change the settings of the currently active board. You can also able to see the settings of other boards in the same window as well as a tab for [Global Settings](../How_To/HowToUseGlobalSettings.md).

- **Refresh Board :** This button helps you to refresh the board with the latest data or to solve any UI anomaly you might see for few Task Items. In normal usage you might not to use this button. This button is very useful when the [Real-Time Scanning](../How_To/HowToUseGlobalSettings.md#real-time-scanning) option is **OFF** and you are doing the [manual scanning](../Features/Auto_Scanning_Files.md#manual-scanning).

## Active Board Section

In this section you will be able to see all your columns of the board in order, the way you organized them in the Board Configuration. In side the Columns you will be able to see all your tasks as a [Task Item Card](./Task_Item_Card.md) as applicable. The tasks will be placed in the respective columns based on the [column criteria](./Types_Of_Columns.md).
