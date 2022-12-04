import os
from setuptools import setup
from setuptools.extension import Extension

this_dir = os.path.dirname(os.path.abspath(__file__))
dynareadout_dir = os.path.join('src', 'dynareadout')

dynareadout = Extension(
  name='dynareadout',
  include_dirs=[
    os.path.join(this_dir, 'src', 'include'),
    os.path.join(dynareadout_dir, 'src'),
    os.path.join(dynareadout_dir, 'src', 'cpp')
  ],
  sources=[
    # C Source Files
    os.path.join(dynareadout_dir, 'src', 'binout.c'),
    os.path.join(dynareadout_dir, 'src', 'binout_glob.c'),
    os.path.join(dynareadout_dir, 'src', 'd3_buffer.c'),
    os.path.join(dynareadout_dir, 'src', 'd3plot.c'),
    os.path.join(dynareadout_dir, 'src', 'd3plot_data.c'),
    os.path.join(dynareadout_dir, 'src', 'd3plot_state.c'),
    os.path.join(dynareadout_dir, 'src', 'path.c'),
    # C++ Source Files
    os.path.join(dynareadout_dir, 'src', 'cpp', 'binout.cpp'),
    os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot.cpp'),
    os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot_part.cpp'),
    # C++ Source Files for pybind11 module
    os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_binout.cpp'),
    os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_d3plot.cpp'),
    os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_module.cpp'),
  ]
)

setup(
  name='dynareadout',
  version='0.4',
  ext_modules=[dynareadout],
  zip_safe=False,
  include_package_data=True
)
