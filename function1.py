#1. Standard Function Definition 

#with parameters and return
def multiply(x, y):
 return x * y

result = multiply(5, 4)
print(result)

#without parameters and return
def greet():
    print("Hello, world!")

greet()

#2.Recursive Functions
#example 1
def fib(n):
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)
  
print(fib(6))

#example 2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)

