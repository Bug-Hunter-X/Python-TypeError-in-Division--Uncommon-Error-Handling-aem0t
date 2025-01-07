def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# This will cause the 'TypeError' because of using string and integer
result = function_with_uncommon_error(10, "hello")
print(result) #Output: Error: Unsupported operand type(s) for /  None

# this will cause the ZeroDivisionError
result = function_with_uncommon_error(10, 0)
print(result) #Output: Error: Division by zero None