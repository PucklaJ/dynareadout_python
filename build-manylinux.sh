#! /bin/sh

set -xe

git clone --recursive https://github.com/PucklaJ/dynareadout_python.git
cd dynareadout_python

if [[ ! -v DRO_SINGLE ]]; then
    for PYBIN in /opt/python/*/bin; do
        DRO_PIP=$PYBIN/pip DRO_OUTPUT=/io ./build.sh
    done
else
    DRO_OUTPUT=/io ./build.sh
fi

