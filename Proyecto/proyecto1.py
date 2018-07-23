 -*- coding: UTF-8 -*-
import getpass
Modulos que nos van a permitir enviar correos
import smtlib.getpass, os
from email.mime.multupart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os
import sys

usuarios = {}
usuar = {}
produ = {}

def menu_principal():
    print("Bienvenido a Free Store")
    print("0) Registrarse")
    print("1) Ingresar")
    print("2) Salir")
    s= int(input("¿Que desea hacer?: "))

    if s == 1:
        print("Ingresar")
        print("")
        Login()
    elif s == 0:
        print("Registrarse")
        print("")
        registro()
        print("Usuario registrado")
        menu_principal()
        return s
    elif s == 2:
        sys.exit
    else:
        print("Por favor digite una respuesta correcta")
        menu_principal()
        return s

def registro ():
    print("Usted puede registrarse")
    print("1) Vendedor")
    print("2) Comprador")
    ing = int(input("¿Como desea registrarse?: "))
    if ing == 2:
        Usuar.agregar()
    elif ing == 1:
        Usuario.agregar()
    else:
        print("Respuesta incorrecta")
        return registro()

def Login():
    print("Las opciones para ingresar son: ")
    print("1) Comprador")
    print("2) Vendedor")
    print("Nota: Es muy importante que SU INGRESO sea de acuerdo a como se Registro, de lo contrario no podra acceder.")
    opcion = int(input("Usted desea ingresar como: "))
    if opcion == 1:
        print("Usted ha ingresado como comprador")
        print("")
        user = input("Ingresa el nombre de usuario: ")
        passw = input("Ingrese su contraseña: ")

        if (usuar[user].password == passw):
            print("Bienvenido", usuar[user].username)
            usuario_buyer.menu_buy()
        else:
            print("Contraseña o usuario incorrecto")

    elif opcion == 2:
        print("Usted ha ingresado como vendedor")
        print("")
        user = input("Ingresa el nombre de usuario: ")
        passw = input("Ingrese su contraseña: ")
        if (usuarios[user].password == passw):
            print("Bienvenido", usuarios[user].username)
            usuario_seller.menu_sell()
        else:
            print("Contraseña o usuario incorrecto")
    else:
        print("Por favor, escriba una opcion correcta")
        Usuario.Login()
        return opcion

class Usuar():
    def __init__(self,username,password,nombre,apellido,edad,numtarj,paypal,paypalcont):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.numtarj = numtarj
        self.paypal = paypal
        self.paypalcont = paypalcont

    def agregar():
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")

        nombre = input("Ingrese su nombre: ")
        apellido =input("Ingrese su apellido: ")
        edad=input("Ingrese su edad: ")
        numtarj=input("ingrese su numero de trajeta de credito: ")
        paypal=input("Ingresa un correo para tu cuenta de PayPal: ")
        paypalcont=input("Ingrese la contraseña de la cuenta de paypal: ")
        usuar1 = Usuar(username,password,nombre,apellido,edad,numtarj,paypal,paypalcont)
        compra(username,password,nombre,apellido,edad,numtarj,paypal,paypalcont)
        usuar[usuar1.username] = usuar1
        return usuar1


    def __str__(Usuar):
        compra=str(Usuar.username)+str(Usuar.password)+str(Usuar.nombre)+str(Usuar.edad)+str(Usuar.numtarj)+str(Usuar.paypal)+str(Usuar.paypalcont)
        return compra

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

    def agregar():
        username = input("Nombre de usuario: ")
        password = input("Contraseña: ")
        nombre = input("Ingrese su nombre: ")
        apellido =input("Ingrese su apellido: ")
        edad=input("Ingrese su edad: ")
        numtarj=input("ingrese su numero de trajeta de credito: ")
        paypal=input("Ingresa un correo para tu cuenta de PayPal: ")
        paypalcont=input("Ingrese la contraseña de la cuenta de paypal: ")
        usuario1 = Usuario(username,password,nombre,apellido,edad,numtarj,paypal,paypalcont)
        usuarios[usuario1.username] = usuario1
        usua(username,password,nombre,apellido,edad,numtarj,paypal,paypalcont)
        return usuario1


    def __str__(Usuario):
        usua=str(Usuario.username)+str(Usuario.password)+str(Usuario.nombre)+str(Usuario.edad)+str(Usuario.numtarj)+str(Usuario.paypal)+str(Usuario.paypalcont)
        return usua

#clase para el vendedor
class usuario_seller():
    def menu_sell():
        print("")
        print("Usted se encuentra en su menu principal")
        print("")
        print("1) Agregar articulo")
        print("2) Ver sus articulos en venta")
        print("3) Salir")
        print("4) Regresar al inicio")
        opc = int(input("¿Que opcion desea realizar?: "))

        if opc == 1:
            usuario_seller.agregar()
            while True:
                print("")
                print("[a] Agregar otro articulo")
                print("[v] Volver al menu.")
                print("[s] Salir")
                resp =  input("¿Que desea hacer?: ")

                if resp == "s":
                    print("Adios")
                    break
                elif resp == "v":
                    usuario_seller.menu_sell()
                elif resp == "a":
                    usuario_seller.agregar()
                else:
                    print("Respuesta no valida")
                    return resp

        elif opc == 2:
            usuario_seller.ver_art()
            print("")
            print("[r] Para regresar al submenu de vendedor")
            print("[m] Para regresar al menu inicial")
            resp = input("¿Que desea hacer?: ")

            if resp == "r":
                usuario_seller.menu_sell()
            elif resp == "m":
                menu_principal()
            else:
                print("Respuesta no valida")
                return resp
        elif opc == 3:
            sys.exit
        elif opc == 4:
            menu_principal()
        else:
            print("Por favor, digite una respuesta valida")
            usuario_seller.menu_sell()
            return opc

    def __init__(self,idarticulo,name,precio,descrip,cantidad):
        self.idarticulo = idarticulo
        self.name = name
        self.precio= precio
        self.descrip = descrip
        self.cantidad = cantidad

    def agregar():
        print("Usted se encuentra en el menu de agregar articulos")
        print("")  	#unicamente para espacio en pantalla
        idarticulo = int(input("Escriba con numero el codigo del articulo: "))
        name = input("Escriba el nombre del articulo que desea vender: ")
        precio = input("Escriba el precio del articulo: ")
        descrip = input("Escriba una descripcion del producto, con la finalidad de ayudar a los compradores a conocer su producto: ")
        cantidad = int(input("¿Cuantos articulos va ha poner en venta?: "))
        producto(idarticulo,name,precio,descrip,cantidad)
        print("Articulo agregado.")
        producto1 = usuario_seller(idarticulo,precio,name,descrip,cantidad)
        produ[producto1.idarticulo] = producto1
        return producto1

    def __str__(usuario_seller):
        produ=str(usuario_seller.idarticulo)+str(usuario_seller.name)+str(usuario_seller.precio)+str(usuario_seller.descrip)+str(usuario_seller.cantidad)
        return produ

    def ver_art():

        print("Sus articulos son los siguientes:")
        print("")
        leer()

#para el usuario comprador
class usuario_buyer():

    def menu_buy():
        print("")
        print("Usted se encuentra en el submenu principal ")
        print("1) Ver articulos")
        print("2) Comprar")
        print("3) Salir")
        print("4) Regresar al menu incial")
        rep = int(input("Digite la opcion que desea realizar: "))

        if rep == 1:
            usuario_buyer.ver_artic()
            print("")
            com = input("Desea comprar algun producto: \t")
            print("[s] Si")
            print("[n] No")
            if com == "s":
                usuario_buyer.comp()
            elif com == "n":
                print("")
                usuario_seller.menu_buy()
            else:
                print("Opcion incorrecta")
                return com
        elif rep == 2:
            usuario_buyer.comp()
            print("")
            des = input("¿Desea comprar otro articulo?: 1)Si \t 2)No: ")
            if des == "1":
                usuario_buyer.comp()
            else:
                print("Su ticket se ha impreso correctamente")
                #print("EL mensaje anterior se enviara a su correo, como un comprobante de su compra")
                #def correo()
        elif rep == 4:
            menu_principal()
        elif rep == 3:
            sys.exit
        else:
            print("La opcion no se encuentra dentro del menu, por favor digite una opcion")
            return usuario_buyer.menu_buy()

    def ver_artic():
        print("Free Store")
        print("Productos: ")
        print("")
        leer()

    def comp():
        print("Compra de Productos")
        print("")
        print("Por favor escriba correctamente lo que se le pide: ")

        for articulo in produ:
            print("No. articulo: ", produ.idarticulo)
            print("Nombre del articulo: : ", produ.name)
            print("Precio: ", produ.precio)
            print("")

        arti = int(input("No. del articulo: "))
        articulo = produ[arti].idarticulo
        precio = produ[arti].precio
        nom = produ[arti].name

        if (produ[arti].idarticulo == arti):
            print("No. articulo: ", produ[arti].idarticulo)
            print("Nombre del articulo: : ", produ[arti].name)
            print("Precio: ", produ[arti].precio)
            print("")
            pg = input("¿Esta seguro de la compra?: 1) Si \t 2)No: ")
            print("")

            if pg == "1":
                cuenta = input("Digite su cuenta de paypal: ")
                use = input("Digite el nombre de usuario-comprador: ")
                nombre = usuar[use].username
                ape = usuar[use].apellido

                if (usuar[use].paypal == cuenta):
                    print("")
                    print("Bienvenido", usuarios[use].username)
                    print("Apellido: ",usuarios[use].apellido)
                    print("Cuenta de paypal:", usuarios[use].paypal)
                    mensaje (nom,ape,articulo,precio)
                    correo(nom,ape,articulo,precio)
                    print(" Compra exitosa")
                else:
                    print("Contraseña o cuenta de paypal incorrecta")
                    return usuario_buyer.comp()
            elif pg == "2":
                print("Compra cancelada")
                return usuario_buyer.comp()
                print("Esperamos encuentre un producto de su agrado dentro del catalago")
            else:
                print("opcion incorrecta")
                return usuario_buyer.comp()
        else:
            print("El articulo no se encuentra en el catalogo")
            return usuario_buyer.comp()

#para crear archivo de texto que guarde vendedores
def usua(username,password,nombre,apellido,edad,numtarj,paypal,paypalcont):
    archivo= open("archivo.txt","a")
    archivo.write("Usario: "+str(username)+ "\n")
    archivo.write("Contrasena de usuario: " +str(password)+ "\n")
    archivo.write("Bienvenido: "+ str(nombre) + " " + str(apellido)+"\n")
    archivo.write("Edad: "+ str(edad)+"\n")
    archivo.write("Numero de tarjeta: " + str(numtarj)+"\n")
    archivo.write("Cuenta de paypal: "  + str(paypal)+"\n")
    archivo.write("Contraseña de paypal: " + str(paypalcont)+"\n")
    archivo.close()

#archivo de texto para compradores
def compra(username,password,nombre,apellido,edad,numtarj,paypal,paypalcont):
    comprador = open("comprador.txt","a")
    comprador.write("Usario: "+str(username)+ "\n")
    comprador.write("Contrasena de usuario: " +str(password)+ "\n")
    comprador.write("Bienvenido: "+ str(nombre) + " " + str(apellido)+"\n")
    comprador.write("Edad: "+ str(edad)+"\n")
    comprador.write("Numero de tarjeta: " + str(numtarj)+"\n")
    comprador.write("Cuenta de paypal: "  + str(paypal)+"\n")
    comprador.write("Contraseña de paypal: " + str(paypalcont)+"\n")
    comprador.close()

def producto(idarticulo,nombre,precio,descrip,cantidad):
    articulo = open("articulo.txt","a")
    articulo.write("No. Articulo: "+ str(idarticulo)+"\n")
    articulo.write("Articulo: "+ str(nombre)+"\n")
    articulo.write("Precio: "+str(precio)+"\n")
    articulo.write("Desripcion: " + str(descrip)+"\n")
    articulo.write("Cantidad de Articulos en venta: "  + str(cantidad)+"\n")
    articulo.close()

def leer():
    articulo = open("articulo.txt", "r")
    print(articulo.read())

def mensaje (nom,ape,articulo,precio):
    ticket = open("ticket.txt", "w")
    ticket.write("Free Store"+ "\n")
    ticket.write("Bienvenido: "+ str(nom) + " " + str(ape)+"\n")
    ticket.write("Comprobante y/o ticket de compra" + '\n')
    ticket.write("Tipo de mercancía adquirida: " + str(articulo)+ '\n')
    ticket.write("Precio:"+str(precio)+"\n")
    ticket.close()

def correo(nom,ape,articulo,precio):
    user = ("curso_python@outlook.com")
    contraseña = ("Aprepyt3") #para cuando pida la contraseña de acceso
    destinatario = input("por favor, vuelva a escribir su correo: ")
    asunto = input("Compra online")
    mensaje = input("Mensaje: Articulos comprados")
    archivo = input("Adjuntar archivo: "+"\n")
    archivo.write("Free Store"+ "\n")
    archivo.write("Bienvenido: "+ str(nom) + " " + str(ape)+"\n")
    archivo.write("Comprobante y/o ticket de compra" + '\n')
    archivo.write("Tipo de mercancía adquirida: " + str(articulo)+ '\n')
    archivo.write("Precio:"+str(precio)+"\n")
    #archivo.close()
    #Protocolo y puerto
    gmail = smtplib.SMTP('smtp.gmail.com',587)
    #cERTIFICACION DE SEGURIDAD
    gmail.startls()
    #Ingresar
    gmail.login(user,password)
    gmail.set_debuglevel(1)
    #Ingresamos pero falta llenar la informacion del correo de datos de captura
    header = MIMEtipart()
    header["Subject"]=asunto
    header["From"]=remitente
    header["To"]=destinatario
    #Convertimos a HTML
    mensaje = MIMEText (mensaje, "html")
    header.attach(mensaje)
    #Comprobar que el archivo exista
    #Comprobar que el archi
    if (os.path.isfile(archivo)):
    	adjunto=MIMEBase("application","octet-stream")
    	adjunto.set_payload(open(archivo,"rb").read()) #leemos el contenido del archivo
    	encode_base64(adjunto)
    	adjunto.add_header('Content-Disposition','attachment; filename="%s"'%os.path.basename(archivo))
    	header.attach(adjunto)
    #Enviar email
    gmail.sendmail(remitente, destinatario, header.as_string())
    #Cerrar sesion
    gmail.quit()

menu_principal()
