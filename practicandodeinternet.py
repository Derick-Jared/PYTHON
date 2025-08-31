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
#16) Crea una funcion que calcule la temperatura media de un dia a partir de la temperatura
# maxima y minima.
#Crear un programa principal, que utilizando la funcion anterior, vaya pidiendo
#la temperatura maxima y minima de cada dia y vaya mostrando la media.
#El programa pedira el numero de dias que se van a introducir.
# def temperaturaMedia(min , max):
#     return (min + max)/2

# cantDias = int(input("Ingrese la cantidad de dias: "))
# for i in range (cantDias):
#     tempmin = float(input("Ingrese la temperatura minima del dia ("+str(i+1)+") :"))
#     tempmax = float(input("Ingrese la temperatura maxima del dia ("+str(i+1)+") :"))
#     print("La temperatura media del dia (",(i+1),") es: ",temperaturaMedia(tempmin,tempmax))
#17)Crea una funcion "ConvertirEspaciado",  que reciba como parametro un texto y devuelve
#una cadeena con un espacio adicional tras cada letra.
#Ejemplo: "hola, tu" devolvera "h o l a ,   t u ". Crea un programa principal donde se use dicha funcion
# def ConvertirEspaciado(text):
#     new_text = ""
#     for i in range(text.__len__()):
#         new_text += text[i]+" "
#     return new_text
# text= input("Ingrese un texto: ")
# print("El nuevo texto es: ",ConvertirEspaciado(text))
#18)Crea una funcion "calcularMaxMin" que reciba una lista de numeros y devuelva el valor 
#maximo y minimo. Crea un programa que pida numeros por teclado y muestre el maximo y minimo,
#utilizando la funcion anterior.
# def calcularMaxMin(lista):
#     min=9999999
#     max=-9999999
#     for i in range (lista.__len__()):
#         if lista[i] < min:
#             min = lista[i]
#         if lista[i] > max:
#             max = lista[i]
#     return min,max
# numeros = []
# cant= int (input("Ingrese la cantidad de numeros a introducir:"))
# for i in range(cant):
#     num = int(input("Ingrese el numero ("+str(i+1)+"): "))
#     numeros.append(num)
# print("El minimo y maximo son :",calcularMaxMin(numeros))
#19)Dise;ar una funcion que calcule el area y el perimetro de una circunferencia.
#utiliza dicha funcion en un programa principal que lea el radio de una circunferencia
#y muestre su area y su perimetro.
# import math
# def calcularAreaPerimetro(radio):
#     area=math.pi*radio**2
#     area=round(area,2)
#     perimetro=2*math.pi*radio
#     perimetro=round(perimetro,2)
#     return area,perimetro
# radio = float (input("Ingrese el radio de la circunferencia:"))
# print("El area y perimetro son:",calcularAreaPerimetro(radio),)
#20)Crear una subrutina llamada "Login", que reciba un nombre de usuario y una contrase;a
#y devuelve Verdadero si el nombre de usuario es "usuario1"
#y la contrase;a es "asdasd". Ademas recibe el numero de intentos que se ha intentado
#hacer login y si no se ha podido hacer login incremente el valor.
#Crear un programa principal que pida un nombre de usuario y una contrase;a y se intente hacer
#login, solamente tres oportunidades para intentarlo.
# def Login(user,passw):
#     if user == "usuario1" and passw == "asdasd":
#         return True
#     else:
#         return False
# intentos = 1
# while (intentos<=3):
#     user = input("Ingrese le nombre de usuario: ")
#     passw = input("Ingrese la contrase;a: ")
#     if Login(user,passw):
#         print("Login exitoso")
#         break
#     else:
#         print("Login fallido")
#         print("Intento numero: ",intentos)
#         intentos += 1
#21)Crear una funcion recursiva que calcule el factorial de un numero. Realiza un
#programa principal que donde se lea un entero y se muestre el resultado del facotorial
# def factorial (number):
#     if(number==0):
#         return 1
#     else:
#         return number * factorial(number-1)
# num = int(input("Ingrese el numero para calcular su facotrial: "))
# print("El factorial de ",num," es: ",factorial(num))
#22)Crear una funcion que calcule el MCD de dos numeros por el metodo Euclides.
# el metodo euclides es el siguiente:
# Se divide el numero mayor entre el menor
# si la division es exacta, el divisor es el MCD
# si la division no es exacta, dividimos entre el resto obtenido y se continua
# de esta forma hasta obtener una division exacta, siendo el ultimo divisor el MCD
#Crea un programa principal que que lea dos numeros y muestre el MCD
# def MCD(num1,num2):
#     if(num1>num2):
#         mayor=num1
#         menor=num2
#     if(num2>num1):
#         mayor=num2
#         menor=num1
#     if(num1%num2==0):
#         return num1/num2
#     else:
#         resto=mayor%menor
#         return MCD(menor,resto)
# number1 = int(input("Ingrese el primer numero: "))
# number2 = int(input("Ingrese el segundo numero: "))