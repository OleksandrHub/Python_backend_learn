def square(x):
    """Returns the square of x."""
    return x * x

def cube(x):
    """Returns the cube of x."""
    return x * x * x

def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    """Returns the nth number in the Fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)