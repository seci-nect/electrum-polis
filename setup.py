#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-POLIS requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-polis.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-polis.png'])
    ]

setup(
    name="Electrum-POLIS",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib',
        'PySocks>=1.6.6',
        'trezor>=0.6.3',
        'x11_hash>=1.4',
    ],
    dependency_links=[
        'git+https://github.com/akhavr/x11_hash@1.4#egg=x11_hash-1.4',
        'git+https://github.com/electrum-polis/python-trezor@v0.6.13#egg=trezor',
    ],
    packages=[
        'electrum_polis',
        'electrum_polis_gui',
        'electrum_polis_gui.qt',
        'electrum_polis_plugins',
        'electrum_polis_plugins.audio_modem',
        'electrum_polis_plugins.cosigner_pool',
        'electrum_polis_plugins.email_requests',
        'electrum_polis_plugins.hw_wallet',
        'electrum_polis_plugins.keepkey',
        'electrum_polis_plugins.labels',
        'electrum_polis_plugins.ledger',
        'electrum_polis_plugins.trezor',
        'electrum_polis_plugins.digitalbitbox',
        'electrum_polis_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_polis': 'lib',
        'electrum_polis_gui': 'gui',
        'electrum_polis_plugins': 'plugins',
    },
    package_data={
        'electrum_polis': [
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-polis'],
    data_files=data_files,
    description="Lightweight Polispay Wallet",
    author="akhavr",
    license="MIT License",
    url="https://electrum-polis.org",
    long_description="""Lightweight Polispay Wallet"""
)
