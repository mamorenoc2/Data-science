#Write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest 
#hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, 
#lists, dictionaries, string manipulation, and return statements.

#---------------------------------------------------- DATA ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1- Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, 
# the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned
# environmentalist, you want to look at data about the most powerful hurricanes that have occurred.

# Begin by looking at the damages list. The list contains strings representing the total cost in USD($) caused by 34 category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h ))
# in the Atlantic region. For some of the hurricanes, damage data was not recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", 
# where B stands for billions (1000000000) and M stands for millions (1000000).

# Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded".
# Test your function with the data stored in damages.

millions = 0
bilions = 0
new_damages = []
index = 0
number = 0
def update_damage(damages):
  for i in damages:
    if i.find('M') != -1:
      index = i.find('M')
      number = float(i[:index])
      number *= 1000000
      new_damages.append(number)
    elif i.find('B') != -1:
      index = i.find('B')
      number = float(i[:index])
      number *= 1000000000
      new_damages.append(number)
    else:
      new_damages.append(i)
  return(new_damages)
  #print(new_damages)
  
# test function by updating damages
update_damage(damages)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2- Additional data collected on the 34 strongest Atlantic hurricanes are provided in a series of lists. The data includes:
#     names: names of the hurricanes
#     months: months in which the hurricanes occurred
#     years: years in which the hurricanes occurred
#     max_sustained_winds: maximum sustained winds (miles per hour) of the hurricanes
#     areas_affected: list of different areas affected by each of the hurricanes
#     deaths: total number of deaths caused by each of the hurricanes
# The data is organized such that the data at each index, from 0 to 33, corresponds to the same hurricane.
# For example, names[0] yields the “Cuba I” hurricane, which ouccred in months[0] (October) years[0] (1924).
# Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, 
# and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, 
# Damage, Death) about the hurricane.
# Example:
# Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165,
# 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}.
#Test your function on the lists of data provided.

# Create a Table
hurracanes_list = []
hurracanes_list = list(zip(months, years, max_sustained_winds, areas_affected, new_damages, deaths))
# Create and view the hurricanes dictionary
hurricanes_dict_names = {}
hurricanes_dict_names = {key:value for key, value in zip(names, hurracanes_list)}
#print(hurricanes_dict_names)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.
# Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists 
# containing a dictionary for each hurricane that occurred in that year.
# For example:
# the key 1932 would yield the value: 
# [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}].


# Organizing by Year
hurricanes_list_2 = []
hurricanes_list_2 = list(zip(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths))

# create a new dictionary of hurricanes with year and key
hurricanes_dict_years = {}

# Add / Append values to an existing key to a dictionary in python

for key, value in zip(years, hurricanes_list_2):
  # Check if key exist in dict or not
  if key in hurricanes_dict_years.keys():
    # Key exist in dict.
    # Check if type of value of key is list or not
    if not isinstance(hurricanes_dict_years[key], list):
      # If type is not list then make it list
      hurricanes_dict_years[key] = [hurricanes_dict_years[key]]
    # Append the value in list
    hurricanes_dict_years[key].append(value)
  else:
    hurricanes_dict_years.update({key:value})

#print(hurricanes_dict_years)

#----------------------------------------------------------  Counting Damaged Areas --------------------------------------------------------------------------------------------------------------------------------------
# 4. You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making 
# preparations for future hurricanes.
# Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary
# where the keys are the affected areas and the values are counts of how many times the areas were affected.

list_areas_affected = []
list_of_n_areas_affected = []
n_area_affected = 1

for i in areas_affected:
  list_areas_affected += i

for i in range(0, len(list_areas_affected)):
  list_of_n_areas_affected.append(1)

#print(list_of_n_areas_affected)

# create dictionary of areas to store the number of hurricanes involved in
dict_areas_affected={}

for key, value in zip(list_areas_affected,list_of_n_areas_affected):
  if key in dict_areas_affected.keys():
    value += 1
    dict_areas_affected.update({key:value})
  else:
    dict_areas_affected.update({key:value})
#print(dict_areas_affected)
