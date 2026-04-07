---
parent: How To
title: Use Board Settings
nav_order: 6
---

# How to use the Board Specific Settings

You can open the Board Specific Settings from the **Board configure button** on the top right corner in the Task Board View as can be seen in the below image.

![BoardConfigButton](/assets/BoardConfigButton.png)

This will open the settings panel as shown below :

![BoardConfigureModal](/assets/BoardConfigureModal.png)

Learn more about all the UI elements of this modal from here : [Board config modal](/docs/7_Components/8_Board_Config_Modal.md).

{: .new-title }
> Save Button
>
> Remember to press on the `Save` button after you have changed any value for the Board settings.

## Basic Settings

### Board name

In this text input field you will be able to enter the Name of the Board or change it any time

### Board description


### Show tags in task card header

{: .note }
> This settings only works for [Tagged type of columns](/docs/6_Features/5_Types_Of_Columns.md#tagged).

Since, the column of type namedTag will show all the tasks which has the specific tag. Then it makes no sense to show the tag on the tasks, since its obvious that all the tasks under the specific column will have the same tag as that of the Column tag.
Hence you can decide to hide this tag from all the Task Items under this column.

For multi-tag Task Item, other tags will be show, only the specific tag will be hidden.


### Auto hide empty columns

## Configure swimlanes

## Columns

Under this section of settings you will see a tabular format arrangement to configure the columns under this board and also change their position.

The first row in this tabular data show the information of the Task Board column and it will be show at the first position in the Task Board View. Followed by the rest of the Columns in order.

### Properties of the Column

**Handler Button :** This button helps you to drag and drop the row, to arrange the postion of the Column inside the Task Board. If you want to change the position of the column, say from the first position to the third. Then you will have to drag the row inside this Tabular data to the third position. After saving your column will be moved to the third position from the first.

**Eye Icon :** Use this button to hide your column from your board. If say, you dont want to see a specific column in the current board, but also do not want to delete that column. You can keep the board hidden, as long as you want.

**Column Type :** At present the plugin supports 6 different types of columns. Learn more about each of them and how to enter the values to create these columns from here : [Types of Columns](/docs/6_Features/5_Types_Of_Columns.md).

**Column Name :** This text input field will allow you to enter or change the name of the column. You can enter a custom name, which you would like to see on the Column bar.

**Column Properties :** You will notice there are further more fields, which are specific to the column type.

**Max number of Items :** Currently this feature is only available to a column of type `Completed`, to restrict from showing all your completed tasks. Its recommended not to show all your completed tasks on the board, if you have completed many tasks. Only show few tasks under this column, by entering the number here, how many tasks you want to see under this column, which will help you to render the board faster.

- In the future releases, there will be a new window to see all your completed tasks.

**Delete Icon :** Using these Icons, you can able to delete the specific Column from the board. This will only delete the column and wont affect any of your tasks. You can easily create the column back if you know the configuration of this column.

### Add Column Button

This button allows you to add more column to this board. Once you press on this button, a pop will appear as shown below :

![Add Column PopUp](/assets/AddColumnModal.png)

This pop-up will ask you to select the type of the new column and the name of this new column, which are the most important fields. Dont worry, you can change the name of the column later at any time. But the type of the Column will be fixed. If you want to change the type, you will have to create a new Column and delete the previous one.

## Delete This Board Button

This button will delete the current board. After you click on this button, a pop up will appear to ask you for Confirmation.

This operation is not reversible. Take care while delete the board. But its also easy to create a new board, if you remember the board structure. Don't worry!

{: .note }
> Deleting a board or changing any setting inside the board makes no changes to you tasks. You can only change the content of your tasks either from the Task Editor or using the delete button inside the Task Item Card.
