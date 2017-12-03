from ctypes import *
import os

fibo_lib = cdll.LoadLibrary(os.path.abspath("fibo.so"))

print fibo_lib.Fibonacci(30)

