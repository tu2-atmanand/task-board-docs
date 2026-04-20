---
parent: How to Contribute
title: Contribute to Language Translation
nav_order: 2
---

# Contribute to Language Translation

This plugin supports below languages. You can help us improve the current language content or add more languages by following this doc.

Task Board has a unique functionality wherein, users can directly update the interface strings from the translation file and reload obsidian to see the changes right away. Read more here : [How to update existing language](#how-to-update-existing-language-content).


## Supported Languages Status

| Language code  | Language name         | Native name         | Status |
| -------------- | --------------------- | ------------------- | :----: |
| `en` (default) | English               | English             |   ✅    |
| `af`           | Afrikaans             | Afrikaans           |   🚧   |
| `am`           | Amharic               | አማርኛ                |   🚧   |
| `ar`           | Arabic                | العربية             |   🚧   |
| `eu`           | Basque                | Euskara             |   🚧   |
| `be`           | Belarusian            | беларуская мова     |   🚧   |
| `bg`           | Bulgarian             | български език      |   🚧   |
| `bn`           | Bengali               | বাংলা               |   🚧   |
| `ca`           | Catalan               | català              |   🚧   |
| `cs`           | Czech                 | čeština             |   🤖    |
| `da`           | Danish                | Dansk               |   🤖    |
| `de`           | German                | Deutsch             |   ✅    |
| `dv`           | Dhivehi               | ދިވެހި              |   🚧   |
| `el`           | Greek                 | Ελληνικά            |   🚧   |
| `en-GB`        | English (GB)          | English (GB)        |   🚧   |
| `eo`           | Esperanto             | Esperanto           |   🚧   |
| `es`           | Spanish               | Español             |   🤖    |
| `fa`           | Persian               | فارسی               |   🚧   |
| `fi-fi`        | Finnish               | suomi               |   🚧   |
| `fr`           | French                | français            |   ✅    |
| `gl`           | Galician              | Galego              |   🚧   |
| `he`           | Hebrew                | עברית 🇮🇱          |   🚧   |
| `hi`           | Hindi                 | हिन्दी              |   ✅    |
| `hu`           | Hungarian             | Magyar nyelv        |   🚧   |
| `id`           | Indonesian            | Bahasa Indonesia    |   🤖    |
| `it`           | Italian               | Italiano            |   🤖    |
| `ja`           | Japanese              | 日本語                 |   🤖    |
| `ko`           | Korean                | 한국어                 |   🤖    |
| `lv`           | Latvian               | Latviešu valoda     |   🚧   |
| `ml`           | Malayalam             | മലയാളം              |   🚧   |
| `ms`           | Malay                 | Bahasa Melayu       |   🚧   |
| `ne`           | Nepali                | नेपाली              |   🚧   |
| `nl`           | Dutch                 | Nederlands          |   🤖    |
| `no`           | Norwegian             | Norsk               |   🤖    |
| `oc`           | Occitan               | Occitan             |   🚧   |
| `pl`           | Polish                | język polski        |   🤖    |
| `pt`           | Portuguese            | Português           |   🤖    |
| `pt-BR`        | Brazilian Portuguese  | Portugues do Brasil |   🤖    |
| `ro`           | Romanian              | Română              |   🤖    |
| `ru`           | Russian               | Русский             |   ✅    |
| `sa`           | Sanskrit              | संस्कृतम्           |   🚧   |
| `sr`           | Serbian               | српски језик        |   🚧   |
| `se`           | Swedish               | Svenska             |   🚧   |
| `sk`           | Slovak                | Slovenčina          |   🚧   |
| `sq`           | Albanian              | Shqip               |   🤖    |
| `ta`           | Tamil                 | தமிழ்               |   🚧   |
| `te`           | Telugu                | తెలుగు              |   🚧   |
| `th`           | Thai                  | ไทย                 |   🚧   |
| `tl`           | Filipino (Tagalog)    | Tagalog             |   🚧   |
| `tr`           | Turkish               | Türkçe              |   🤖    |
| `uk`           | Ukrainian             | Українська          |   🤖    |
| `ur`           | Urdu                  | اردو                |   🚧   |
| `vi`           | Vietnamese            | Tiếng Việt          |   🚧   |
| `zh`           | Chinese (Simplified)  | 简体中文                |   🤖    |
| `zh-TW`        | Chinese (Traditional) | 繁體中文                |   ✅    |

{: .new-title }
> LEGENDS
> ✅ : Means the language has been properly integrated and human reviewed.
>
> 🤖 : Means the language is machine generated and haven't been human reviewed yet.
> 
> 🚧 : Means the language is either haven't been integrated, or is under development.


{: .new-title }
> NOTE
>
> This table might not always show the latest status about the translation languages and even the ✅ marked languages might be missing some translations when new version are released.


## How to Update existing Language content

> This is a very straight forward method.

**STEP 1** : If you have already downloaded your language translation file using following setting, then move on to the next step : [Update language translations](/docs/Settings/General.md#update-language-translations)

**STEP 2** : Go inside the plugin's language config folder using your system file explorer. Usually the config folder will be inside `.obsidian/plugin/task-board/locales`. This `.obsidian` hidden folder will be present inside your vault folder (you might need to enable some option in your system file explorer to see this folder). Now open the file with your language code in any text editor.
For example, if you language is Czech, then find your language code from the above table. In this example the code is '**cs**', hence the file name will be `cs.json`.

**STEP 3** : Now whichever string you want to edit, find that string and simply edit it.

**STEP 4** : If, the string you want to edit is not present inside the file, open the following link which has the corresponding english strings : [English translation strings](https://github.com/tu2-atmanand/Task-Board/blob/main/src/utils/lang/locale/en.json)

**STEP 5** : Now find the string which you want to add, then copy its corresponding id.
For example, if the string you want to edit is "Add sub task". Then you may see its corresponding id is "add-sub-task".

**STEP 6** : Pase this id in your language file. On the right of this id after the colon symbol (:), you can add your language suitable string.

**STEP 7** : Save this file and reload Obsidian using the command "Reload without saving" and your changes will be applied automatically.

After you have completed with all the required changes, you may submit this file to contribute to the development of this plugin.

---

## How to add a new Language

**STEP 1** : If you have received the message through bug report modal that the language translation file for the selected language is not present, then you will need to create a new file for the same.

**STEP 2** : Go inside the plugin's language config folder using your system file explorer. Usually the config folder will be inside `.obsidian/plugin/task-board/locales`. 

**STEP 3** : Inside this folder create a new file with your language code using any text editor and the extension of this file should be `.json`.
For example, if you language is Czech, then find your language code from the above table. In this example the code is 'cs', hence the file name will be `cs.json`.

**STEP 4** : Open the following link and copy the whole content and paste it inside the new file which you have just created. : [English translation strings](https://github.com/tu2-atmanand/Task-Board/blob/main/src/utils/lang/locale/en.json)
(You can find a button in the header of on left which will say 'Copy raw file')

**STEP 5** : Now you can start replacing the english strings with your language strings.
For example, if the string you want to edit is "Add sub task". Then you may see its corresponding id is "add-sub-task". So, you should not touch the id, and replace its corresponding string only. In this example, *"Add sub task"* will be replaced with *"Přidejte dílčí úkol"*.

**STEP 6** : Save this file and reload Obsidian using the command "Reload without saving" and your changes will be applied automatically.

## How to Submit your file

- After you have completed translation of all the strings properly, submit the file either using pull request to the Github project or directly send the file by creating a GitHub request here : [How to Create an Request](/docs/Advanced/How_To_Create_Request.md).
