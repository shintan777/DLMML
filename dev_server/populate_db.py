import os
import json

from connect_mongo import connect


def populate(lang, lib):
    """
    Populate database with backend to frontend schema
    """

    db = connect()
    collection = db['schema']
    with open('schema' + os.sep + 'backend_2_frontend_schema.json', 'r') as f:
        data = json.load(f)

    data_list = []
    for layer in data.keys():
        name = layer
        value = data.get(name, {})
        value['name'] = name
        value['lang'] = lang
        value['lib'] = lib
        data_list.append(value)

    collection.insert_many(data_list)
    print("Backend Schema written to db successfully")


if __name__ == "__main__":
    lang = "python"
    lib = "keras"
    populate(lang, lib)
