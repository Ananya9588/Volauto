#!/bin/bash

sudo pacman -S python2
sudo pacman -S python3
sudo pacman -S git

git clone https://github.com/volatilityfoundation/volatility.git

cd volatility/

git clone https://github.com/superponible/volatility-plugins.git

sudo python2 setup.py install

sudo pip2 install pillow

sudo pip2 install pycrypto

sudo pip2 install distorm3

sudo pip2 install yara-python
