"""
PURPOSE: TBD
"""

import requests
import json

import random

BASE_URL = "https://pokeapi.co/api/v2/"

# build standard team of 6 pokemon
team_list = []

while (not team_list) or (len(team_list) != 6):

    # get random pokemon
    id = random.randint(1, 100)

    response = requests.get(BASE_URL + "pokemon/" + str(id))
    # print(response.status_code)

    info = json.loads(response.text)

    name = info["forms"][0]["name"]

    # TODO: fix this logic, hacky
    if not team_list:
        team_list.append(name)

    elif name not in team_list:
        team_list.append(name)

    else:
        continue

print(team_list)
