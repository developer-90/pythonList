print('listas y colecciones')

# Crear listas, tuplas, set y diccionarios
lista=[10,'madrid',True,15.95,"valencia",10]
print(lista)
tupla=(10,'madrid',False)
conjunto={10,'madrid',True,15.95,"valencia",10} # no ordena ni soporta repeticion
print(conjunto)
diccionario={'lunes':15,'martes':18.5}
print(diccionario)

#Mutable vs Inmutable
#lista es mutable
lista[0]=14 # setter #update
print(lista[0]) # getter
print(lista[5])
lista.append('elemento añadido') #añadir elemento

#lista[6]='novedad' #add : no funciona si esta fuera de rango, si existe si funciona
for item in lista:
    print(item)
#tupla es inmutable

#set : no soporta duplicado. Son mutables
print('mnejando conjuntos')
conjunto.add('item añadido al conjunto')
for i in conjunto:
    print(i)
#ordenar
lista1=[2,8,9,6,5,4,74]
lista1.sort() # los elementos de la lista deben tener el mismo tipo de dato
lista1.reverse()
for x in lista1:
    print(x)

convertirlista=list(conjunto) # metodo list para hacer una conversion
