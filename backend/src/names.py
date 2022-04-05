import random


def upstanding_name(players):
    name = create_silly_name()
    while name in players:
        name = create_silly_name()
    return name


def create_silly_name():
    random_number = random.randint(1, 250)
    if random_number == 1:
        return 'Paddington Bear'
    name = random.choice(first_names) + ' ' + random.choice(last_names)
    return name


first_names = ['Erinold', 'Meribeth', 'Archingham', 'Pethlemew', 'Euphrenia', 'Cheerio', 'Walter', 'Betsy', 'Prince',
               'Bengulburt']
last_names = ['Mornington', 'Laughtsworth', 'Duceistershire', 'Thewsithbury', 'Grubblestinch', 'Topham-Hatt',
              'Cusperterch']
