#! /bin/sh

set -xe
script_dir=$(dirname $0)

if [[ ! -v DRO_PIP ]]; then
    DRO_PIP=$(which python) -m pip
fi
if [[ ! -v DRO_OUTPUT ]]; then
    DRO_OUTPUT=$script_dir/dist
fi

rm -rf $script_dir/build $script_dir/dist $script_dir/*.egg-info

$DRO_PIP wheel $script_dir --no-deps -w $DRO_OUTPUT
rm -rf $script_dir/build $script_dir/*.egg-info

echo Successfully built wheel for dynareadout "($DRO_PIP)"

