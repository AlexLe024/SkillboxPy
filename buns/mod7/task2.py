def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__

    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input("Введите индекс в последовательности Фибоначчи: "))
    result = fibonacci(n)
    print(f"The {n}-th Fibonacci number is: {result}")
except ValueError:
    print("Пожалуйста, введите целое число.")
