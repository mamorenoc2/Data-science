# A dictionary begins and ends with curly braces { and }.
# Each item consists of a key("avocado toast") and a value(6).
# Each key: value pair is separated by a comma.

# Values can be of any type. We can use a string, a number, a list,
#  or even another dictionary as the value associated with a key
#EX
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": [
    "Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

#We can also mix and match key and value types. For example:
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

#--------------------------------------------------   ADD  ------------------------------------------------#
#To add a single key:value pair to dictionary, we can use:
#dictionary[key] = value
#EX
numbers = {'one':1, 'two':2, 'three':3}
#print('This is', numbers, 'before')
numbers['four'] = 4
#print('This is', numbers, 'after')

#------------------------------------------------  UPDATE  ----------------------------------------------#

# If we wanted to add multiple key : value pairs to a dictionary 
# at once, we can use the .update() method.
#EX:
home_temp = {'apartado':36, 'medellin':27}
#print('This is', home_temp, 'before')
home_temp.update({'cartagena': 29, 'corea del sur': 26})
#print('This is', home_temp, 'after')

#------------------------------------------------  OVERWRITE  ----------------------------------------------#

#We can overwrite the existing value in similar way to add a key
#EX:
numbers_2 = {'uno': 1, 'dos': 6}
#print('This is', numbers_2, 'before')
numbers_2['dos'] = 2
#print('This is', numbers_2, 'after')

#------------------------------------------- LIST COMPREHENSIONS  ------------------------------------------#

#Let’s say we have two lists that we want to combine into a dictionary,
#Python allows you to create a dictionary using a list comprehension, with this syntax:

#name_of_dictionary = {key:value for key, value in zip(list_1, list)}

numbers_3_l = ['uno', 'dos', 'tres']
numbers_3_n = [1,2,3]

unit_of_list = {key:value for key, value in zip(numbers_3_l, numbers_3_n)}
#print(unit_of_list)


#------------------------------------------- PRINT VALUES  ------------------------------------------#

numbers_4 ={'Pares': [2,4,6,8], 'Impares':[1,3,5,7]}
#print(numbers_4['Pares'])


#--------------------------------------------  TRY / EXCEPT  -----------------------------------------#

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
                    "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")


#----------------------------------------------  GET  ----------------------------------------------#
#Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation.
# If the key you are trying to .get() does not exist, it will return None

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
                    "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
#print(building_heights.get("Shanghai Tower"))

#this line will return None:
#print(building_heights.get("My House"))


#You can also specify a value to return if the key doesn’t exist. 
#print(building_heights.get('Kilimanjaro', 'No Value'))
#print(building_heights.get('Kilimanjaro', 0))


#----------------------------------------------  POP  ----------------------------------------------#
#Use .pop() to return the value and also remove that pair from the dictionary
#Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary

numbers_5 = {'uno':1, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5}
# print(numbers_5)
# print(numbers_5.pop('cinco', 'no existe'))
# print(numbers_5)

#------------------------------------PRINT MULTIPLE DICT KEYS ---------------------------------------#

#Dictionaries also have a .keys() method that returns a dict_keys object. A dict_keys object is a view object, 
#which provides a look at the current state of the dictionary, without the user being able to modify anything. 
#The dict_keys object returned by .keys() is a set of the keys in the dictionary. 
#You cannot add or remove elements from a dict_keys object, but it can be used in the place of a list for iteration:

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()


#------------------------------------PRINT MULTIPLE DICT VALUES ---------------------------------------#

#Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object 
#but for values!) with all of the values in the dictionary

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for i in num_exercises.values():
  total_exercises += i
print(total_exercises) 

#------------------------------------PRINT MULTIPLE DICT ITEMS ---------------------------------------#

#You can get both the keys and the values with the .items() method. Like .keys() and .values(),
#  it returns a dict_list object. Each element of the dict_list returned by .items()


