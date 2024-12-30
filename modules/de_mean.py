import ctypes
from pathlib import Path

library = ctypes.cdll.LoadLibrary(Path(__file__).resolve().parent / "go/library.so")
de_mean_go = library.de_mean_go

de_mean_go.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
de_mean_go.restype = ctypes.c_double

def de_mean(array):
    array_type = ctypes.c_double * len(array)
    c_array = array_type(*array)

    return de_mean_go(c_array, len(array))