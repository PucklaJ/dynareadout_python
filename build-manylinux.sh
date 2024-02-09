#! /bin/sh

set -xe

git clone --recursive https://github.com/PucklaJ/dynareadout_python.git
cd dynareadout_python

DRO_PIP=/opt/python/cp310-cp310/pip DRO_OUTPUT=/io ./build.sh

