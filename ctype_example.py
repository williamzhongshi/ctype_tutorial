from ctypes import *
import os

libc = cdll.LoadLibrary("libc.so.6")

print(libc.time(None))
i = c_int(42)
print(i)
print(i.value)

printf = libc.printf
printf(b"Hello, %s\n", b"World!")

print_lib = cdll.LoadLibrary(os.path.abspath("print_hello.so"))
print_lib.hello()

add_lib = cdll.LoadLibrary(os.path.abspath("add_two_values.so"))

print add_lib.add_two_values(5, 6)

result = c_uint32()

add_lib.add_two_values_return_ref(5, 6, byref(result))

print result.value