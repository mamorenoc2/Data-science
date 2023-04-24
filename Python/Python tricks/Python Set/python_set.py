set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numers = {1, 2, 3, 4, 2}
print(set_numers)

set_type = {1, 'hola', False, 12.2}
print(set_type)

set_from_string = set('hola')
print(set_from_string)

# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print (set_from_tuples) # {'as', 'abc', 'cbv'}

# la podemos crear a partir de una lista
numbers = [1,2,3,1,2,3,4]
set_numbers= set(numbers)

print (set_numbers) # {1, 2, 3, 4}

# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers)