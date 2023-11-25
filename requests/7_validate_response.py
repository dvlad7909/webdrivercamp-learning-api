"""Find the mismatches in Planets data"""

import json
import requests
from pprint import pprint


def find_mismatched_data(url_, file_name_):
    """JSON validation function"""
    # YOUR CODE HERE

    with open(file_name_, 'r', encoding="utf-8") as json_file:
        file_data = json.load(json_file)

    planets = requests.get(url_)

    planets_expected = file_data['results']
    planets_actual = planets.json()['results']
    planet_assertion = {}
    keys = planets_expected[0].keys()

    for i in range(len(planets_expected)):
        ls_tmp = []

        for j in keys:
            if planets_expected[i][j] != planets_actual[i][j]:
                ls_tmp.append({j: {'Actual': planets_actual[i][j], 'Expected': planets_expected[i][j]}})
                name = planets_expected[i]['name']
                planet_assertion.update({name: ls_tmp})

    return planet_assertion


if __name__ == "__main__":
    url = "https://swapi.dev/api/planets/"
    file_name = "planets.json"

    pprint(find_mismatched_data(url, file_name))
