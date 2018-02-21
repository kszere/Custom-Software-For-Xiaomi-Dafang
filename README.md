## Repo build, coming soon.

[![Donate with PayPal](/assets/donate.en.png)](https://paypal.me/kszere)

# Custom Software For Xiaomi Dafang
This repository cointains Custom Software with HTTP API and panel site for the Xiaomi Dafang Camera.

This API based with [Xiaomi Dafang Hacks](https://github.com/EliasKotlyar/Xiaomi-Dafang-Hacks).

## HTTP API
![API return data with JSON](/assets/api-return-json.png)

Return data in JSON.


## Repo Wiki
* [How add Xiaomi Dafang API on Camera](https://github.com/kszere/Xiaomi-Dafang-API/wiki/How-add-Xiaomi-Dafang-API-on-Camera)
* [How add XML config on tinyCam App on Android](https://github.com/kszere/Xiaomi-Dafang-API/wiki/How-add-XML-config-on-tinyCam-App-on-Android)

## Features
* HTTP API with return JSON data
* config for tinyCam App on Android
* WEB Panel with HTML5/CSS/JS \(in soon\)

### ToDo
* [ ] Correct and add real check return data status in api \(success, error, info\)
* [ ] Create table with return code api
* [ ] Add additional functions for all Actions if possible it
* [ ] Create panel with framework CSS on Dafang

### Changelog
###### v0.0.5 Beta (not upload)
* [x] rename repo from `Xiaomi-Dafang-API` to `Custom-Software-For-Xiaomi-Dafang`
* [ ] added OSD to RTSP and snaphot

###### v0.0.4 Beta
* [x] added nightvision in ?action=get_snaphot when v4l2rtspserver-master running
* [x] added home page api.cgi with informations about API
* [x] update Manual and Documentation API

###### v0.0.3 Beta
* [x] start making GitBook Documentation API [click here](https://kszere.gitbooks.io/xiaomi-dafang-api/content/) \(2018-01-30\)
* [x] update system informaations on API \(2018-01-31\)
* [x] added new ?action=get_snaphot for making snaphot, also when running v4l2rtspserver-master \(2018-01-31\)
* [x] added new ?action=set_timezone for change timezone localy time (\(2018-01-31\))

###### v0.0.2 Beta
* [x] create XML file configuration Camera for tinyCam on Android \(2018-01-23\)
* [x] added system  informations on API \(2018-01-28\)
* [x] added light sensor information on API \(2018-01-28\)

###### v0.0.1 Beta
* [x] create repo \(2018-01-23\)
* [x] upload first version api \(2018-01-23\)
