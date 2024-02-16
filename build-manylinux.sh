#! /bin/sh

set -xe

mkdir -p /wheelhouse

if [[ ! -v DRO_SINGLE ]]; then
    for PYBIN in /opt/python/*/bin; do
        DRO_PIP=$PYBIN/pip DRO_OUTPUT=/wheelhouse ./build.sh
    done
else
    DRO_OUTPUT=/wheelhouse ./build.sh
fi

for whl in /wheelhouse/*.whl; do
    if ! auditwheel show "$whl"; then
        echo "Skipping non-platform wheel $whl"
        cp $whl /io/
    else
        auditwheel repair $whl --plat $PLAT -w /artifacts
    fi
done

