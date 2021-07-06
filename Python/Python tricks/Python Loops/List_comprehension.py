# ------------------------ esquema de la lista de comprensiones------------------------------------
# [operacion for elemento in lista]
#Ejemplo, aumentar la temperatura 20 centigrados
temperatura = [-5, 29, 26, -7, 1, 18, 12, 31]

temperatura_ajustada = [i+20 for i in temperatura]
print(temperatura_ajustada)

# lista = temperatura
# elemento = i
# operación = i + 1

# -------------- esquema de la lista de comprensiones y decisiones ---------------------------------
# [operacion for elemento in lista if condicion == True]


#Ejemplo 3

# -------------- sublistas de comprensiones ---------------------------------
original_list = [[1, 2], [3, 4],  [5, 6]]
new_list = [item1 + item2 for (item1, item2) in original_list]
print(new_list)


# -------------- Listas multiples de comprensiones ---------------------------------
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

sums = [a+b for (a,b) in zip(a, b)]
print(sums)

