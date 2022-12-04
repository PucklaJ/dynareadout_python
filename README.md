# dynareadout

An Ansi C library for parsing binary output files of LS Dyna (d3plot, binout) with bindings for python

## Examples

### Binout

```python
from dynareadout import Binout, BinoutType

bin_file = None
try:
  # This library also supports opening multiple binout files at once by globing them
  bin_file = Binout("simulation/binout*")
except RuntimeError as e:
  print("Failed to open binout: {}".format(e))
  exit(1)

# Print the children of the binout
children = bin_file.get_children("/")
for (i, child) in enumerate(children):
  print("Child {}: {}".format(i, child))

# Read some data. This read method can read variables with different types, but
# there are also read methods for particular types
node_ids = bin_file.read("/nodout/metadata/ids")
for (i, nid) in enumerate(node_ids):
  print("Node ID {}: {}".format(i, nid))

# You can also read this variable with the read method of the particular type
# First find out what the type is
node_ids_type = bin_file.get_type_id("/nodout/metadata/ids")

# Then read the data using the special read method.
# The benefit of using those methods over the generalised read method
# is that the data does not need to be converted to a python list, but
# instead it can be accessed directly which is better for performance.
if node_ids_type == BinoutType.Int32:
  node_ids = bin_file.read_int32("/nodout/metadata/ids")
elif node_ids_type == BinoutType.Int64:
  node_ids = bin_file.read_int64("/nodout/metadata/ids")
else:
  print("The node ids are not 32-Bit or 64-Bit integers")
  exit(1)

for (i, nid) in enumerate(node_ids):
  print("Node ID {}: {}".format(i, nid))
```

### D3plot

```python
from dynareadout import D3plot

plot_file = None
try:
  # Just give it the first d3plot file and it opens all of them
  plot_file = D3plot("simulation/d3plot")
except e as RuntimeError:
  print("Failed to open: {}".format(e))
  exit(1)

# Read the title
title = plot_file.read_title()
print("Title: {}".format(title))

# Read node ids
node_ids = plot_file.read_node_ids()
print("Nodes: {}".format(len(node_ids)))
for (i, nid) in enumerate(node_ids):
  print("Node {}: {}".format(i, nid))

# Read node coordinates of time step 10
node_coords = plot_file.read_node_coordinates(10)
for i in range(len(node_coords)):
  print("Node Coords {}: ({:.2f}, {:.2f}, {:.2f})".format(i, node_coords[i][0], node_coords[i][1], node_coords[i][2]))
```

## Other languages

This library is also available for C and C++ this version can be found [here](https://github.com/PucklaJ/dynareadout).

## Installation

*The library has not yet been uploaded to the official PyPI*

```console
python -m pip install dynareadout
```

## Uploading to PyPI

1. Make sure that the dynareadout submodule has the correct version

2. Update the version in `setup.py` and `pyproject.toml`. Also check if new source files have been added

3. Publish a new release

4. Create source distribution

```console
python setup.py sdist
```
5. Upload to `test.pypi.org`

```console
python -m twine upload --repository testpypi dist/*
```

6. Install package from `test.pypi.org` to test it

```console
python -m pip install --no-build-isolation --index-url https://test.pypi.org/simple/ dynareadout
```

7. If it works upload it to `pypi.org`

```console
python -m twine upload dist/*
```
