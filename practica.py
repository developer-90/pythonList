from cliente import Cliente

print('Práctica de Collections')
#crear una lista de frutas
frutas=['naranja','limon','platano','mandarina','uva','manzana','pera','aguacate','chirimoya','banana','ciruela','melocoton','albaricoque','lima']
#muestra las frutas ordenadas alfabeticamente
frutas.sort()
for f in frutas:
    print(f)
#añade a las frutas, macedonia
frutas.append('macedonia') # insert puedes añadir un elemento en un posicion concreta
for f in frutas:
    print(f)
#tengo un error. porque hay que poner precios a las frutas. con decimales
#crea un dict nuevo con las frutas y los precios
frutas_dict={'melon':9.95,'manzana':15,'pera':14.95,'sandia':10.25}
#mostrar el precio medio
total=0 #totalizador
for precio in frutas_dict.values():
    total+=precio
    print(precio)
print(f'el total es {total}')
print(f'el total es {total/len(frutas_dict)}')

# guardar 5 paises del mundo. No es necesario añadir mas paises. Los quiero ordenar alfabeticamente
# lista : elegido y puede añadir. pues vale necesito sort
# tupla : mejor opcion. NO permite añadir, pero si permite sort
# set : no sirve, porque no permite ordenar
# dict : descartado porque no pedimos key value

paises=('españa','francia','belgica','rumania','irlanda')
for pais in paises:
    print(pais.lower())

# 3 alumnos con sus notas : con decimales
# muestra unicamente los alumnos cuya nota >= a 5
notasAlumnos={'alumno1':8.5,'alumno2':2.8,'alumno3':0.5,'alumno4':9.8}
for alumno in notasAlumnos.items():
    if alumno[1] >= 5:
        print(alumno[0])

# listado de clientes. 3 clientes : nombre, ciudad, facturacion
#POO
#String, int, float, boolean..
#usamos objetos : cliente es un objeto definido por nosotros
cliente1=Cliente('juan','madrid',1500)
cliente2=Cliente('maria','sevilla',2570)
cliente3=Cliente('laura','madrid',1500)

clientes=[cliente1,cliente2,cliente3]
for cliente in clientes:
    print(cliente.nombre,'-',cliente.ciudad,'-',cliente.facturacion)