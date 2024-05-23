# Trend Vision - Auto Add IoC 1.0

[![Travis branch](https://img.shields.io/badge/made%20with-%3C3-red.svg)](https://github.com/its0v3r/https://github.com/its0v3r/Trend-Vision-Auto-Add-IoC)

## 📄 About

Trend Vision - Auto Add IoC is a software meant to block lots of IOCs in Trend Vision Threat Intelligence Suspicious Object Management feature.

## 🌟 Features

-   Adds lots of IoCs without having to manually insert by one;
-   Simple CSV list to insert the client name and Trend Vision Token (API Key);
-   Fast and simple to use: just edit the "csv/client_data.csv" to add new clients and "csv/ioc-list.csv" to add new IoCs;
-   Choose if you want to make the changes to a single client or to only a single client;
-   You can skip IoCs if they are already blocked in the client's Vision: you need to open the "csv/ioc-list.csv" and in "blocked" column you need to insert the client names that already have that IoCs blocked. For example, if I aready blocked IoC ABCDEF123456 in client "Fake Client", in the refered IoC row I will edit the column "blocked" and add "Fake Client" there. If you want to add more clients, just add commas and keep adding client names.

## 💻 How to use?

1. Enter you client name and it's API Key token in the "csv/client_data.csv";
2. Place the IoCs you want to block in "csv/ioc-list.csv". IoCs can be from multiple types: sha1, sha256, url, domain, ip and email. Please, follow Trend Vision rules to properly add the IoCs.
3. With the 2 files ready, execute the script
4. Select your desired language
5. Select the client
6. Confirm if you want to proceed
7. The IoCs will start to get blocked

## 🌎 Available Languages

-   English (US) - by its0v3r
-   Português (Brasil) - by its0v3r
