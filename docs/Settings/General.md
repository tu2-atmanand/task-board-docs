---
parent: Plugin Settings
title: General
nav_order: 1
---

# General Tab

The General tab contains miscellaneous settings that control core plugin behavior and scanning functionality. These are global settings applied to the entire plugin.

## Filters for Scanning

This setting allows you to apply multiple types of filters to control which files and tasks are scanned from your vault. These filters will restrict Task Board from even reading the notes, if say, for example, you have added the notes in the below "File filters" and have set the polarity to "Dont scan this".

We have four types of filters :

- **Tag Filters**: Include or exclude tasks with specific tags
- **Frontmatter Filters**: Filter tasks by frontmatter tags (scan only files with specific frontmatter)
- **File Filters**: Include or exclude specific files from scanning
- **Folder Filters**: Include or exclude entire folders from scanning

You can use one filter independently or combine multiple filters together. For detailed information on how filters work together, see: [Filters for Scanning](../6_Features/10_Filters_for_Scanning.md)

{: .note }
> After making significant changes to scan filters, use the "Scan Vault" feature to re-scan your vault with the new filters applied.

## Scanning Mode

| Input Field | Options | Default |
|---|---|---|
| Dropdown | **Balanced** - Scans modified files when you finish editing and switch tabs/windows<br>**Real-Time** - Live updates with ~1 second delay (slight performance impact)<br>**Manual** - Requires manual refresh via button | Balanced |

Select how frequently Task Board scans your vault for changes. The Balanced and Real-Time modes provide [automatic scanning](../6_Features/11_Auto_Scanning_Files.md) capabilities.

## Auto Add Unique ID

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, the plugin automatically assigns incremental numeric IDs to tasks as you interact with them. This is especially useful for:
- **Map View Feature** - Tasks require unique IDs to appear on the dependency map canvas
- **Future Features** - Manual sorting and task pinning in upcoming versions


## Tasks Cache File Path

| Input Field | Default |
|---|---|
| File Path Input | `.obsidian/plugins/task-board/tasks.json` |

This setting allows you to customize where the plugin stores its tasks cache file. The cache improves performance by storing task metadata and retrieve it faster from a single location. Its easy to rebuild this cache, incase it gets corrupted using the [vault scanner feature](/docs/6_Features/9_Vault_Scanner.md).

Using this setting you can store the cache within your vault, incase if you want to sync it across devices. This will show real-time changes on the board when its opened on two devices at the same time and if the cache file is synching in real-time.


## Open Board on Obsidian Startup

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, Task Board opens automatically when you launch Obsidian. The last viewed board will be brought to focus.

## Show Modified Files Message on Startup

| Input Field | Default |
|---|---|
| Toggle | ON |

When enabled, the plugin displays a notice showing which files were modified when the Obsidian was closed and in its absence if other external applications or services have updated any vault files.

If you want Task Board to scan the modified files automatically without showing you the message every time you start Obsidian. You can disable this setting.


## Update language translations

| Input Field | Default |
|---|---|
| 1 Button | NA |

This settings contains a single button, called **Update**. Task Board supports some of the languages which are supported by Obsidian. The default language of this plugin will be english when you going to install it. If your Obsidian language is other than english, simply click on this update button and the latest language translations for your language will be downloaded from GitHub. Following are the languages supported by Task Board : [Languages translation status](/docs/10_Advanced/3_How_To_Contribute/2_HowToContributeToTranslations.md#supported-languages-status).

To contribute translations or improve existing ones, see: [How to Contribute to Translations](../10_Advanced/3_How_To_Contribute/2_HowToContributeToTranslations.md)

## Import/Export configurations

| Input Field | Default |
|---|---|
| 2 Buttons | NA |

In this setting you will find two buttons : 
- **Export :** Using this button you can export the current Task Board plugin's configurations, incase you want to take a backup. Very useful, when you are trying to debug any issue within the plugin(like uninstall and install the plugin) and want to keep the current configs same, so you can import them again later. Also, useful, if you want to share your configurations with others, like sharing to the developer while reporting a bug.
- **Import :** Using this button you can import any previously exported Task Board configurations.

When you will click on the button a file selector will open to let you choose where you want to export the configuration file. And incase if importing, which file you want to import.

## Export logs

| Input Field | Default |
|---|---|
| 1 Button | NA |

Using this setting you can easily export the logs captured within this plugin. For more information on how this plugin captures logs, please refer the following wiki : [Bug reporter](/docs/6_Features/20_Bug_Reporter.md).


## Safe Guard Feature

| Input Field | Default |
|---|---|
| Toggle | ON |

When enabled, the Safe Guard feature provides additional protections to prevent accidental data loss. See [Safe Guard feature](../6_Features/14_Safe_Guard.md) for more details.


## Experimental Features

| Input Field | Default |
|---|---|
| Toggle | OFF |

Enables access to experimental/beta features if there are any released in the present version. These features are still under development and may have limitations/bugs/issues. The description of this setting will list all the features which are present as experimental features in your current Task Board version.


## Donation Section

This section contains links to support the plugin development through various sponsorship platforms. If you find Task Board valuable, please consider supporting the project!
