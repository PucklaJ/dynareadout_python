#! /bin/sh

set -xe
script_dir=$(dirname $0)

mkdir -p /wheelhouse

if [[ ! -v DRO_SINGLE ]]; then
    for PYBIN in /opt/python/*/bin; do
        DRO_PIP=$PYBIN/pip DRO_OUTPUT=/wheelhouse $script_dir/build.sh
    done
else
    DRO_OUTPUT=/wheelhouse $script_dir/build.sh
fi

for whl in /wheelhouse/*.whl; do
    auditwheel repair $whl --plat $PLAT -w /artifacts
done

