import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
    return wrapper

def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper

@timer
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input("Введите значение n для числа Фибоначчи: "))
    result = fibonacci(n)
    print(f"The {n}-th Fibonacci number is: {result}")
except ValueError:
    print("Пожалуйста, введите целое число.")
