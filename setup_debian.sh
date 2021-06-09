#!/bin/bash

sudo apt install python2
sudo apt install python3
sudo apt install git 

git clone https://github.com/volatilityfoundation/volatility.git

cd volatility/

git clone https://github.com/superponible/volatility-plugins.git

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py

sudo python2 get-pip.py

sudo python2 setup.py install

sudo pip2 install pillow

sudo pip2 install pycrypto

sudo pip2 install distorm3

sudo pip2 install yara-python
