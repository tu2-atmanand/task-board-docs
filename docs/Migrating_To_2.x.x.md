---
title: Migrating to 2.x.x
nav_order: 13
---

# Migrating to Task Board 2.x.x series

Task Board is now migrating from `1.x.x` version series to `2.x.x` version series. This means, some of the features from the `1.x.x` versions will not be supported in the new series, because of some architectural changes done within this plugin. These major changes has been done to this plugin because of the following issue found in Task Board : [tu2-atmanand/ticket-561](https://github.com/tu2-atmanand/Task-Board/issues/561).

Task Board version `2.0.0` will going to be the first production ready version in this new series. But to test these new changes, we will be releasing few beta versions before we finally release the `2.0.0` version officially.

The testing phase will take some time, since we need a good amount of time to test all the things. Will release multiple beta version during this testing phase, `2.0.0-beta-1`, `2.0.0-beta-2`, etc...

You can contribute in testing these beta version using the following wiki : [How to test 2.x.x beta versions](/docs/Advanced/How_To_Contribute/Test_2.0.0_Beta_Release.md).

Keep an eye on the Obsidian forum, Discord and [YouTube channel](https://www.youtube.com/@tu2_atmanand) to get the latest update when this new version will be released.

## What will happen in migration

When we are moving from **Task Board v1.x.x** to **Task Board v2.x.x**, this plugin has some migration code which it will run when you will install/update the new version. Majorly, the following things will happen in the migration : 

- Right now all your boards are stored inside the configuration file inside the plugin config folder. All these boards will be moved inside your vault and each board will be saved as a single `.taskboard` file mostly inside the following folder : `Meta/Task_Board/Boards/`.
  - For example, lets say you have the following three boards : **Time based workflow**, **Tag based workflow**, **Status based workflow**.
  - After the migration, these boards will be stored like this : 
    - `Meta/Task_Board/Boards/Time based workflow.taskboard`
    - `Meta/Task_Board/Boards/Tag based workflow.taskboard`
    - `Meta/Task_Board/Boards/Status based workflow.taskboard`

- Inside each of the board file, there will be two views : 
  - **Kanban view :** The data for the Kanban view and few other config data specific to the board will be moved from the config file to the respective `.taskboard` file.
  - **Map view :** The map view data will be moved from an internal database called `LocalStorage` database to the respective `.taskboard` file.


## How the migration will be applied

As you can see, since the data from two different sources are brought into the single `.taskboard` file for the respective boards, there are few safe measures taken to avoid a smooth migration process.

Now, if you are at any version from the previous series `1.x.x`. For example, lets say you are at the version `1.10.1`. And you are now updating this plugin to the version `2.0.1`. After the plugin has been updated, you will be presented with a notice and a button, when you will click on this button a new modal will be opened as shown below : 



You can also open this migration modal from the settings.

In this modal, when you will click on the **Start migration**, button few actions will be executed step-by-step automatically and you dont have to worry about any of them.

Here is how the migration will be applied, step-by-step : 

1. **Backup config file** : The current config file backup will be saved at the root of your vault. This is done so that, later, if there was some error occurred during the migration process or if you feel you dont want to move to the new Task Board series, you can easily [revert back to the previous version](#how-to-revert-back-to-the-previous-version). Otherwise, you can delete the backup config file later.
2. **Create board file** : Each of your board will be converted into a corresponding `.taskboard` file and will be saved at the following path : `Meta/Task_Board/Boards/` (as explained above).
3. **Moving map view data** : Now, the map view data for each board is stored inside a separate location called `LocalStorage`, which is like a database inside Obsidian application. It is not 100% assured that your map-view data for the specific board will be properly moved to the respective `.taskboard` file, This is because, there are possibilities that the data from the `LocalStorage` database might have got lost or erased when the plugin was updating. But, this migration code will do its best to move the data which is present in that database. The worst thing which will happen is that, the task card positions on the map will be misplaced, which you can then move the their correct positions, the connections and everything will be preserved as it is.
4. **Restart Obsidian** : After the above migration steps has been successfully applied, you will be asked to reload the Obsidian. After the reload, the new version of Task Board should be ready with an enhanced architecture.


## How to revert back to the previous version

{: .warning }
> There are the following two things you should remember : 
>
> 1. There is a possibility that, your map view data might be completely lost when you will revert back to this previous version. As you might have read in the GitHub ticket shared above, this is a major flaw in this plugin in the `1.x.x` series. Hence, if you are heavily dependent on the Map view feature, you should migrate to the latest version of this plugin, that is the latest version of `2.x.x` series.
>
> 2. Please note that, the previous Task Board version series, `1.x.x`, will reach its end of life, 2 months after the release of the first official version of `2.0.0`. No, further improvements, bug-fixes or features will be provided for the previous version series of this plugin, after its end of life. Hence, its always recommended to be on the latest version of this plugin.
>
> Please use the below steps only if there was an issue during the migration and migration broke the plugin. The below steps will fix it. You can remain on the previous version of this plugin, until the migration issue you are facing has been fixed.

In a worst case scenario, if there were any issues during the migration process or if you feel that, you want to be in the previous version of this plugin, then you can easily migration to the previous version without any issues.

Please follow the below steps to easily revert back to the previous version : 

**Step 1** : Uninstall the Task Board version you have just now updated.

**Step 2** : Install a new plugin called [BRAT](https://github.com/TfTHacker/obsidian42-brat) from the community marketplace, how you normally install any plugin. This is a special plugin which helps you to selectively install a specific version of any plugin, which Obsidian do not provides in-built. Through this plugin we will proceed to only install the latest version from the `1.x.x` series. (At the time of writing this documentation, the latest version of `1.x.x` series is `1.10.2`)

**Step 3** : After you have installed the BRAT plugin, open its settings. You will find a button called **Add beta plugin**, click on this button.

**Step 4** : Then enter the following link in the Repository text field : `https://github.com/tu2-atmanand/Task-Board/`.

**Step 5** : Wait of few seconds for the BRAT plugin to verify the link. Once it has fetched all the latest versions of the Task Board plugin, you will be able to see the list of versions in the drop-down. Select the latest version of the `1.x.x` series. (Mostly it will be `1.10.2`).

{: .note }
> Do not select the **latest** option here, because the latest version of Task Board will be from the `2.x.x` series. But you should select the latest version from the `1.x.x` series, because you are trying to revert back to the previous version of the Task Board.


**Step 6** : Once you have selected the version, click on the **Add plugin** button, which will install that specific version of the Task Board.


This image shows all the steps from **Step 3** to **Step 6**.


**Step 7** : Now, open the settings of Task Board plugin. And navigate to the setting called **"Import/Export configurations"** under the **General** tab.

**Step 8** : Click on the **Import** button and select the backup configuration file which Task Board generated during the first step of the migration process. It will be present at the root of your vault folder. It will be with the name `taskboard-configs-yyyy_dd_mm.json`. (Where `yyyy_dd_mm` will be the date)

**Step 9** : After Task Board has successfully imported all your previous configurations, you are all good to start using the previous version where you left off.
