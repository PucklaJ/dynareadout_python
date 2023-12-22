# dynareadout

High-Performance and Thread-Safe C/C++ library for parsing binary output files and key files of LS Dyna (d3plot, binout, input deck) with bindings for python.

## Documentation

You can find a [Wiki](https://github.com/PucklaJ/dynareadout/wiki) with API Documentation for python.

## Examples

### Binout

```python
from dynareadout import Binout

bin_file = None
try:
  # This library also supports opening multiple binout files at once by globing them
  bin_file = Binout("path/to/your/binout*")
except RuntimeError as e:
  print("Failed to open binout: {}".format(e))
  exit(1)

# Print the children of the binout
children = bin_file.read()
for (i, child) in enumerate(children):
  print("Child {}: {}".format(i, child))

# Read some data. This method can read variables of all different types
node_ids = bin_file.read("nodout/ids")
for i in range(len(node_ids)):
  print("Node ID {}: {}".format(i, node_ids[i]))

# You can also find out if a variable exists
node_ids_exist = bin_file.variable_exists("nodout/ids")

# Get the number of time steps in the binout
nodout_timesteps = bin_file.get_num_timesteps("nodout")
# The time steps can vary inside the binout
rcforc_timesteps = bin_file.get_num_timesteps("rcforc")

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
  plot_file = D3plot("path/to/your/d3plot")
except RuntimeError as e:
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

keywords = key_file_parse("path/to/your/input.k")

# Parse all nodes
node_keywords = keywords["NODE"]

# Loop over all *NODE keywords
for i in range(len(node_keywords)):
  # Loop over all cards of each *NODE keyword
  for j in range(len(node_keywords[i])):
    node = node_keywords[i][j]
    # Then you can parse the variables of each card as integers and floats
    # The list of integers holds all the widths of each variable in the card in characters
    nid, x, y, z = node.parse_whole([8, 16, 16, 16])

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
