"""Train pipeline to contain compile, train and eval functions."""
import json
import os
import sys
from pprint import pprint

from .symbol_table import symbol_table


def compile_model(inputs):
    """
    Compile model along with adding optimizer.
    
    Parameters
    ------------
    inputs = dict
        Parse input json from post request body
    
    Returns
    --------
    compile_string: str(multiline)
        get the optimizer and compile the model   
    """
    try:
        opt = inputs.get("optimizer", "sgd")
        opt_code = symbol_table[opt]
        # let loss and metrics be a compulsory fields for the user?
        loss = inputs.get("loss")
        metrics = str(inputs.get("metrics"))

        return '\n' + opt_code + '\n' + \
            "model.compile(optimizer=opt, loss='{}', metrics={})".format(loss, metrics)

    except Exception as e:
        print(e)


def train_evaluate_model(inputs):
    """
    Add code required to train and evaluate model.

    Works only if:
        - train_data's generator is train_generator
        - test_data's generator is called test_generator
        - Only epochs and verbose taken from json
    
    Parameters
    -----------
    inputs : dict
        Parsed input json from post request
    
    Returns
    --------
    fit_generator : str(multiline)
        Train the model and store the result in the variable history
    
    eval_generator : str(multiline)
        Evaluate the model performance

    """
    try:
        epochs = inputs.get('epochs', 20)   # decide default
        verbose = inputs.get('verbose', 0)
        fit_generator = \
"""

print("\\n\\n ==========Fitting Model========== \\n")
history = model.fit_generator(
                    train_generator,
                    steps_per_epoch=len(train_generator),
                    validation_data=test_generator,
                    validation_steps=len(test_generator),
                    epochs={},
                    verbose={}
                )
""".format(epochs, verbose)

        eval_generator = \
"""

print("\\n\\n ==========Evalutating Model========== \\n")
_, acc = model.evaluate_generator(test_generator,
                                  steps=len(test_generator),
                                  verbose={})
print('\\n\\nACCURACY:  %.3f \\n\\n' % (acc * 100.0))
""".format(verbose)
        return fit_generator + eval_generator
    except Exception as e:
        print(e)