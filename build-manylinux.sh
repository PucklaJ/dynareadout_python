#! /bin/sh

set -xe

git clone --recursive https://github.com/PucklaJ/dynareadout_python.git
cd dynareadout_python

for PYBIN in /opt/python/*/bin; do
    DRO_PIP=$PYBIN/pip DRO_OUTPUT=/io ./build.sh
done

