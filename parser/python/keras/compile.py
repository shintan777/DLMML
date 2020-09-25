"""
write a func compile_model() which takes ip(input-dict) and compiles the model acc to layers
returns 0, None if exec successfully else 1, error

"""
import json
import os
import sys
from pprint import pprint

from .imports import get_imports
from .init import init_sequential
from .inputs import image_input
from .layers import parse
from .train_pipeline import compile_model
from .visualize import add_plots_and_summary


def test_compile_model(input_dict):
    """
    input_dict - dictionary of nested json
    """
    with open('compile_test,py', 'w') as f:
        try:
            inputs = input_dict
            f.write(get_imports())
            f.write(add_plots_and_summary())
            f.write(image_input(inputs))
            f.write(init_sequential())
            f.write(parse(inputs))
            f.write(compile_model(inputs))
            os.system("python compile_test.py")
            print("Model compiled successfully")
        except Exception as e:
            print("Error - ", e)
      