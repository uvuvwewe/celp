from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS

import random
import json
import pandas as pd
import numpy as np
from pathlib import Path


# HELPERS
def create_similarity_matrix_categories(matrix):
    """Create a  """
    npu = matrix.values
    m1 = npu @ npu.T
    diag = np.diag(m1)
    m2 = m1 / diag
    m3 = np.minimum(m2, m2.T)
    return pd.DataFrame(m3, index = matrix.index, columns = matrix.index)


def get_data(id):
    for i in data:
        if i['business_id'] == id:
            return {'business_id' : id, 'stars' : i['stars'], 'name' : i['name'], 'city' : i['city'], 'adress' : i['address']}


# HELPERS


def recommend(user_id=None, business_id=None, city=None, n=10):
    """
    Returns n recommendations as a list of dicts.
    Optionally takes in a user_id, business_id and/or city.
    A recommendation is a dictionary in the form of:
        {
            business_id:str
            stars:str
            name:str
            city:str
            adress:str
        }
    """


    business_id = '-MsRvdPnuw6QuLn5Vxjruw'
    city = 'Westlake'
    n = 5







    data_folder = Path("data/westlake/")

    file_to_open = data_folder / "business.json"

    f = open(file_to_open)









    # Data inladen
    data = []
    for line in open(file_to_open, 'r'):
        data.append(json.loads(line))


    # Dezelfde stad
    same_city = []
    for i in data:
        if i['city'] == city:
            same_city.append(i['name'])

    # Zelfde ratings
    same_star_range = []
    teller = 0
    for i in data:
        if 4.1 <= i['stars'] <= 5.0:
            same_star_range.append(i['name'])


    # Zelfde categorie + lijst maken
    dict_categories = {}
    for i in data:
        dict_categories[i['business_id']] = i['categories'].split(', ')


    # Maak waarden in lijst per twee
    listos = []
    for i in dict_categories:
        for j in dict_categories[i]:
            listos.append([i, j])

    # Maak er een pandas-dataframe van
    df_categories = pd.DataFrame(columns=['bedrijf', 'soort'])
    for i in range(len(listos)):
        df_categories.loc[i] = listos[i]


    utility_matrix = df_categories.pivot_table(index = 'bedrijf', columns = 'soort', aggfunc = 'size', fill_value=0)
    similarity_matrix = create_similarity_matrix_categories(utility_matrix)

    #display(similarity_matrix)



    # Kijk of bedrijf similar is
    similarities = {}
    for column in similarity_matrix:
        for row in similarity_matrix:
            if 0 < similarity_matrix.loc[column][row] < 1:
                similarities[(column, row)] = {'value' : similarity_matrix.loc[column][row]}


    # Maak paren met gelijkenis
    possibilities = {}
    for Tuple in similarities:
        if business_id in Tuple[0]:
            possibilities[Tuple[1]] = similarities[Tuple]['value']
        if business_id in Tuple[1]:
            possibilities[Tuple[0]] = similarities[Tuple]['value']

    # Kijk welke meest gelijke er zijn, en hier de top n van nemen
    possible = pd.Series(possibilities)
    possible = possible.sort_values(ascending=False)
    possible_id = possible.index.tolist()[:n]

    # Maak laatste lijstje om te returnen
    finalreturn = []
    for i in possible_id:
        finalreturn.append(get_data(i))

    return finalreturn


    # Genereer random stad indien geen city gegeven
    if not city:
        city = random.choice(CITIES)
    return random.sample(BUSINESSES[city], n)
