from data import CITIES, BUSINESSES, USERS, REVIEWS, TIPS, CHECKINS

import random

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

    # Maak een lijstje indien city gegeven

    if city:
        top = USERS
        for City in top:
            print(City)


    list_of_dicts = []
        #for i in range(n):

         #   list_of_dicts.append("iets")

    #    return list_of_dicts

    # Genereer random stad indien geen city gegeven
    if not city:
        city = random.choice(CITIES)
    return random.sample(BUSINESSES[city], n)
