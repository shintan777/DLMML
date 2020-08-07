class MakeDict:
    """
    Makes nested dict, required to process, parse and write code

    Input: 
    ------
    inp_json : Input json (str), body of post request ideally
    
    Return:
    --------
    dict obj -> Nested dict object
    """

    def __init__(self, inp_json):
        self.layers = []
        self.image = {'augment':{},
                   'params': {}}
        self.dataset = {}
        self.pointer = 0
        self.inp_json = inp_json
        self.nestedJSON = {}

    def parse_layer(self, key):
        [_, position, name, param] = key.split('-')
        position = int(position)

        if position > self.pointer:
            self.pointer = position
            self.layers.append({'name': name})
            if param != '':
                self.layers[self.pointer-1][param] = self.inp_json.pop(key)
            else:
                self.inp_json.pop(key)
        else:
            self.layers[self.pointer-1][param] = self.inp_json.pop(key)

    def parse_image(self, key):
        [_, _, arg] = key.split('-')
        try:
            if 'augment' in key:
                self.image['augment'][arg] = self.inp_json.pop(key)
            elif 'params' in key:
                self.image['params'][arg] = self.inp_json.pop(key)
            else:
                print("image key not recognised")
        except Exception as e:
            print(e, key)

    def parse_dataset(self, key):
        _, arg = key.split('-')
        self.dataset[arg] = self.inp_json.pop(key)
        
    def merge(self):
        self.nestedJSON['layers'] = self.layers
        self.nestedJSON['dataset'] = self.dataset
        self.nestedJSON['image'] = self.image
        self.nestedJSON.update(self.inp_json)

    def parse(self):
        for key in list(self.inp_json.keys()):
            if 'Layer' in key:
                self.parse_layer(key)
            if 'image' in key:
                self.parse_image(key)
            if 'dataset' in key:
                self.parse_dataset(key)
        self.merge()
        return self.nestedJSON
