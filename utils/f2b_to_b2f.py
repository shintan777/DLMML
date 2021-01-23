import os
import json
import sys

sys.path.append("..")

from dev_server.connect_mongo import connect


def parse():
    """
    Converts the data from f2b to b2f format

    Parameter
    ----------
    f2b : dict
        The front end to backend json

    Returns
    ---------
    b2f : dict
        The backend to frontend json
    """
    f2b = {
	"Layer-1-Conv2D-filters": 32,
	"Layer-1-Conv2D-kernel_size": [3, 3],
	"Layer-1-Conv2D-activation": "relu",
	"Layer-1-Conv2D-padding": "same",
	"Layer-1-Conv2D-input_shape": [200, 200, 3],

	"Layer-2-MaxPooling2D-pool_size": [2, 2],

	"Layer-3-Flatten-": {},

	"Layer-4-Dense-units": 128,
	"Layer-4-Dense-activation": "relu",
	"Layer-4-Dense-kernel_initializer": "he_uniform",

	"Layer-5-Dense-units": 1,
	"Layer-5-Dense-activation": "sigmoid",

	"dataset-type": "image",
	"dataset-path": "../data/dogs_and_cats",

	"image-augment-rotation_range": 40,
	"image-augment-width_shift_range": 0.2,
	"image-augment-height_shift_range": 0.2,
	"image-augment-horizontal_flip": "True",
	"image-augment-rescale": 0.0039215,

	"image-params-target_size": [200, 200],
	"image-params-batch_size": 64,
	"image-params-class_mode": "binary",

	"optimizer": "sgd",
	"loss": "binary_crossentropy",
	"metrics": [
		"accuracy"
	],
	"epochs": 5,

	"verbose": 1,
	"plot": "True",
	"save_plots": "True",
    "lib": "keras",
    "lang": "python"
    }

    db = connect()
    collection = db['schema']
    b2f = {}

    for key, value in f2b.items():
        elements = key.split('-')
        
        if elements[0] == 'Layer':
            # TODO: deduplicate layers with same name
            if not b2f.get(elements[2]):
                layer = collection.find_one({"name": elements[2], "lib": f2b['lib'], "lang": f2b['lang'] })
                del layer['_id']
                b2f[elements[2]] = layer
            b2f[elements[2]][elements[3]]['value'] = value

        elif len(elements) == 1:
            b2f[key] = value
        else:
            # TODO: Parse keys other than layers  
            pass

    print(b2f)
    return b2f


if __name__ == "__main__":
    parse()