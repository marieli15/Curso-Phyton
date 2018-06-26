# Ejercico hecho en clase
from funciones import Suma,Resta,multiplicacion

print("[1] Suma")
print("[2] Resta")
print("[3] Multiplicacion")

resp = input("¿Que operacion desea hacer?: ")

num1 = int(input("Escribe el primer numero :"))
num2 = int(input("Escribe el segundo numero :"))

if resp == "1":
	print(Suma(num1,num2))
elif resp == "2":
	print(Resta(num1,num2))
else:
	print(multiplicacion(num1,num2))

