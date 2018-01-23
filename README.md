[![Donate with PayPal](/Assets/donate.en.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=kszere@gmail.com&lc=PL&item_name=Project+Xiaomi+Dafang+API+on+GitHUB&no_note=0&cn=&curency_code=USD&bn=PP-DonationsBF:btn_donateCC_LG.gif:NonHosted)
# Xiaomi-Dafang-API
API and panel site for Xiaomi Dafang

![API return data with JSON](/Assets/api-return-json.png)

This API based and works with [Xiaomi-Dafang-Hacks](https://github.com/EliasKotlyar/Xiaomi-Dafang-Software).

## How get software and API?
1. [Installing the Current Dafang Hacks Custom Firmware](https://github.com/EliasKotlyar/Xiaomi-Dafang-Hacks/blob/master/hacks/install_cfw.md).
2. Clone this repository from github. If you are on windows download the repository as zip file.
3. Copy everything from "firmware_mod" folder into the root of the MicroSD. You can use FTP.
4. Open [http://[ip-dafang]/cgi-bin/api.cgi](http://[dafanghacks]/cgi-bin/api.cgi) on your Browser.

## tinyCam App on Android
1. [Download](/tinyCam/custom_vendors.xml) configuration file.
2. Open App and go to Settings ->Developer settings -> Custom brands XML file -> (select)
3. Force close App
4. Run app and Happy Fun!
![tinyCam App on Android with Commands](/Assets/tinyCam-01.png)
![tinyCam App on Android with PTZ control](/Assets/tinyCam-02.png)
![tinyCam App on Android with Archive Records](/Assets/tinyCam-03.png)

### ToDo
- [x] Add to GitHUB actual version (2018-01-23)
- [x] Create XML file configuration Camera for tinyCam on Android (2018-01-23)
- [ ] Correct and add real check return data status in api (success, error, info)
- [ ] Create table with return code api
- [ ] Add additional functions for all Actions if possible it
- [ ] Create panel with framework CSS on Dafang
