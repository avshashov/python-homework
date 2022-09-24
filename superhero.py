import requests


def smartest_hero(*args):
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    superhero_list = response.json()

    intelligence_hero = {}
    for hero in superhero_list:
        if hero['name'] in args:
            intelligence_hero[hero['name']] = hero['powerstats']['intelligence']

    return max(intelligence_hero, key=intelligence_hero.get)


print(smartest_hero('Hulk', 'Captain America', 'Thanos'))
