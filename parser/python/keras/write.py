import json
import os
import sys
from pprint import pprint

from .imports import get_imports
from .init import init_sequential
from .inputs import image_input
from .layers import parse
from .train_pipeline import compile_model, train_evaluate_model
from .visualize import add_plots_and_summary, plot_and_summarize_model


def write_to_file(file_name, input_dict, output_dir = ''):
    """
    Call all the functions to generate test.py file.

    Parameters
    -----------
    file_name: string (with extension), generated code 
               will be saved as file_name in the test dir
    input_dict: Dict generated by parsing json to make 
                nested dict
    output_dir : str
       
    Returns
    ---------
    Get the final file with generated code.
    """
    try:
        inputs = input_dict
        with open(output_dir + file_name, 'w') as f:
            f.write(get_imports())
            f.write(add_plots_and_summary())
            f.write(image_input(inputs))
            f.write(init_sequential())
            f.write(parse(inputs))
            f.write(compile_model(inputs))
            f.write(train_evaluate_model(inputs))
            f.write(plot_and_summarize_model(inputs))
        print("Code generated in file test/" + file_name)
    except:
        print("Exception occured")
