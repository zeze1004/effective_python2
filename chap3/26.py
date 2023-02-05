def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper

# def fibonacci(n):
#     """Return the n-th Fibonacci number"""
#     if n in (0, 1):
#         return n
#     return fibonacci(n - 2) + fibonacci(n - 1)
#
# fibonacci = trace(fibonacci)
#
#
# fibonacci(4)
#
# print(fibonacci)

from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """n번째 피보나치 수를 반환함"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# Example 9
help(fibonacci)
print(fibonacci)