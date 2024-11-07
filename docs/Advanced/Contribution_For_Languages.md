---
parent: Advanced Topics
title: Contribute to Language Translation
---

# Contribute to Language Translation

This plugin supports following languages. You can help us improve the current language content or add more language by following this doc :

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
| `cs`           | Czech                 | čeština             |   ✅    |
| `da`           | Danish                | Dansk               |   ✅    |
| `de`           | German                | Deutsch             |   ✅    |
| `dv`           | Dhivehi               | ދިވެހި              |   🚧   |
| `el`           | Greek                 | Ελληνικά            |   🚧   |
| `en-GB`        | English (GB)          | English (GB)        |   🚧   |
| `eo`           | Esperanto             | Esperanto           |   🚧   |
| `es`           | Spanish               | Español             |   ✅    |
| `fa`           | Persian               | فارسی               |   🚧   |
| `fi-fi`        | Finnish               | suomi               |   🚧   |
| `fr`           | French                | français            |   ✅    |
| `gl`           | Galician              | Galego              |   🚧   |
| `he`           | Hebrew                | עברית 🇮🇱          |   🚧   |
| `hi`           | Hindi                 | हिन्दी              |   ✅    |
| `hu`           | Hungarian             | Magyar nyelv        |   🚧   |
| `id`           | Indonesian            | Bahasa Indonesia    |   ✅    |
| `it`           | Italian               | Italiano            |   ✅    |
| `ja`           | Japanese              | 日本語                 |   ✅    |
| `ko`           | Korean                | 한국어                 |   ✅    |
| `lv`           | Latvian               | Latviešu valoda     |   🚧   |
| `ml`           | Malayalam             | മലയാളം              |   🚧   |
| `ms`           | Malay                 | Bahasa Melayu       |   🚧   |
| `ne`           | Nepali                | नेपाली              |   🚧   |
| `nl`           | Dutch                 | Nederlands          |   ✅    |
| `no`           | Norwegian             | Norsk               |   ✅    |
| `oc`           | Occitan               | Occitan             |   🚧   |
| `pl`           | Polish                | język polski        |   ✅    |
| `pt`           | Portuguese            | Português           |   ✅    |
| `pt-BR`        | Brazilian Portuguese  | Portugues do Brasil |   ✅    |
| `ro`           | Romanian              | Română              |   ✅    |
| `ru`           | Russian               | Русский             |   ✅    |
| `sa`           | Sanskrit              | संस्कृतम्           |   🚧   |
| `sr`           | Serbian               | српски језик        |   🚧   |
| `se`           | Swedish               | Svenska             |   🚧   |
| `sk`           | Slovak                | Slovenčina          |   🚧   |
| `sq`           | Albanian              | Shqip               |   ✅    |
| `ta`           | Tamil                 | தமிழ்               |   🚧   |
| `te`           | Telugu                | తెలుగు              |   🚧   |
| `th`           | Thai                  | ไทย                 |   🚧   |
| `tl`           | Filipino (Tagalog)    | Tagalog             |   🚧   |
| `tr`           | Turkish               | Türkçe              |   ✅    |
| `uk`           | Ukrainian             | Українська          |   ✅    |
| `ur`           | Urdu                  | اردو                |   🚧   |
| `vi`           | Vietnamese            | Tiếng Việt          |   🚧   |
| `zh`           | Chinese (Simplified)  | 简体中文                |   ✅    |
| `zh-TW`        | Chinese (Traditional) | 繁體中文                |   ✅    |

{: .note }
✅ : Means the language has been properly integrated.
🚧 : Means the language is either haven't been integrated or is under development.

## How to Update existing Language content

### Manually

- This is a very straight forward method.

- Find the language file which you want to update.
For example, if you language is Czech, then find your language code from this link. In this example the code is 'cs', hence the file name will be `cs.ts`.

- Open this file and find the old string which you want to update.

- Now, simply update the whole string with new content. You can either use online services, but will recommend translating it on your own for better understanding of the content for others.

### Using Automation Script

When you will change any one string from the main en.ts file. Run the script and give all the lines number as argument to the script, which will change the line in all the other language files.

---

## How to add a new Language

### Manually

- Create a new file with the name of your language code and the extension will be '.ts'.
For example, if you language is Czech, then find your language code from this link. In this example the code is 'cs', hence the file name will be `cs.ts`.

- Now open the file you have just created and create the following structure first before adding your code (preferably use a better coding editor) :

```
const cs = {

};

export default cs;
```

> NOTE : For you the cs part will be different, it will be your Language code.

- Open this file in another tab for your reference : en.ts

- Now, simply replace the english line with your specific language line. You can use online translation tools to translate the language. But it will be preferred if you translate the lines in your own words for better understanding of the content.

### Using Automation Script

- Copy the en.ts into another temporary folder.

- Now, create the new language file you want to add, this files name will be the language code and the extension will be '.ts'.
For example, if you language is Czech, then find your language code from this link. In this example the code is 'cs', hence the file name will be `cs.ts`.

- You can add multiple language files at once.

- Now open the file you have just created and create the following structure first before adding your code (preferably use a better coding editor) :

```
const cs = {

};

export default cs;
```

> NOTE : For you the cs part will be different, it will be your Language code.

- Now, run the script with the argument as 0. It will convert all the english lines with the new language if the language is available in the online service.

- Please Cross check all the strings properly, if the translation of some string doesn't makes sense or haven't been translated properly, please translate them into your own words

> NOTE : Also note that, if the language is not supported by the oline service, then all the english strings will be copied as it is into the new file. In this case, you will have to manually translate ALL the strings into your language.

## How to Submit your file

- After you have completed translation of all the strings properly, submit the file either using pull request to the Github project or directly send the file by creating a GitHub request  here : [How to Create an Request](./HowToCreateRequest.md).
