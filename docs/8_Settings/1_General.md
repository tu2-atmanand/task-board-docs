---
parent: Plugin Settings
title: General
nav_order: 1
---

# General Settings

The General tab contains miscellaneous settings that control core plugin behavior and scanning functionality. These are global settings applied to the entire plugin.

## Filters for Scanning

This section allows you to apply multiple types of filters to control which files and tasks are scanned from your vault:

- **Frontmatter Filters**: Filter tasks by frontmatter tags (scan only files with specific frontmatter)
- **File Filters**: Include or exclude specific files from scanning
- **Folder Filters**: Include or exclude entire folders from scanning
- **Tag Filters**: Include or exclude tasks with specific tags

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

## Default Note for Adding New Tasks

| Input Field | Default |
|---|---|
| File Picker | (Select a file) |

Specify the default markdown file where new tasks created via the "Add New Task" modal will be saved.

## Tasks Cache File Path

| Input Field | Default |
|---|---|
| File Path Input | `.obsidian/plugins/task-board/tasks.json` |

This setting allows you to customize where the plugin stores its tasks cache file. The cache improves performance by storing task metadata and retrieve it faster from a single location. Its easy to rebuild this case, incase it gets corrupted using the [vault scanner feature](/docs/6_Features/9_Vault_Scanner.md).


## Open Board on Obsidian Startup

| Input Field | Default |
|---|---|
| Toggle | OFF |

When enabled, Task Board opens automatically when you launch Obsidian. The last viewed board will be brought to focus.

## Show Modified Files Message on Startup

| Input Field | Default |
|---|---|
| Toggle | ON |

When enabled, the plugin displays a notice showing which files were modified during the previous session when Obsidian starts.


## Update language translations

| Input Field | Default |
|---|---|
| Dropdown | (Based on Obsidian language) |

Select the language for the Task Board plugin UI. To contribute translations or improve existing ones, see: [How to Contribute to Translations](../10_Advanced/3_How_To_Contribute/2_HowToContributeToTranslations.md)

## Import/Export configurations


## Export logs


## Safe Guard Feature

| Input Field | Default |
|---|---|
| Toggle | ON |

When enabled, the Safe Guard feature provides additional protections to prevent accidental data loss. See [Safe Guard](../6_Features/14_Safe_Guard.md) for more details.


## Experimental Features

| Input Field | Default |
|---|---|
| Toggle | OFF |

Enables access to experimental/beta features if there are any released in the present version. These features are still under development and may have limitations/bugs/issues. The description will list all the features which are present as experimental features.



## Donation Section

This section contains links to support the plugin development through various sponsorship platforms. If you find Task Board valuable, please consider supporting the project!
