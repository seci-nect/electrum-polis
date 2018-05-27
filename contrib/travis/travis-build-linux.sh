#!/bin/bash
BUILD_REPO_URL=https://github.com/akhavr/electrum-seci.git

cd build

if [[ -z $TRAVIS_TAG ]]; then
  exit 0
else
  git clone --branch $TRAVIS_TAG $BUILD_REPO_URL electrum-seci
fi

docker run --rm -v $(pwd):/opt -w /opt/electrum-seci -t akhavr/electrum-seci-release:Linux /opt/build_linux.sh
docker run --rm -v $(pwd):/opt -v $(pwd)/electrum-seci/:/root/.wine/drive_c/electrum -w /opt/electrum-seci -t akhavr/electrum-seci-release:Wine /opt/build_wine.sh
