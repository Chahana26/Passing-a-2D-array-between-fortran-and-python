import twod
import numpy as np
from cffi import FFI
ffi = FFI()

def convert_to_from_cffi(c_or_numpy_array, num_bytes=None):

        '''
        Utility function to convert to and from numpy and ffi buffer interfaces
        Args:
            c_or_numpy_array (buffer):
                an object that is either a numpy array or a FFI cdata pointer
            num_bytes (integer, optional):
                size of buffer when converting from CFFI to ndarray
        '''

        if isinstance(c_or_numpy_array, np.ndarray):
            out_buffer = ffi.cast('{} *'.format('double'),
                                        c_or_numpy_array.ctypes.data)
        elif isinstance(c_or_numpy_array, ffi.CData):
            out_buffer = np.frombuffer(ffi.buffer(
                c_or_numpy_array, num_bytes), dtype=np.float64)
        else:
            raise ValueError(
                'Buffer must be either numpy.ndarray or ffi CData,\
                not {}'.format(type(c_or_numpy_array)))

        return out_buffer

n_profilep = input(" enter the number of profiles")
n_profilep = int(n_profilep)
n_layerp = input(" enter the number of layers")
n_layerp = int(n_layerp)

sw_heating_ratep = np.empty((n_profilep,n_layerp), dtype=float, order='C')

twod.lib.wrapping(convert_to_from_cffi(sw_heating_ratep),n_profilep,n_layerp)

print("back in python - trying to print the array")
print(sw_heating_ratep)
