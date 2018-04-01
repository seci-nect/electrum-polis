#!/bin/bash
BUILD_REPO_URL=https://github.com/akhavr/electrum-polis.git

cd build

if [[ -z $TRAVIS_TAG ]]; then
  exit 0
else
  git clone --branch $TRAVIS_TAG $BUILD_REPO_URL electrum-polis
fi

docker run --rm -v $(pwd):/opt -w /opt/electrum-polis -t akhavr/electrum-polis-release:Linux /opt/build_linux.sh
docker run --rm -v $(pwd):/opt -v $(pwd)/electrum-polis/:/root/.wine/drive_c/electrum -w /opt/electrum-polis -t akhavr/electrum-polis-release:Wine /opt/build_wine.sh
