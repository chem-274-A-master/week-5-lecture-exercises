import inspect
import os
import sys
import subprocess

import pytest


def test_Introspection01():

    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Introspection01"))
    sys.path.append(exercise_dir)

    # Import the function
    from main import count_object_callables

    test_list = []
    test_tup = ()

    assert count_object_callables(test_list) == 46
    assert count_object_callables(test_tup) == 34

def test_Introspection02():

    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Introspection02"))
    sys.path.append(exercise_dir)

    # Import the function
    from main import get_source_code

    class MyClass:
        def my_method(self):
            return "Hello, World!"
        
    obj = MyClass()
    
    # Call the student's get_source_code function
    source_code = get_source_code(obj.my_method)

    # Verify that the source code is correct
    assert 'def my_method(self)' in source_code

def test_Introspection02_2():
    
    # add exercise directory to the path
    exercise_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Introspection02"))
    sys.path.append(exercise_dir)

    # Import the function
    from main import get_source_code

    # Use a built-in method and expect a TypeError
    with pytest.raises(TypeError):
        get_source_code(len)


def test_ScopeNamespace01():

   # Directory containing the student's Introspection01 exercise script
    script_dir = os.path.join(os.path.dirname(__file__), '..', 'ScopeNamespace01')

    # Path to the student's Python script (main.py)
    script_path = os.path.join(script_dir, 'main.py')

    # Run the student's script and capture the output
    result = subprocess.run(['python', script_path], capture_output=True, text=True)

    # Expected output
    expected_output = "zymMlopiWf"
    
    # Check if the output is correct
    assert expected_output == result.stdout.strip()