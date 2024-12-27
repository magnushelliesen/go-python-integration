import ctypes

library = ctypes.cdll.LoadLibrary('fibonacci/go/library.so')
fibonacci_iterative = library.fibonacci_iterative

fibonacci_iterative.argtypes = [ctypes.c_int]
fibonacci_iterative.restype = ctypes.c_char_p

def fibonacci(num):
    return int(fibonacci_iterative(num).decode())