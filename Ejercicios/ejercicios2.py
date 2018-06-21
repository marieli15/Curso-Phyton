listaNombre = ["Gerardo", "Damian", "Cesar"]
print(listaNombre)

#Agregar elementos a la listaNombre
listaNombre.append("Kenedy")
print(listaNombre)

#Ver elementos de la lista
print(listaNombre[0])
print(listaNombre[3])
print(listaNombre[0],",",listaNombre[1])
#
#ver elementos de la lista
newlista = listaNombre[0:2]
print(newlista)
newlista = listaNombre[0:6:4]
print(newlista)
newlista = listaNombre[1:6:4]
print(newlista)

#Agregar eleentos 
listaNombre = (0,"Juan")
listaNombre = (3,"Irais")
print(listaNombre)

#borrar elementos
listaNombre.remove("Juan")
print(listaNombre)
listaNombre.remove("Cesar")
print(listaNombre)

#Buscar el indice del elemento de la lista
print(listaNombre.index("Carlos"))
print(listaNombre.index("Pepe"))

#Tuplas
tuplaNombres = ("Gerardo", "Cesar")
print(tuplaNombres)
print(tuplaNombres[0])
print(tuplaNombres[1])
#tuplaNombres.append("Carlos")
#tuplaNombres.

#regresando a lista
#ordenar lista
listaNumeros = [3,6,4,2,3,7,4,3,4,7]
nuevalista = sorted(listaNombre)
print(nuevalista)
print(listaNumeros)
print(sorted(listaNumeros))

