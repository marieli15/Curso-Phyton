#Parte dos del registro
#lo tengo guardado en el dicc(usuarios), pero a su vez estan dentro de la listaregustro 
from ejer3 import nom, ape, edad, numtarj, paypal, paypalcont
registro= open("registro.txt","w")
nombre = nom()
apellido = ape()
ed = edad()
numtarjeta = numtarj()
paypal = paypal()
paycont = paypalcont
registro.write("Bienvenido: "+ nombre + " " + apellido)
registro.write("Edad: "+ edad)
registro.write("Numero de tarjeta: " + numtarjeta)
aregistro.write("Cuenta de paypal y contraseña: "  + paypal + " " + paycont)
registro.close()
