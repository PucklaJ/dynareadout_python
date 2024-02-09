#! /bin/sh

set -xe

git clone --recursive https://github.com/PucklaJ/dynareadout_python.git
cd dynareadout_python

mkdir -p /wheelhouse

if [[ ! -v DRO_SINGLE ]]; then
    for PYBIN in /opt/python/*/bin; do
        DRO_PIP=$PYBIN/pip DRO_OUTPUT=/wheelhouse ./build.sh
    done
else
    DRO_OUTPUT=/wheelhouse ./build.sh
fi

for whl in /wheelhouse/*.whl: do
    if [ ! auditwheel show $whl ]; then
        echo "Skipping non-platform wheel $whl"
    else
        auditwheel repair $whl --plat $PLAT -w /io
    fi
done

cp /wheelhouse/* /io/

