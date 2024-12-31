import ctypes
from pathlib import Path

library = ctypes.cdll.LoadLibrary(Path(__file__).resolve().parent / "go/library.so")

fibonacci_iterative_go = library.fibonacci_iterative
fibonacci_recursive_go = library.fibonacci_recursive

fibonacci_iterative_go.argtypes = [ctypes.c_int]
fibonacci_iterative_go.restype = ctypes.c_char_p

def fibonacci(num, recursive=False):
    if recursive is False:
        return int(fibonacci_iterative_go(num).decode())
    else:
        return fibonacci_recursive_go(num)