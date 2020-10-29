import json
import os
import sys
from pprint import pprint


def init_sequential():
    """
    Initialize the model.
    
    Returns
    ---------
    init_string: str
        define sequential model
    """
    try:
        return \
'\nmodel = Sequential()\n'

    except Exception as e:
        print(e)