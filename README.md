# greenhouse-console

## Setup

At Raspberry Pi install Qt5, PyQt5, paho-mqtt _using `apt install`_. Note that `pip` installation
 is currently broken. 

For other systems: from repository root run `source init.sh`

Run `source installer.sh` to make distribution.

Make `deploy.sh` execuatble (`chmod a+x `) and run `sudo deploy.sh` to
 deploy application to `/usr/local/lib/`.  It can be run as 
 `/usr/local/lib/greenhouse-console/greenhouse-console`

## Running as kiosk app at Raspberry Pi

It is assumed that kiosk is run under `pi` user account.

Use `sudo systemctl stop` and `sudo systemctl disable` to sop current display manager
 (`lightdm.service` by default)

Install [`nodm`](https://github.com/spanezz/nodm) package by `apt install`.
 Edit `/etc/default/nodm` and set `NODM_USER=pi` and 
`NODM_XSESSION=/home/pi/Xsession`

Create `/home/pi/Xsession` and insert
 [the following lines](https://github.com/ekondayan/poor_mans_kiosk):

```
/usr/bin/xset -d :0 s off
/usr/bin/xset -d :0 s noblank
/usr/bin/xset -d :0 -dpms
xrandr -d :0 --output HDMI-1 --brightness 0.25
/usr/bin/unclutter -d :0 -idle 0.5 -root &

/usr/local/lib/greenhouse-console/greenhouse-console
```

Run `sudo systemctl start nodm` and verify that the app is starting up.

## Testing 

- Run `app.py`, use `-H <MQTT broker host>` to connect to broker other than `localhost`.
- from any terminal run `mosquitto_pub`, changing topic and message: 
 ````
 mosquitto_pub -h <MQTT broker host> -t "nodes/node1/temp/T2" -m "{\"value\": 18, \"unit\": \"\u00b0C\"}"
 ```` 
.
