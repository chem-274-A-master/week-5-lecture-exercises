"""
This exercise tests your ability to inspect the global namespace.

Your task is to complete the function `find_variable_name` that takes in a variable value.
The function should return the name of the variable that has that value in the global namespace.

For example, if you have a variable `my_variable` with the value `"my_secret"`, the function should return `"my_variable"` 
when called with the value `"my_secret"`.

Fill in the function `find_variable_name` to complete this task.
"""

def find_variable_name(variable_value):
    
    # Your code here
    pass

if __name__ == "__main__":

    ## Do not modify the code below - used for testing
    import random
    import string

    random.seed(99)

    globals()[''.join(random.choice(string.ascii_letters) for i in range(10))] = "my_secret"
    print(find_variable_name("my_secret"))

