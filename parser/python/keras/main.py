import json
import os
import sys
from pprint import pprint

import write


def generate_code(inputs, filename = "test.py"):
    """Trigger function to generate code from JSON."""
    try: 
        write.write_to_file(filename, inputs)
        return 0, None
    except Exception as e:
        return 1, e

if __name__ == "__main__":
    print("Not yet implemented, please use generator for now...")
