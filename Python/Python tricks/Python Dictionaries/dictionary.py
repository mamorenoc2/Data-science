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
print(unit_of_list)

