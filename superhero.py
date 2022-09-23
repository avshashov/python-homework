import requests

response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
superhero_list = response.json()

intelligence_hero = {}
for hero in superhero_list:
    if hero['name'] in ('Hulk', 'Captain America', 'Thanos'):
        intelligence_hero[hero['name']] = hero['powerstats']['intelligence']

print(max(intelligence_hero, key=intelligence_hero.get))
