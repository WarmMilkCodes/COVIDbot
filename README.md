# COVIDbot

This Discord bot was created during RU Hacks: 2022. The purpose of the bot is to allow for more COVID-19 awareness and to share resources with Discord users.

The bot has six functional slash commands:
- Covid Counter - Displays current worldwide COVID case utilizing BeautifulSoup web scraping from Worldometers.info
- Covid Info - Returns a hyperlink to CDC's COVID-19 landing page, for COVID-19 information and resources
- Covid Test - Returns a hyperlink to USPS's website to request free at home COVID-19 test kits
- Covid Vaccine - Utilizes USZipCode module to take user's zipcode and return Vaccine.gov search results for vaccine locations near user's zipcode
- Covid Local - Utilizes CDC's API, and addfips module, and USZipCode module to take user's zipcode, convert it to FIPS and then access the CDC's API to return local community information such as cases or deaths (this API can also return other information, but is currently only dispalying cases/deaths)
