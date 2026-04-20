---
parent: How to Contribute
title: Test beta releases
nav_order: 3
---

## How to test beta release

{: .new-title }
> 2.0.0 Beta Release
>
> If you are testing the version 2.0.0-beta-1 release, the steps are slightly different. Hence, please refer the following wiki : [Test 2.0.0-beta-1 release](./Test_2.0.0_Beta_Release.md).

Beta releases are the versions released for testing and ensuring the plugin will work as expected after the main release. Beta version usually will have the name/tag as minor release version followed by a 'beta' name, followed by a number. Eg.: `1.5.0-beta-2`.

Whenever a new beta version has been released, you will get a notification for the same either through mail if you are watching this repository or in the Announcement section of the discussion.

{: .note }
> Points to remember while installing a beta versions : 
> - Use a dummy vault or sandbox vault. Since new changes might contain some bugs, there is a possibility of data loss. Hence never install a beta version of any plugin inside your main vaults.
> - Uninstall any version of previous Task Board you have installed in the vault you are doing the testing. If this is your fresh new vault, then no worries.
> - Preferably use the first method from below to do the testing, to avoid wasting time in creating a dummy vault, etc.

There are two methods to test a beta version : 

1. Download a pre-configured test vault. (This is a easy method)
2. Install the beta version using BRAT plugin.

### First Method : Download a test vault

- In every beta release you will find a zip file attached in the release notes. Which you can easily download, unzip and open inside Obsidian.
- For example, open the following link to see a zip file attached at the end for the release notes of the beta version `1.8.0-beta-4` : https://github.com/tu2-atmanand/Task-Board/releases/tag/1.8.0-beta-4.
- Simply download this zip file, then extract the folder from the zip file, then open that folder inside Obsidian. Now you can easily start testing this beta version.
- If you found any issue or bug, if its a small bug you can simply report the bug here : [create a new issue](https://github.com/tu2-atmanand/Task-Board/issues/new).
- But, if the developer wants more information to troubleshoot the issue, try to reproduce the issue inside this same test vault you are using. If you are able to reproduce the issue, simply zip this test vault folder back and send this zip to developer. Either in the same issue ticket or email it to [sanketgauns8@gmail.com](mainto:sanketgauns8@gmail.com).


### Second Method : Install the beta version using BRAT plugin.

**Step 1 :** Open the Dummy vault inside Obsidian.

**Step 2 :** Open the Settings Panel using the Gear Icon from the Side bar:
![Open Settings Panel](/assets/OpenSettingsPanel.png)

**Step 3 :** Click on the Community Plugins Tab from the Right Sidebar.
![alt text](/assets/CommunityBrowseButton.png)

**Step 4 :** Click on the Browser button from the pane.

**Step 5 :** Search for `BRAT` in the search bar.

**Step 6 :** Click on the plugin by `TFTHacker`.
![BRAT plugin](/assets/BRAT_Plugin_Install.png)

**Step 7 :** Click on **Install**.

**Step 8 :** After installing you will see a **Enable** button, click on it.

**Step 9 :** Navigate to the setting of BRAT plugin and open the tab as shown in below image :
![BRAT Plugin Settings](/assets/BRAT_plugin_settings.png)

**Step 10 :** Click on the **Add beta plugin** button. You will see a new modal as below : 
![BRAT_Add_New_Plugin](/assets/BRAT_Add_New_Plugin.png)

**Step 11 :** In the first input field enter the following url : `https://github.com/tu2-atmanand/Task-Board`. And then click anywhere else on the modal. You will get a green highlighting for the input field, indicating its a correct url.

**Step 12 :** Now you can select the any version of Task Board using the `"Select a version.."` drop-down menu. Select the latest beta version you want to start testing.

**Step 13 :** Simply click on the **Add plugin** button and wait for some time for the plugin to get installed.

**Step 14 :** The plugin is ready for using as usual. Try out all the new features in this version and report the bugs you will encounter. Also your suggestions are more than welcome for the enhancement of this plugin in any way.

**Thank you for you contribution!**

