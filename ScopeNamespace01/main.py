"""
This exercise tests your ability to inspect the global namespace.

Your task is to complete the function `find_variable_name` that:

1. Inspects the global namespace to find the name of the variable with the value "my_secret".
2. Returns the name of the variable as a string.

Fill in the function `find_variable_name` to complete this task.
"""

def find_variable_name():
    # YOUR CODE HERE

    return variable_name

if __name__ == "__main__":
    # Example global variable for testing
    my_variable = "my_secret"
    
    # Call the function to find the variable name and print the result
    # this will print "my_variable" for this example.
    variable_name = find_variable_name()
    print(variable_name)
