#Menu principal
usuarios = {}
listaregistro = []

def Menu():
	
	print("1) Registrarse")
	print("2) Ingresar")
	print("3) Salir")



def registro():

	usuarios[name] = listaregistro
	name = input("Nombre de ususario: ")
	password = input("Contraseña: ")
	listaregistro.append(name)
	listaregistro.append(password)
	nom=input("Ingrese su nombre: ")
	listaregistro.append(nom)
	ape=input("Ingrese su apellido: ")
	listaregistro.append(ape)
	edad=input("Ingrese su edad: ")
	listaregistro.append(edad)
	numtarj=input("ingrese su numero de trajeta de credito: ")
	listaregistro.append(numtarj)
	pp = []
	paypal=input("Ingresa un correo para tu cuenta de PayPal: ")
	pp.append(paypal)
	paypalcont=input("Ingrese la contraseña de la cuenta de paypal: ")
	pp.append(paypalcont)
	listaregistro = listaregistro.append(pp)

	while True:
		respuesta = input("¿Quieres agregar otro usuario? s/n " )
		if (respuesta == 'n'):
			print("Sus datos se han guardado exitosamente")
			break
			Menu()

		elif (respuesta == "s"):
			registro()
		else:
			print("opcion invalida")

#Para ingresar datos de usuario
def Login(usuarios):
	usuarios[username] = listaregistro	     
	user = input("Usuario: ")
	passw = input("Contrasenia: ")
	    
	    #Si el usuario esta en el diccionario, comparara posteriormente la contrasenia para ver si son correctos
	if(user in usuarios) and (usuarios[user][1] == passw): #Si el usuario y contrasenia son correctos, dejara entrar al usuario
		print("Bienvenido",usuarios.get(registro)[2])
		print("Apellido: ",usuarios.get(registro)[3])
		print("Edad: ",usuarios.get(registro)[4])
		print("Tarjeta de credito:",usuarios.get(registro)[5])
		print("Cuenta de paypal:",usuario(registro)[6])
	#elif (user in usuarios) and (usuarios[user][1] = passw):: #Si el usuario no coincide en el diccionario, imprimira lo siguiente:
		#print( "contraseña incorrecto")
	else:
		print("Usuario no registrado o contraseña incorrecta")
	

Menu()
x= int(input("¿que deseas hacer?"))
if (x == 1):
	print("Registro")
	Registro()
elif (x == 2):
	print("Login")
	Login()
else: 
	print("Adios")

