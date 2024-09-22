"""
This exercise tests the object introspection methods you have learned so far.

Your task is to write a function called `get_source_code` that:

1. Takes a Python method as an argument (e.g., `object.method`).
2. Uses introspection techniques to retrieve the **source code** of the passed method.
3. Stores the source code in a variable called `source` and returns it.

You can test your function by passing in a method, such as a method from a custom class.
Note that the source code of built-in methods cannot be retrieved and will raise a `TypeError`.

See main section for example usage.
    
"""

import inspect

def get_source_code(python_method):
    """
    Returns the source code of a Python method.
    """

    # Use an introspection method to get the source code of the method.
    source = 
        
    # Return the source code
    return source

if __name__ == "__main__":

    # Retrive source code of a method from numpy
    source_code = get_source_code(np.mean)

    # Print the source code for the np.mean method
    print(source_code)
