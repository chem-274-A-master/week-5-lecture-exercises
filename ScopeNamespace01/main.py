"""
This exercise tests your ability to inspect the global namespace.

Your task is to complete the function `find_variable_name` that:

1. Inspects the global namespace to find the name of the variable with the value "my_secret".
2. Returns the name of the variable as a string.

Fill in the function `find_variable_name` to complete this task.
"""

def find_variable_name():
    """
    Finds the name of the variable in the global namespace that has the value "my_secret".
    Returns the variable name as a string.
    """
    for var_name, var_value in globals().items():
        if var_value == "my_secret":
            return var_name
    return None

if __name__ == "__main__":
    # Example global variable for testing
    name = "my_secret"
    
    # Call the function to find the variable name and print the result
    variable_name = find_variable_name()
    print(variable_name)
