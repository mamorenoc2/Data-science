import random
countries = ['col', 'mex', 'bol', 'pe']

#Diccionarios con condicionales#
population_dict = {country: random.randint(1,100) for country in countries}

population_less_30 = {country: population for (country, population) in population_dict.items() if population < 30}

print(population_dict)
print(population_less_30)

#Diccionarios con texto