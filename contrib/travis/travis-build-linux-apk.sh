#!/bin/bash
set -ev

if [[ -z $TRAVIS_TAG ]]; then
  echo TRAVIS_TAG unset, exiting
  exit 1
fi

BUILD_REPO_URL=https://github.com/akhavr/electrum-polis.git

cd build

git clone --branch $TRAVIS_TAG $BUILD_REPO_URL electrum-polis

docker run --rm \
    -v $(pwd):/opt \
    -w /opt/electrum-polis \
    -t zebralucky/electrum-polis-winebuild:Linux /opt/build_linux.sh

sudo find . -name '*.po' -delete
sudo find . -name '*.pot' -delete

sudo chown -R 1000 electrum-polis

docker run --rm \
    -v $(pwd)/electrum-polis:/home/buildozer/build \
    -t zebralucky/electrum-polis-winebuild:Kivy bash -c \
    'rm -rf packages && ./contrib/make_packages && mv ./contrib/packages . && ./contrib/make_apk'
