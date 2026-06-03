---
parent: Advanced Filter
title: Column Level
nav_order: 5
---

# Filters Warehouse

With the advancement of the Filters feature, we can now create a lot of [quick filters](/docs/Components/Advanced_Filter_Menu_v2.md#quick-filter) easily. But, we will find ourselves in a situation where we have created a complex quick filter and we want to apply it to the other boards or views within either the same board or different board.

Re-creating the same filter from scratch will be very painful. The best solution to handle this is to be able to share the specific filter with other boards.

Hence, this Filter warehouse feature helps you to exactly do that.

The **Filters Warehouse** is stored inside the plugin configuration. Which means, it will present at the vault-level. So any board inside your vault can use the filters which you have saved inside the warehouse.

## How to share/store any quick filter in warehouse?

To do this, simply open the [Advanced filter menu](/docs/Components/Advanced_Filter_Menu_v2.md) of the entity from which you want to share the quick filter with other entities. Now click on the three dots icon for the specific quick filter and click on the option "Save in warehouse".

Once the quick filter has been successfully stored inside the warehouse, you should see message that the filter has been stored successfully.

To confirm this, you can also open the [Filters warehouse modal](/docs/Components/Filters_Warehouse.md) using the button "**Import filter**" which you will see at the bottom right corner inside the Advanced filter menu you are in.

In this Filters warehouse modal you can also edit the saved filters.


## Share saved filters in another vault

Now, we can implement a feature wherein you can export all/selected filters from the warehouse of one vault and import those filters inside another vault.

But, this will be more development burden and we can simply achieve this an easier way.

Here is a hack I have...


**Step 1 :** Create a dummy board.
**Step 2 :** Open the board and open either the board-level or view-level advanced filter menu.
Import all the quick filters from the warehouse inside this board.
Move this dummy board file (`.taskboard`) inside the different vault where you want to import the filers.
Open that second vault inside Obsidian and open this dummy board inside inside that new vault.
Now, you can store/save all the quick filter from this dummy board inside the warehouse of the second vault.
I know, the only pain here will be, if you have a lot of filters, like 50 (Not sure if you should have that many), then you will need to click on each quick filter from the dummy board and save it inside the warehouse.

But for now, this workaround will do the job. And in the future will think of a solution to implement it as a feature is its really required.

{: .note }
> For this workaround to work, the Task Board plugin in both the vaults should be on the same version.