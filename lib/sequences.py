#!/usr/bin/env python3
import ipdb

def print_fibonacci(length):
    fibonacci = [value * 0 for value in range(length)]
    if len(fibonacci) > 2:
        fibonacci[1] = 1
        i = 2
        while i < length:
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
            i += 1
    elif len(fibonacci) == 2:
        fibonacci[1] = 1
    print(fibonacci)

# print_fibonacci(6)
# ipdb.set_trace()