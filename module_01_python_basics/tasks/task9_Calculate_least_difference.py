
# def function_name():
#     body
#     return value 
a, b, c = 10, 20, 30;
def least_difference(a,b,c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    # The docstring is a triple-quoted string (which may span multiple lines) 
    # that comes immediately after the header of a function. 
    # When we call help() on a function, it shows the docstring
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    
    return min(diff1, diff2, diff3)
# If we dont include return keyword, it would print None as the output. Which is a special value in Python.
#Two functions that dont return anything are print() and help(). They display information but dont return a value.

print(least_difference(a, b, c))
print(least_difference(10,40, 90))
print(least_difference(-100, -200, 400))
help(least_difference)