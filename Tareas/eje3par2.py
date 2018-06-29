#from ejer3 import usuarios, username
def imprimir(nombre,apellido,edad,numtarjeta,paypal,paycont):
	registro= open("registro.txt","w")
	registro.write("Bienvenido: " + str(nombre) + " " + str(apellido)+"\n")
	registro.write("Edad: "+ str(edad)+"\n")
	registro.write("Numero de tarjeta: " + str(numtarjeta)+"\n")
	registro.write("Cuenta de paypal y contraseña: "  + str(paypal) + " " + str(paycont)+"\t")
	registro.close()



