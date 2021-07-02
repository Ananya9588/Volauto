#!/bin/bash

sudo apt install python2
sudo apt install python3
sudo apt install git 

git clone https://github.com/volatilityfoundation/volatility.git
wget downloads.volatilityfoundation.org/releases/2.6/volatility_2.6_lin64_standalone.zip

unzip volatility_2.6_lin64_standalone.zip


cd volatility/

cp ../volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone .
chmod +x volatility_2.6_lin64_standalone/volatility_2.6_lin64_standalone
git clone https://github.com/superponible/volatility-plugins.git

sudo python2 setup.py install

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py

sudo python2 get-pip.py

sudo pip2 install pillow

sudo pip2 install pycrypto

sudo pip2 install distorm3

sudo pip2 install yara-python
