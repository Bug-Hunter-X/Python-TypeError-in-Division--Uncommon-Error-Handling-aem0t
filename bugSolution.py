def function_with_improved_error_handling(a, b):
    try:
        if not isinstance(b, (int, float)):
            raise TypeError("Divisor must be a number")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

#This will cause TypeError
result = function_with_improved_error_handling(10, "hello")
print(result) #Output: Error: Divisor must be a number None

#this will cause ZeroDivisionError
result = function_with_improved_error_handling(10, 0)
print(result) #Output: Error: Division by zero None

#This will give the correct answer
result = function_with_improved_error_handling(10, 2)
print(result) #Output: 5.0