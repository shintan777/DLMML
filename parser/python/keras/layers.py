import json
import os
import sys
from pprint import pprint


symbol_table = {
    'Conv2D' : 'model.add(Conv2D())',
    'MaxPooling2D' : 'model.add(MaxPooling2D())',
    'Dense': 'model.add(Dense())',
    'Flatten': 'model.add(Flatten())',
    'sgd': 'opt = SGD(lr=0.001, momentum=0.9)',
}


def parse(input_dict):
    """
    Parser which adds layers (mostly)
    """
    try:
        # init_sequential()
        layers = input_dict['layers']
        generated_code = ''

        #TODO: Take care of indentation and stuff if making functions
        #TODO: Ordering in dict (work around -> ordered_dict)

        for layer in layers:
            name = layer.get('name', None)
            curr_layer = symbol_table[name]
            args = layer.copy()
            args.pop('name')
            args = str(args)
            curr_layer = curr_layer[:-2] + '**' + args + curr_layer[-2:]
            generated_code += curr_layer + '\n'
        print()
        return generated_code
    
    except Exception as e:
        print(e)
