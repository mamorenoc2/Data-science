#Numeros del 1 al 10
numbers = [i for i in range(1,11) ]
print(numbers)

numbers_by_two = [i*2 for i in range(1,11)]
print(numbers_by_two)

#Programa, multiplicar un numero si este es par con list comprehesions de 1 a 20
numbers_2 = [i*2 for i in range(1, 20) if i%2 == 0]
print(numbers_2)
