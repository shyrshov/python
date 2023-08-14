# 1) Create a decorator named "cache" that allow you to store the result of any function call in cache. 
# Every time the function is called with different arguments that result of this call should be added to cache. 
# In case the function decorated with a @cache was previously called with same arguments - the result should be returned
#  from the cache and message should be sent to the console that this value was taken from the cache.

# For example:

# @cache
# def add_numbers(a, b):
#     return a + b
    
# >>> add_numbers(1, 2)
# >>> 3

# >>> add_numbers(2, 4)
# >>> 6

# >>> add_numbers(1, 2)
# >>> 'Result was taken from cache'
# >>> 3

operations = {}

def cache(func): 
    def wrapper(num1: int, num2: int):
        k = (func.__name__, num1, num2)
        if k in operations:
            print("Result was taken from cache")
            return operations[k]
        else:
            result = func(num1, num2)
            operations[k] = result
            return result
    return wrapper

@cache
def add_numbers(num1: int, num2: int):
    return num1 + num2

print(add_numbers(1, 2))
print(add_numbers(2, 4))
print(add_numbers(1, 2))


# 2) Create a decorator "log" which takes 2 parameters "log_level" and "output_file". This decorator should add log message 
# to output file with the following format - "{Debug Level}": "Function {function name} was called with arguments {arguments}".

def log(log_level, output_file):
    def decorator(func):  
        def wrapper(*args, **kwargs):
            with open(output_file, 'w') as file:
                file.write(f'"{log_level}": "Function "{func.__name__}" was called with arguments {args}, {kwargs}"\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log(log_level="Debug Level", output_file="lesson11\decorator.txt")
def add(num1, num2):
    return num1+num2

print(add(1, 5))