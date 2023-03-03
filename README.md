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
children = bin_file.read("/")
for (i, child) in enumerate(children):
  print("Child {}: {}".format(i, child))

# Read some data. This read method can read variables with different types, but
# there are also read methods for particular types
node_ids = bin_file.read("nodout/ids")
for (i, nid) in enumerate(node_ids):
  print("Node ID {}: {}".format(i, nid))

# You can also read this variable with the read method of the particular type
# First find out what the type is
node_ids_type = bin_file.get_type_id("/nodout/metadata/ids")

# Then read the data using the special read method.
# If you already know the exact type and path of a variable
# these methods can be a bit more performant,
# since the library does not need the get the type and path first.
if node_ids_type == BinoutType.Int32:
  node_ids = bin_file.read_int32("/nodout/metadata/ids")
elif node_ids_type == BinoutType.Int64:
  node_ids = bin_file.read_int64("/nodout/metadata/ids")
else:
  print("The node ids are not 32-Bit or 64-Bit integers")
  exit(1)

for (i, nid) in enumerate(node_ids):
  print("Node ID {}: {}".format(i, nid))

# If you want to read "timed" data (x_displacement, x_force, etc.) you can do so also with the read method
x_displacement = bin_file.read("nodout/x_displacement")
for (t, time_step) in enumerate(x_displacement):
  for (n, x_disp) in enumerate(time_step):
    print("X Displacement time_step={}, node_id={}: {}".format(t, node_ids[n], x_displacement[t][n]))
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

### KeyFile

```python
from dynareadout import key_file_parse

keywords = key_file_parse("simulation/input.k")

# Parse all nodes
node_keywords = keywords["NODE"]

for i in range(len(node_keywords)):
  for j in range(len(node_keywords[i])):
    node = node_keywords[i][j]
    node_data = node.parse_whole([8, 16, 16, 16])
    nid = node_data[0]
    x = node_data[1]
    y = node_data[2]
    z = node_data[3]

    print(f"NODE {nid:d}: ({x:.3f}; {y:.3f}; {z:.3f})")
```

## Other languages

This library is also available for C and C++ this version can be found [here](https://github.com/PucklaJ/dynareadout).

## Installation

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

Then insert `__token__` as username and the token as password.

6. Install package from `test.pypi.org` to test it

```console
python -m pip install --upgrade --no-build-isolation --index-url https://test.pypi.org/simple/ dynareadout
```

7. If it works upload it to `pypi.org`

8. Create windows wheel

```console
python -m build
```

9. Upload windows wheel to `test.pypi.org` and test it.

10. If it works upload it to `pypi.org`

```console
python -m twine upload dist/*
```
