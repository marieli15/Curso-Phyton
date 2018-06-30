#Menu principal
usuarios = {}
listaregistro = []

def Menu():
	
	print("1) Registrarse")
	print("2) Ingresar")
	print("3) Salir")



def registro():

	username = input("Nombre de ususario: ")
	password = input("Contraseña: ")
	listaregistro.append(username)
	listaregistro.append(password)
	
	nom=input("Ingrese su nombre: ")
	listaregistro.append(nom)
	
	ape=input("Ingrese su apellido: ")
	listaregistro.append(ape)
	
	edad=input("Ingrese su edad: ")
	listaregistro.append(edad)
	
	numtarj=input("ingrese su numero de trajeta de credito: ")
	listaregistro.append(numtarj)
	
	paypal=input("Ingresa un correo para tu cuenta de PayPal: ")
	
	listaregistro.append(paypal)
	
	paypalcont=input("Ingrese la contraseña de la cuenta de paypal: ")
	listaregistro.append(paypalcont)
	
	usuarios[username] = listaregistro

	respuesta = input("¿Quieres agregar otro usuario? s/n " )
	if (respuesta == 'n'):
		print("Sus datos se han guardado exitosamente")
		Menu()
		return x
	elif (respuesta == "s"):
		registro()
	else:
		print("opcion invalida")


#Para ingresar datos de usuario
def Login(usuarios):     
	user = input("Usuario: ")
	passw = input("Contrasenia: ")
	    
	    #Si el usuario esta en el diccionario, comparara posteriormente la contrasenia para ver si son correctos
	if(user in usuarios) and (usuarios[user][1] == passw): #Si el usuario y contrasenia son correctos, dejara entrar al usuario
		print("Bienvenido", usuarios.get(user)[2])
		print("Apellido: ", usuarios.get(user)[3])
		print("Edad: ", usuarios.get(user)[4])
		print("Tarjeta de credito:", usuarios.get(user)[5])
		print("Cuenta de paypal:", usuarios.get(user)[6])
		print("Contraseña de paypal:", usuarios.get(user)[7])
	else:
		print("Usuario no registrado o contraseña incorrecta")
	Menu()
	return x

Menu()
while True:
	x= int(input("¿que deseas hacer?: "))
	if (x == 3):
		print("Adios")
		break
	elif (x == 1):
		print("Registro")
		registro()
	else: 
		print("Login")
		Login(usuarios)
	
	
