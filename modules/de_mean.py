import ctypes
from pathlib import Path

library = ctypes.cdll.LoadLibrary(Path(__file__).resolve().parent / "go/library.so")

de_mean_go = library.de_mean
free_array_go = library.free_array

de_mean_go.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
de_mean_go.restype = ctypes.POINTER(ctypes.c_double)

def de_mean(input_list):
    input_array = (ctypes.c_double * len(input_list))(*input_list)
    result_pointer = de_mean_go(input_array, ctypes.c_int(len(input_list)))
    result_array = [result_pointer[i] for i in range(len(input_list))]
    free_array_go(result_pointer)
    return result_array