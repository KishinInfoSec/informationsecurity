---
title: blueducky-script
tags: [wireless-hacking, bluetooth-attacks, type/tool, phase/exploitation, platform/wireless]
---

# BlueDucky Script

## Introduction


 CVE-2023-45866 - BlueDucky Implementation (Using DuckyScript)  Unauthenticated Peering Leading to Code Execution (Using HID Keyboard)


BlueDucky is a powerful tool for exploiting a vulnerability in Bluetooth devices. By running this script, you can:

1.  Load saved Bluetooth devices that are no longer visible but have Bluetooth still enabled.
2.  Automatically save any devices you scan.
3.  Send messages via ducky script format to interact with devices.

## Installation

```
# update apt
sudo apt-get update
sudo apt-get -y upgrade

# install dependencies from apt
sudo apt install -y bluez-tools bluez-hcidump libbluetooth-dev \
                    git gcc python3-pip python3-setuptools \
                    python3-pydbus

# install pybluez from source
git clone 
cd pybluez
sudo python3 setup.py install

# build bdaddr from the bluez source
cd ~/
git clone --depth=1 
gcc -o bdaddr ~/bluez/tools/bdaddr.c ~/bluez/src/oui.c -I ~/bluez -lbluetooth
sudo cp bdaddr /usr/local/bin/
```

### Running the Script

```
git clone 
cd BlueDucky
sudo hciconfig hci0 up
python3 BlueDucky.py
```

Alternatively,

```
pip3 install -r requirements.txt
```

## Demo

***

## REFERENCES

* 
* 
* 
