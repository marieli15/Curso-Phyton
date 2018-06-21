import os

listadatos = []
listadatos1 = []
listadatos2 = []

nom = input("¿Como te llamas?: ")
ape = input("Escribe tu primer apellido: ")
edad = input("¿Que edad tiene?: ")

listadatos1.append(nom)
listadatos1.append(ape)
listadatos1.append(edad)
print(listadatos1)

print("¿Quieres agregar otro usuario?: ")
opcion = input("1) si, 2)no\n")

while (opcion == "1"):
	nom = input("Ingresa tu nombre:")

	ape = input("Ingresa tu apellido:")

	edad = input("ingresa tu edad:")

	listadatos2.append(nom)

	listadatos2.append(ape)

	listadatos2.append(edad)
	print(listadatos2)

	print("¿Deseas parar?: ")
	continuar = input("1) si, 2)no\n")

	if(continuar == "2"):
		nom = input("Ingresa tu nombre:")

		ape = input("Ingresa tu apellido:")

		edad = input("ingresa tu edad:")

		listadatos.append(nom)

		listadatos.append(ape)

		listadatos.append(edad)

	else:
		print(listadatos)
		listdat = [listadatos1, listadatos2,  listadatos]
		print(listdat)
		os.system("pause") #pausa la pantalla para que no se cierre la ventana

		break 

		

if(opcion == "2"):

	print(listadatos1)

	os.system("pause") 
	