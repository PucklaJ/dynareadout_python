#! /bin/sh

set -xe
script_dir=$(dirname $0)

if [ ! -v DRO_PYTHON ]; then
    DRO_PYTHON=$(which python)
fi

rm -rf $script_dir/build $script_dir/dist $script_dir/*.egg-info

$DRO_PYTHON -m pip wheel $script_dir --no-deps -w dist
rm -rf $script_dir/build $script_dir/*.egg-info

echo Successfully build wheel for dynareadout "($DRO_PYTHON)"

