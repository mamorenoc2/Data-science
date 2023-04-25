# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# 1. Write a function that returns a new list of updated damages where the recorded data is converted to float
# values and the missing data is retained as "Damages not recorded". Test your function with the data stored in damages.

# write your update damages function here:

def update_damage_data(damages):

    conversion = {"M": 1000000, "B": 1000000000}
    update_damages = []

    for damage in damages:
        if damage[-1] == "M":

            update_damages.append(float(damage.strip('M'))*conversion["M"])

        if damage[-1] == 'B':
            update_damages.append(float(damage.strip('B'))*conversion['B'])

        if damage == 'Damages not recorded':
            update_damages.append(damage)

    return update_damages


update_damages = update_damage_data(damages)
# print(update_damages)

# write your construct hurricane dictionary function here:


def hurricanes_dictionary_data(names, months, years, max_sustained_winds, areas_affected, damages, deaths):

    hurricanes = {}
    num_hurricanes = len(names)

    for i in range(0, num_hurricanes):
        hurricanes[names[i]] = {'Name': names[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i],
                                "Areas Afected": areas_affected[i], 'Damage': damages[i], 'Deaths': deaths[i]}
    return hurricanes


hurricanes_dictionary = hurricanes_dictionary_data(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths)
# cls
# print(hurricanes_dictionary)


# write your construct hurricane by year dictionary function here:

def convert_names_to_years(hurricanes_dictionary):
    hurricanes_dictionary_by_years = {}
    for cane in hurricanes_dictionary:
        current_year = hurricanes_dictionary[cane]['Year']
        current_hurricane_data = hurricanes_dictionary[cane]
        if current_year not in hurricanes_dictionary_by_years:
            hurricanes_dictionary_by_years[current_year] = [
                current_hurricane_data]
        else:
            hurricanes_dictionary_by_years[current_year].append(
                current_hurricane_data)
    return hurricanes_dictionary_by_years


hurricanes_dictionary_years = convert_names_to_years(hurricanes_dictionary)
# print(hurricanes_dictionary_years)

# write your count affected areas function here:


def hurricane_affected_areas(hurricanes_dictionary):
    hurricane_dictionary_affected_areas = {}
    for cane in hurricanes_dictionary:
        for area_affected in hurricanes_dictionary[cane]['Areas Afected']:
            if area_affected not in hurricane_dictionary_affected_areas:
                hurricane_dictionary_affected_areas[area_affected] = 1
            else:
                hurricane_dictionary_affected_areas[area_affected] += 1
    return hurricane_dictionary_affected_areas


hurricanes_affected_areas = hurricane_affected_areas(hurricanes_dictionary)
# print(hurricanes_affected_areas)

# write your find most affected area function here:
def most_affected_area(hurricanes_affected_areas):
    max_num_hurricanes_afected = 0
    max_hurricanes_afected = ''
    most_hurricanes_afected = {}
    for i in hurricanes_affected_areas:
        if hurricanes_affected_areas[i] > max_num_hurricanes_afected:
            max_hurricanes_afected = i
            max_num_hurricanes_afected = hurricanes_affected_areas[i]
    most_hurricanes_afected[max_hurricanes_afected] = max_num_hurricanes_afected
    return most_hurricanes_afected

most_affected_area = most_affected_area(hurricanes_affected_areas)
print(most_affected_area)
# write your greatest number of deaths function here:


# write your catgeorize by mortality function here:


# write your greatest damage function here:


# write your catgeorize by damage function here:
