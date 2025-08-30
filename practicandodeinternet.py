#https://www.studocu.com/latam/document/universidad-nacional-experimental-de-los-llanos-occidentales-ezequiel-zamora/informatica/400-ejercicios-de-python-desde-nivel-basico-a-avanzado-con-aplicaciones-en-i/82255584
#1) Hacer un programa donde se pida un nombre por teclado y se imprima “Hola ..el_nombre_ingresado”
# name = input("Ingrese tu nombre: ")
# print("Hola tu nombre es :"+name)
#2) Hacer un programa que solicite por teclado dos número y muestre la suma ,
#la resta ,la multiplicación y la división de esos números 
# number1 = float(input("Ingrese el primer numero: "))
# number2 = float(input("Ingrese el segundo numero: "))
# suma = number1 + number2
# resta = number1 - number2
# multiplicacion = number1 * number2
# division = number1 / number2
# print("La suma es: "+str(suma))
# print("La resta es: "+str(resta))
# print("La multiplicacion es: "+str(multiplicacion))
# print("La division es: "+str(division))
#3) Hacer un programa que solicite una edad y determine si es mayor de edad. 
#4) Hacer un programa que solicite una edad e imprima “Es mayor” si es mayor de edad ,
# sino que imprima “Es menor”   
# years = int(input("Ingrese su edad: "))
# if years >= 18:
#     print("Usted es mayor de dedad")
# else:
#     print("Usted es menor de edad")
#5) Hacer un programa que solicite un color por teclado e imprima
# “Puede pasar “ si el color ingresado es verde , “Precaución “ si es amarillo ,
# “No pasar “ si es rojo o “Color inválido” si es cualquier otro.
# color = input("Ingrese un color: ")
# if color.lower() == "verde":
#     print("Puede pasar")
# elif color.lower() == "amarillo":
#     print("Precaucion")
# elif color.lower() == "rojo":
#     print("No pasar")
# else:
#     print("Color invalido")
#6) Hacer un programa que cuente desde el 1 al 100 y los imprima uno a uno. 
# for i in range(1,101):
#     print(i)
#7) Hacer un programa que cuente del 1 al 100 inclusive e imprima sólo los números pares
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)
#8)Hacer un programaque cuente del 1 al 100 inclusive e imprima los numeros que 
#son divisibles por 2 y 5 
# for i in range(1,101):
#     if(i%2==0 and i%5==0):
#         print(i)
#9)Hacer un programa que imprima una tabla de multiplicar del 2 al 9. Cada uno 
#debe mostrar sus valores multiplicados del 1 al  9 inclusive.
# for i in range (2,10):
#     for j in range(1,10):
#         print(i,"*",j,"=",str(i*j))
#10)Hacer un programa que muestre el siguiente dibujo
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
# for i in range (5):
#     for j in range(10):
#         print("*", end=" ")
#     print("")
#11)Hacer un programa que muestre el siguiente dibujo
#   * * * * * * * * * *
#   *                 *
#   *                 *
#   *                 *
#   * * * * * * * * * *
# for i in range (5):
#     for j in range(10):
#         if (i==0) or i==4  or (j==0) or (j==9):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")
#12)Hacer un programa que muestre el siguiente dibujo
#   * 
#   * *
#   * * * 
#   * * * *
#   * * * * *
# for i in range(5):
#     for j in range(5):
#         if(j<=i):
#             print("*",end=" ")
#     print("")
#13)Hacer un programa que muestre el siguiente dibujo
#   * * * * *
#   * * * * *
#   * * * 
#   * * 
#   * 
# for i in range(5):
#     for j in range(5):
#         if (j>=i):
#             print("*",end=" ")
#     print("")
#==============================FUNCIONES=================================
#14)Crea una funcion EscribirCentrado, que reciba como parametro un texto y lo escriba 
#centrado en pantalla suponiendo una anchura de 80 columnas. 
# def EscribirCentrado(texto):
#     anchura = 80
#     print(texto.center(anchura))
# text = input("Ingrese el texto: ")
# EscribirCentrado(text)
#15)Crea un programa que pida dos numeros al usuario y diga si alguno
#de ellos es multiplo del otro. Crea una funcion EsMultiplo que reciba los dos numeros
#y devuelve si el primero es multiplo del segundo.
# def EsMultiplo(num1,num2):
#     if num1 % num2 == 0 or num2 % num1 == 0:
#         return print("Si es multiplo")
#     else:
#         return print("No es multiplo")
# number1 = input("Ingrese el primer numero:")
# number2 = input("Ingrese el segundo numero:")
# EsMultiplo(int(number1),int(number2))