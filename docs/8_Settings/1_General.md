---
parent: Plugin Settings
title: General
nav_order: 1
---

# General settings

### Filters for Scanning

This section contains three different types of filters you can apply while your vault is getting scanned for tasks. The first two filters are for scanning files and all the files inside the folder. The third filter is to scan task which contains any one fo the tag you have mentioned in the input field.

If you are using only one of this filter at a time and keeping the other two disabled, then its very simple to understand, but if you are using combinations of all the filters, then a proper understanding is required to understand how to use them or how it works. To understand all this things and also how to enter the values. please read this section carefully : [Filters for Scanning](../Features/Filters_for_Scanning.md)

### Scanning modes


| Input Field | Dropdown Options                                                                                                                     | Default Value           |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| Dropdown    | Balanced<br>Real-time<br>Manual | Balanced |


This setting helps you to select what type of scanning mode you would like this plugin to use for scanning your latest changes in your note. Using the first two options, you get the power of [automatic scanning feature](../5_Features/11_Auto_Scanning_Files.md).

### Default note for adding new tasks

### File for archived tasks

### Tasks cache file path


### Open board on Obsidian startup

| Input Field   | Default Value |
|---------------|---------------|
| Toggle Button | OFF            |

This setting will help you to get your Task Board visible to you on Obsidian startup. When you open and close Obsidian, if you want Task Board to be the first thing visible inside the Obsidian, you can enable this feature.

### Auto-scan the vault on Obsidian start-up

| Input Field   | Default Value |
|---------------|---------------|
| Toggle Button | OFF           |

This option will help you to decide whether you want to scan all your files or filtered files every time when the Obsidian starts. The Vault-Scanning feature can be understood from here : [Vault-Scanning](../Features/Scan_Vault_Feature.md).

This can be a beneficial feature for those who edit their files outside of Obsidian, so when Obsidian opens, Task Board is unaware that the tasks has been updated from various files, in this case you will be required to run the [Scan Vault](../Features/Scan_Vault_Feature.md) feature manually, so you can set this option to ON, to scan all the files automatically whenever Obsidian starts.

{: .warning } 
>Do not enable this feature if you vault is very big and contains lot of large files with lot of data. This feature will work the best if you have set the file and folder [Scanning Filters](../Features/Filters_for_Scanning.md).


### Update language translation

| Input Field   | Default Value |
|---------------|---------------|
| Click Button | NA           |

You may see this is a simple click button. This button simply downloads the latest language translation file for your selected language in Obsidian general setting and place it inside the plugin's config folder. Even you can edit this file to make instant changes. Read this : [Update language translation strings](../Advanced/Contribution_For_Languages.md#how-to-update-existing-language-content)

> Note : Obsidian reload is required after downloading the new updates. You can use the "Reload without saving command".


## Donation Section

This section contains button-links to my various sponsorship sites. If you have like this plugin and would like to support the further development of this idea and to improve it, consider supporting my work by sponsoring this project using any site you want.
