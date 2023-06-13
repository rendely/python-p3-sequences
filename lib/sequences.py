#!/usr/bin/env python3

def print_fibonacci(length):   
    if length == 0:
      fib = [] 
    elif length == 1:
      fib = [0]
    elif length > 1:
      fib = [0,1]
      while len(fib) < length:
        a = fib[-1]
        b = fib[-2]
        fib.append(a+b)
    print (fib)

print_fibonacci(0)    
print_fibonacci(1)    
print_fibonacci(2)
print_fibonacci(5)
print_fibonacci(10)