from eje3par2 import imprimir
#Menu principal
usuarios = {}
listaregistro = []
username = ""

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
	conT=usuarios.get(user)[1]
	nom=usuarios.get(user)[2]
	apl=usuarios.get(user)[3]
	ed=usuarios.get(user)[4]
	tg=usuarios.get(user)[5]
	cuen=usuarios.get(user)[6]
	cons=usuarios.get(user)[7]
	    
	#Si el usuario esta en el diccionario, comparara posteriormente la contrasenia para ver si son correctos
	if(user in usuarios) and (conT == passw): #Si el usuario y contrasenia son correctos, dejara entrar al usuario
		

		print("Bienvenido", nom)
		print("Apellido: ", apl)
		print("Edad: ", ed)
		print("Tarjeta de credito:",tg )
		print("Cuenta de paypal:", cuen)
		print("Contraseña de paypal:", cons)
		imprimir(nom,apl,ed,tg,cuen,cons)
	else:
		print("Usuario no registrado o contraseña incorrecta")
	Menu()
	return x
if __name__ == "__main__":

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
		
	
