import os
import numpy as np
from cffi import FFI
from os.path import abspath

desired_compiler = 'gcc'
real2_library_path = abspath('./libtwod.a')

absolute_library_path = os.path.abspath(real2_library_path)


def as_pointer(numpy_array):
    assert numpy_array.flags['F_CONTIGUOUS'], \
        "array is not contiguous in memory (Fortran order)"
    return ffi.cast("double*", numpy_array.__array_interface__['data'][0])



####################
# Setup part
####################

if not os.environ.get('CC'):
    os.environ['CC'] = desired_compiler


####################
# Compilation part
####################

ffibuilder = FFI()
# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("void wrapping(double *Q,int a,int b);", override=True)


# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("twod",''' #include "2darr.h" ''',
                      library_dirs=[os.getcwd()],
                      include_dirs=[os.getcwd()],
                      extra_link_args=[os.path.abspath(real2_library_path), '-lgfortran',])
ffibuilder.compile(verbose=True)
