---
title: Migrating to 2.x.x
nav_order: 13
---

# Migrating to Task Board 2.x.x series

Task Board is now migrating from `1.x.x` series to `2.x.x` series. This means, some of the features from the `1.x.x` series will not be supported in the new series, because of some architectural changes done within this plugin. These major changes has been done to solve the following issue found in this plugin : [task-board-github/ticket-561](https://github.com/tu2-atmanand/Task-Board/issues/561).

Task Board version `2.0.0` will going to be the first production ready version in this new series. But to test these new changes, we will be releasing few beta versions before we finally release the `2.0.0` version officially.

The testing phase will take some time, since we need a good amount of time to test all the things. Will release multiple beta versions during this testing phase, `2.0.0-beta-1`, `2.0.0-beta-2`, etc...

You can contribute in testing these beta version using the following wiki : [How to test 2.x.x beta versions](/docs/Advanced/How_To_Contribute/Test_2.0.0_Beta_Release.md).

Keep an eye on the Obsidian forum, Discord and [YouTube channel](https://www.youtube.com/@tu2_atmanand) to get the latest update when this new version will be released.

## What will happen in migration

When we are moving from **Task Board v1.x.x** to **Task Board v2.x.x**, this plugin needs to apply some migrations when you will update to the new version. Majorly, the following things will happen in the migration : 

- Right now all your boards are stored inside the configuration file inside the plugin config folder. All these boards will be moved inside your vault and each board will be saved as a single `.taskboard` file inside the following folder : `Meta/Task_Board/Boards/`.
  - For example, lets say you have the following five boards : 
    - **Project 1 - Time Based**
    - **Project 1 - Tag Based**
    - **Project 2 - Tag Based**
    - **Project 3 - Status Based**
    - **Daily Notes**
  - So your previous Task Board tab will look like this : 
  - ![All Boards before migration](/assets/allBoardsBeforeMigration.png)
  - After the migration, these boards will be stored like this : 
    - `Meta/Task_Board/Boards/Project 1 - Time Based.taskboard`
    - `Meta/Task_Board/Boards/Project 1 - Tag Based.taskboard`
    - `Meta/Task_Board/Boards/Project 2 - Tag Based.taskboard`
    - `Meta/Task_Board/Boards/Project 3 - Status Based.taskboard`
    - `Meta/Task_Board/Boards/Daily Notes.taskboard`
  - The new interface will look something like this : 
  - ![All Boards after migration](/assets/allBoardsAfterMigration.png)

- Inside each of the board file, there will be two views : 
  - **Kanban view :** The data for the Kanban view and few other config data specific to the board will be fetched from the `data.json` file and put inside the respective `.taskboard` file.
  - **Map view :** The map view data will be moved from an internal database called `LocalStorage` to the respective `.taskboard` file.

- But, what if all your Kanban views are related to the same project and you dont use the Map view feature that much?
  - In this case you can merge all the three boards into one and delete all the map views from that board. See [this section below](#i-want-to-combine-two-or-more-boards).

## How the migration will be applied

> The migrations will not going to be applied automatically. This plugin never runs anything without user permission. You will need to initiate the migration process as explained below...

As you can see, since the data from two different sources is brought into the single `.taskboard` file for every single board, there are few safety measures taken to have a smooth migration process.

Now, if you are at any version from the previous series `1.x.x`. For example, lets say you are at the version `1.10.1`. And you are now updating this plugin to the version `2.0.1`. After the plugin has been updated, you will see a notice with a button, as shown below :  

![Migration notice after plugin update](/assets/migrationNotice.png)

When you will click on the **"Open migration modal"** button a new modal will be opened as shown below : 

![Migration modal](/assets/migrationModal.png)

You can also open this migration modal from the settings, incase if the notice do not appears after the plugin update.

In this modal, when you will click on the **Run migrations** button, few actions will be executed step-by-step automatically.

Here is how the migration will be applied, step-by-step : 

1. **Backup config file** : The current config file backup will be saved at the root of your vault. This is done so that, later, if there was some error occurred during the migration process or if you feel you dont want to move to the new Task Board series, you can easily [revert back to the previous version](#how-to-revert-back-to-the-previous-version). Otherwise, you can delete the backup config file later.

2. **Create board file** : Each of your board will be converted into a corresponding `.taskboard` file and will be saved at the following path : `Meta/Task_Board/Boards/` (as explained above).

3. **Moving map view data** : Now, the map view data for each board is stored inside a separate location called `LocalStorage`, which is like a database inside Obsidian application. It is not 100% assured that your map-view data for the specific board will be properly moved to the respective `.taskboard` file, This is because, there are possibilities that the data from the `LocalStorage` database might have got lost or erased when the plugin was updating. But, this migration code will do its best to move the data which is present in that database. The worst thing which will happen is that, the task card positions on the map will be misplaced, which you can then move to their correct positions, the connections and everything will be preserved as it is.

4. **Update plugin settings file** : Since, in this new version, all the board configurations are moved to their individual board files, now, the plugin config file (`data.json`) file will be very optimal and will only contain the global plugin settings data. 

5. **Restart Obsidian** : You dont have to do anything during the migration. But after the migration is completed, you will see the complete logs. And at the bottom how many boards has been successfully migrated out of the total boards you have. A notice will be shown to reload Obsidian. If you dont get the notice, there will be also a button at the bottom inside this migration modal. See below image : 

![Migration modal after migration is completed](/assets/migrationModalComplete.png)

After the reload, the new version of Task Board should be ready with an enhanced architecture.

**Additionally** : 
1. The migration logs will be saved inside a log file in the plugin config folder, for debugging purposes, incase anything goes wrong.





## I want to merge two or more boards

Now, there will be often a situation where you would like to combine two or more of your Kanban views inside a single board file. For example, even though this plugin always encourages its users to create a single board for every project, thats not always possible. Sometimes, we need to have multiple Kanban views to manage a single project. This was not possible in the Task Board 1.x.x series, but its now possible by creating multiple Kanban views inside the same board file.

In the previous version of Task Board, you were creating boards and inside each of those boards, there were only two fixed views : **Kanban view** and **Map view**. So, during this migration, basically, these two views are stored inside the board file.


Now, once your boards have been migrated and stored as `.taskboard` files, you can later merge two boards to combine all the views from the two boards inside a single board file. And later delete those two earlier board files.

For example, in the images shown above, you may see that, there are two Kanban views created for the same **Project 1** : 
- **Project 1 - Time Based**
- **Project 1 - Tag Based**

Since, both these boards are for managing the same project, hence you can combine both the board files into a single board file and delete the older two board files.


## How to revert back to the previous version

{: .warning }
> There are the following two things you should remember : 
>
> 1. There is a possibility that, your map view data might get completely lost when you will revert back to this previous version. As you might have read in the GitHub ticket shared above. This is a major flaw in the previous series of this plugin. Hence, if you are heavily dependent on the Map view feature, you should migrate to the `2.x.x` series.
>
> 2. Please note that, the previous Task Board version series, `1.x.x`, will reach its end of life, 2 months after the release of the version `2.0.0`. No, further improvements, bug-fixes or features will be provided for the previous version series of this plugin, after its end of life. Hence, its highly recommended to be on the latest version of this plugin.


{: .note }
> Please use the below steps only if there was an issue during the migration and migration broke the plugin. The below steps will fix it and get you back to where you were. You can remain on the previous version of this plugin, until the migration issue you are facing has been fixed.
> 
> In a worst case scenario, if there were any issues during the migration process or if you feel that, you want to be on the previous version of this plugin, then you can easily revert back to the previous version by following the below steps.

Please follow the below steps to easily revert back to the previous version : 

**Step 1** : Uninstall the Task Board version you have just now updated.

**Step 2** : Install a new plugin called [BRAT](https://github.com/TfTHacker/obsidian42-brat) from the community marketplace, how you normally install any plugin. This is a special plugin which helps you to selectively install a specific version of any plugin, which Obsidian do not provides in-built. Through this plugin we will proceed to only install the latest version from the `1.x.x` series. (At the time of writing this documentation, the latest version of `1.x.x` series is `1.10.2`)

**Step 3** : After you have installed the BRAT plugin, open its settings. You will find a button called **Add beta plugin**, click on this button.

**Step 4** : Then enter the following link in the Repository text field : `https://github.com/tu2-atmanand/Task-Board/`.

**Step 5** : Wait of few seconds for the BRAT plugin to verify the link. Once it has fetched all the latest versions of the Task Board plugin, you will be able to see the list of versions in the drop-down. Select the latest version of the `1.x.x` series. (Mostly it will be `1.10.2`).

{: .note }
> Do not select the **latest** option here, because the latest version of Task Board will be from the `2.x.x` series. But you should select the latest version from the `1.x.x` series, because you are trying to revert back to the previous version of the Task Board.


**Step 6** : Once you have selected the version, click on the **Add plugin** button, which will install that specific version of the Task Board.


This image shows all the logs from **Step 3** to **Step 6**.


**Step 7** : Now, open the settings of Task Board plugin. And navigate to the setting called **"Import/Export configurations"** under the **General** tab.

**Step 8** : Click on the **Import** button and select the backup configuration file which Task Board generated during the first step of the migration process. It will be present at the root of your vault folder. It will be with the name `taskboard-configs-yyyy_dd_mm.json`. (Where `yyyy_dd_mm` will be the date)

**Step 9** : After Task Board has successfully imported all your previous configurations, you are all good to start using the previous version where you left off.
