#diccionarios de numeros pares
dict = {}
for i in range(1,10):
  dict[i] = i*2

#list comprehesions in dictionaries
dict_comprehesion = {i: i * 2 for i in range(1, 10) }
print(dict)
print(dict_comprehesion)


