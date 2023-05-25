import os
from setuptools import setup
from setuptools.extension import Extension

this_dir = os.path.dirname(os.path.abspath(__file__))
dynareadout_dir = os.path.join('lib', 'dynareadout')

compile_args = []
if os.name == "nt":
    compile_args.append("/std:c++17")
    compile_args.append("/w")
else:
    compile_args.append("-std=c++17")
    compile_args.append("-w")

dynareadout_c = Extension(
    name='dynareadout_c',
    extra_compile_args=compile_args,
    include_dirs=[
        os.path.join(this_dir, 'lib', 'pybind11', 'include'),
        os.path.join(dynareadout_dir, 'src'),
        os.path.join(dynareadout_dir, 'src', 'cpp')
    ],
    sources=[
        # C Source Files
        os.path.join(dynareadout_dir, 'src', 'binary_search.c'),
        os.path.join(dynareadout_dir, 'src', 'binout.c'),
        os.path.join(dynareadout_dir, 'src', 'binout_directory.c'),
        os.path.join(dynareadout_dir, 'src', 'binout_glob.c'),
        os.path.join(dynareadout_dir, 'src', 'binout_read.c'),
        os.path.join(dynareadout_dir, 'src', 'd3_buffer.c'),
        os.path.join(dynareadout_dir, 'src', 'd3plot.c'),
        os.path.join(dynareadout_dir, 'src', 'd3plot_data.c'),
        os.path.join(dynareadout_dir, 'src', 'd3plot_part_nodes.c'),
        os.path.join(dynareadout_dir, 'src', 'd3plot_state.c'),
        os.path.join(dynareadout_dir, 'src', 'extra_string.c'),
        os.path.join(dynareadout_dir, 'src', 'key.c'),
        os.path.join(dynareadout_dir, 'src', 'path.c'),
        os.path.join(dynareadout_dir, 'src', 'path_view.c'),
        # C++ Source Files
        os.path.join(dynareadout_dir, 'src', 'cpp', 'binout.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot_part.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot_state.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'key.cpp'),
        # C++ Source Files for pybind11 module
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_binout.cpp'),
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_d3plot.cpp'),
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_key.cpp'),
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_module.cpp'),
    ])

setup(name='dynareadout',
      version='23.05',
      ext_modules=[dynareadout_c],
      zip_safe=False,
      include_package_data=True)
