#! /bin/bash

if [ ! -d .venv ]; then
    mkdir .venv
    python -m venv .venv
fi

source .venv/bin/activate

pip install -U wheel
pip install -U PyQt6
pip install -U paho-mqtt
pip install -U PyInstaller pyinstaller-hooks-contrib    
