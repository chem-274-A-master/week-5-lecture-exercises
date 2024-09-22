"""
This exercise tests the object introspection methods you have learned so far.

Your task is to complete the function `count_object_callables` that:

1. Takes a Python object as an argument.
2. Uses the `inspect.getmembers` method to retrieve all of the **callable** members associated with the object.
   - A callable is any object that can be called, including methods and built-in functions.
3. Returns the number of callables associated with the object.

Instead of using `inspect.ismethod` as the second argument to `inspect.getmembers`, you can use `callable` to find all callables related to the object.

The function should take the Python object as an argument and return the number of callables associated with it.

You can test your function by creating any Python object and passing it to the function.
For example, create a class or use a built-in object like a list or string.
"""

import inspect

def count_object_callables(python_object):
    """
    Returns the number of callable members associated with an object.
    """
    
    # Use an introspection method to get all the callable members associated with the object.
    # Replace 'inspect.ismethod' that was shown in the Lecture Exercise video with 'callable'
    obj_callables = 
    
    # Get the number of callable members
    num_callables = 

    # Return the number of callables
    return num_callables

if __name__ == "__main__":

    # Create a sample object (for testing, you can change this to any other object)
    obj = []

    # Call the function with the object and print the result.
    print(count_object_callables(obj))
