#!/bin/bash

VERSION_STRING=(`grep ELECTRUM_VERSION lib/version.py`)
electrum_VERSION=${VERSION_STRING[2]}
electrum_VERSION=${electrum_VERSION#\'}
electrum_VERSION=${electrum_VERSION%\'}
export electrum_VERSION
