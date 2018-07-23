import os
import sys
import psycopg2
import pprint

usuarios={}

def menu_principal():
	print("Bienvenido a Free Store")
	print("0) Registrarse")
	print("1) Ingresar")
	print("3) Salir")
	s= int(input("¿Que desea hacer?: "))

	if s == 1:
		print("Ingresar")
		print("")
		Usuario.Login()
	elif s == 0:
		print("Registrarse")
		print("")
		Usuario.registro()
		return menu_principal()
	elif s == 2:
		sys.exit()
	else:
		print("Por favor digite una respuesta correcta")
		menu_principal()
		return s

class Usuario:
	def __init__(self,username,password,nombre,apellido,edad,numtarj,paypal,paypalcont):
			self.username = username
			self.password = password
			self.nombre = nombre
			self.apellido = apellido
			self.edad = edad
			self.numtarj = numtarj
			self.paypal = paypal
			self.paypalcont = paypalcont

	def registro ():
		username = input("Nombre de ususario: ")
		password = input("Contraseña: ")

		nombre = input("Ingrese su nombre: ")
		apellido =input("Ingrese su apellido: ")
		edad=input("Ingrese su edad: ")
		numtarj=input("ingrese su numero de trajeta de credito: ")
		paypal=input("Ingresa un correo para tu cuenta de PayPal: ")
		paypalcont=input("Ingrese la contraseña de la cuenta de paypal: ")
		usuario1 = Usuario(username,password,nombre,apellido,edad,numtarj,paypal,paypalcont)
		usuarios[usuario1.username] = usuario1
		return usuario1

	def __str__(Usuario):
		s=str(Usuario.username)+str(Usuario.password)
		return s

	def Login():

		user = input("Ingresa el nombre de usuario: ")
		passw = input("Ingrese su contraseña: ")
		if (usuarios[user].password == passw):
			print("Bienvenido", usuarios[user].username)
			print("Usted desea ingresar como: ")
			print("1) comprador")
			print("2) vendedor")

		opcion = int(input("¿Como desea ingresar?: "))

		if opcion == 1:
			print("Usted ha ingresado como comprador")
			print("")
			usuario_buyer.menu_buy()
		elif opcion == 2:
			print("Usted ha ingresado como comprador")
			print("")
			usuario_seller.menu_sell()
		else:
			print("Por favor, escriba una opcion correcta")
			Login()
			return opcion


class usuario_seller():
	def menu_sell():
		print("Usted se encuentra en su menu principal")
		print("")
		print("1) Agregar articulo")
		print("2) Modificar articulo")
		print("3) Ver articulo")
		print("4) Eliminar articulo")
		print("5) Salir")
		print("6) Regresar al inicio")
		opc = int(input("¿Que opcion desea realizar?: "))

		if opc == 1:
			agregar()
		elif opc == 2:
			modificar()
		elif opc == 3:
			ver_art()
		elif opc == 4:
			print("Hasta luego")
		elif opc == 5:
			sys.exit()
		elif opc == 6:
			menu_principal()
		else:
			print("Por favor, digite una respuesta valida")
		menu_sell()
		return opc

	def __init__(self,name,precio,descrip,cantidad):
			self.name = name
			self.precio= precio
			self.descrip = descrip
			self.cantidad = cantidad

	def agregar():

	    prodConexion="host='localhost' dbname='Tienda' user='postgres' password='Mary2115'"   #Variable conexion SQL
	    art = psycopg2.connect(prodConexion)
	    artCursor = art.cursor()
	    print("Usted se encuentra en el menu de agregar articulos")
	    print("")
	    name = input("Escriba el nombre del articulo que desea vender: ")
	    precio = input("Escriba el precio del articulo: ")
	    descrip = input("Escriba una descripcion del producto, con la finalidad de ayudar a los compradores a conocer su producto: ")
	    cantidad = int(input("¿Cuantos articulos va ha poner en venta?: "))
        artCursor.execute("INSERT INTO articulo(nombre, precio, descripcion, cantidad) VALUES ('"+name+"', '"+precio+"', '"+descrip+"', '"+cantidad+"')")
        art.commit()
        art.close()

		print("Articulo agregado.")
		print("")
		print("[a] Agregar otro articulo")
		print("[v] Volver al menu.")
		print("[s] Salir")

		resp =  input("¿Que desea hacer?: ")

		if resp == "v":
			menu_sell()
		elif resp == "a":
			agregar()
		elif opcion == "s":
			sys.exit()   #para salir
		else:
			print("Respuesta no valida")
			return resp
menu_principal()
	#def modificar():
		#print("Modificar articulo/os")
		#print("")
		#print("Nombre\t\tPrecio\t\tDescripcion\t\tCantidad")
		#print("")

		#for articulo in cursor:
			#print(str(articulo[0])+"\t\t"+articulo[1]+"\t\t"+articulo[2])
			#print("")

		#nombre = input("Digite el nuevo nombre: ")
		#precio = input("Digite el nuevo precio: ")
		#descrip= input("Digite la descripcion del articulo que desea modificar: ")
		#cantidad=input("Digite la cantidad de articulos en venta: ")

		#print("")
		#print("Articulo modificado")
		#print("")
		#print("[m] Modificar otro articulo")
		#print("[s] Salir")

		#resp =  input("¿Que desea hacer?: ")

		#if resp == "v":
			#menu_sell()
		#elif resp == "m":
			#modificar()
		#elif opcion == "s":
			#sys.exit()   #para salir
		#else:
			#print("Respuesta no valida")
			#return resp


	def ver_art():
		prodConexion="host='localhost' dbname='Tienda' user='postgres' password='Mary2115'"
		art=psycopg2.connect(prodConexion)
        artCursor=art.cursor()
        artCursor.execute("SELECT * FROM articulo")
        art.commit()
		print("Sus articulos son los siguientes:")
		print("")
		print("\t idarticulo \tNombre \tPrecio \tDescripcion \t Cantidad")

		for articulo in cursor:
			produ='\t'+str(articulo[0])+ '\t' +str(articulo[1])+"\t"+str(articulo[2])+"\t"+str(articulo[3])+"\t"+str(articulo[4])           #en la posicion cero se captura el codigo, como una cadena para que me vaya dando los datos de cada columna de la tabla
			print(str(produ))
			print("")

		produ=artCursor.fetchall()
		#imprimir productos
		pprint.pprint(produ)
        art.close()

		#print("Articulos en Tienda.")
		#print("")
		#print("[v] Ver los demas articulos")
		#print("[r] Regresar al menu")
		#print("[s] Salir")

		#resp =  input("¿Que desea hacer?: ")

		#if resp == "r":
			#menu_sell()
		#elif resp == "v":
			#ver_artic()
		#elif opcion == "s":
			#sys.exit()   #para salir
		#else:
			#print("Respuesta no valida")
			#return resp

	#def elim_art():
		#print("Eliminar articulo/os")
		#print("Nombre\t\tPrecio\t\tDescripcion\t\tCantidad")
		#print("")



#menu_principal()
