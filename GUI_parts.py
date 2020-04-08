import pandas as pd
from pandas import Series
import numpy as np
from tensorflow.keras.models import load_model

def load_dictionary():
    dict_path = 'Material_Dictionary.csv'
    dictionary = pd.read_csv(dict_path, header=0)
    dictionary.sort_values("Material", inplace=True)
    return dictionary

def Materals_list():
    dictionary = load_dictionary()
    dict_ceramic = dictionary[dictionary["Group"]=='ceramic']
    dict_metal = dictionary[dictionary["Group"]=='metal']
    dict_polymer = dictionary[dictionary["Group"]=='polymer']
    List_ceramic = dict_ceramic["Material"].tolist()
    List_metal = dict_metal["Material"].tolist()
    List_polymer = dict_polymer["Material"].tolist()
    return List_ceramic, List_metal, List_polymer

def encode_material(material):
    dictionary = load_dictionary()
    code_row = dictionary[dictionary["Material"]==material]
    code = code_row.drop(["Group", "Material", "index"], axis=1)
    return np.array(code)

def encode_group(group):
    category = {'ceramic': [1, 0, 0],
                'polymer': [0, 0, 1],
                'metal': [0, 1, 0]}
    group_code = np.array(category[group])
    return group_code

def encode_fluid(fluid):
    category = {'TBA': [1, 0, 0],
                'water': [0, 0, 1],
                'camphene': [0, 1, 0]}
    fluid_code = np.array(category[fluid])
    return fluid_code

def predict_porosity(inputs):
    model = load_model('model.h5')
    porosity = model.predict(inputs)
    return porosity
