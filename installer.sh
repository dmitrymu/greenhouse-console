#! /bin/bash

if [ ! -d build ]; then
    mkdir build
else
    rm -rf build/*
fi

pushd build

pyinstaller -n greenhouse-console ../src/app/app.py

popd
