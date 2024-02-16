import os
from setuptools import setup
from setuptools.extension import Extension

this_dir = os.path.dirname(os.path.abspath(__file__))
dynareadout_dir = os.path.join('lib', 'dynareadout')

c_args = []
cpp_args = []
link_args = []
if os.name == "nt":
    cpp_args.append("/std:c++17")
    cpp_args.append("/w")
    c_args.append("/w")
else:
    cpp_args.append("-std=c++17")
    cpp_args.append("-w")
    c_args.append("-ansi")
    c_args.append("-w")
    link_args.append("-lpthread")
    link_args.append("-lstdc++fs")

ext_libraries = [[
    'dynareadout_c', {
        'sources': [
            # C Source Files
            os.path.join(dynareadout_dir, 'src', 'binary_search.c'),
            os.path.join(dynareadout_dir, 'src', 'binout_directory.c'),
            os.path.join(dynareadout_dir, 'src', 'binout_glob.c'),
            os.path.join(dynareadout_dir, 'src', 'binout_read.c'),
            os.path.join(dynareadout_dir, 'src', 'binout.c'),
            os.path.join(dynareadout_dir, 'src', 'd3_buffer.c'),
            os.path.join(dynareadout_dir, 'src', 'd3plot_data.c'),
            os.path.join(dynareadout_dir, 'src', 'd3plot_part_nodes.c'),
            os.path.join(dynareadout_dir, 'src', 'd3plot_state.c'),
            os.path.join(dynareadout_dir, 'src', 'd3plot.c'),
            os.path.join(dynareadout_dir, 'src', 'extra_string.c'),
            os.path.join(dynareadout_dir, 'src', 'include_transform.c'),
            os.path.join(dynareadout_dir, 'src', 'key.c'),
            os.path.join(dynareadout_dir, 'src', 'line.c'),
            os.path.join(dynareadout_dir, 'src', 'multi_file.c'),
            os.path.join(dynareadout_dir, 'src', 'path_view.c'),
            os.path.join(dynareadout_dir, 'src', 'path.c'),
            os.path.join(dynareadout_dir, 'src', 'string_builder.c'),
            os.path.join(dynareadout_dir, 'src', 'sync.c'),
        ],
        'include_dirs': [
            os.path.join(dynareadout_dir, 'src'),
        ],
        'cflags': c_args,
    }
]]

dynareadout = Extension(
    name='dynareadout',
    extra_compile_args=cpp_args,
    extra_link_args=link_args,
    include_dirs=[
        os.path.join(this_dir, 'lib', 'pybind11', 'include'),
        os.path.join(dynareadout_dir, 'src'),
        os.path.join(dynareadout_dir, 'src', 'cpp')
    ],
    sources=[
        # C++ Source Files
        os.path.join(dynareadout_dir, 'src', 'cpp', 'binout.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot_part.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot_state.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'd3plot.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'include_transform.cpp'),
        os.path.join(dynareadout_dir, 'src', 'cpp', 'key.cpp'),
        # C++ Source Files for pybind11 module
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_binout.cpp'),
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_d3plot.cpp'),
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_key.cpp'),
        os.path.join(dynareadout_dir, 'src', 'python', 'pybind11_module.cpp'),
    ],
    libraries=['dynareadout_c'],
)

setup(name='dynareadout',
      version='24.01.1',
      ext_modules=[dynareadout],
      zip_safe=False,
      include_package_data=True,
      libraries=ext_libraries)
