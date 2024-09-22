"""
In this exercise, your task is to complete the function `count_object_methods` that:

1. Takes a Python object as an argument.
2. Uses the `inspect.getmembers` method to retrieve all of the **methods** associated with the object.
3. Returns the number of methods associated with the object.

The function should take the Python object as an argument and return the number of methods associated with it.

You can test your function by creating any Python object and passing it to the function. 
For example, create a class or use a built-in object like a list or string.
"""

import inspect

def count_object_methods(python_object):
    """
    Returns the number of methods associated with an object.
    """
    
    # Use an introspection method to get all the methods associated with the object.
    obj_methods =

    # Get the number of methods
    num_methods =

    # Return the number of methods
    return num_methods

if __name__ == "__main__":

    # Create a sample object (for testing, you can change this to any other object)
    obj = []

    # Call the function with the object and print the result.
    print(count_object_methods(obj))
