# (enumerate)  Ciclos con contador
for i, v in enumerate(['a', 'b', 'c']):
 print(i, v)

#Imprime
#0 a
#1 b
#2 c

# (zip) Recorrer 2 listas al mismo tiempo

pares    = [2,4,6]
impares  = [1,3,5]

for a, b in zip (impares, pares):
 print(a,b)

#Imprime
#1,2
#3,4
#5,6  

#More: https://docs.python.org/3/tutorial/datastructures.html#looping-techniques
