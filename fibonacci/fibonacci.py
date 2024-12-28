import ctypes
from pathlib import Path

library = ctypes.cdll.LoadLibrary(Path(__file__).resolve().parent / "go/library.so")
fibonacci_iterative = library.fibonacci_iterative
fibonacci_recursive = library.fibonacci_recursive

fibonacci_iterative.argtypes = [ctypes.c_int]
fibonacci_iterative.restype = ctypes.c_char_p

def fibonacci(num, recursive=False):
    if recursive is False:
        return int(fibonacci_iterative(num).decode())
    else:
        return fibonacci_recursive(num)