from myfunctions import operAritmetic
from myfunctions import calcIva
from myfunctions import fibonacciSeries
from myfunctions import factorial

print("Hola mundo dese Python")
"""
Este es un comentario de varias lineas 
"""
# Este es un comentario de una línea

# Definición de variables
firstName = "Pedro"
lasttName = "Gomez"
print(type(firstName))
salaryEmployee = 5000000
gender = True
# lista
numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
]
# tupla
todd = (1, 3, 5, 7, 9)
# set
tpair = {
    10,
    20,
    30,
    40,
}
# diccionario
person = {
    "cc": "1214",
    "name": "Jhon Doe",
    "phone": "3127852596",
    "gender": False,
    "Salary": 3200000,
}
# arreglo de objetos
persons = [
    {"id": 3, "firstName": "Jane Doe", "addres": "Diagonal 59 # 40-70"},
    {"id": 4, "firstName": "Julian Pedro", "addres": "Calle 40 # 88-10"},
    {"id": 5, "firstName": "Simone Lucas", "addres": "Carrera 89 # 100-280"},
]

# Condicional (tradicional)
"""
if not gender:
    print("El empleado es hombre")
else:
    print("El empleado es mujer")
"""

# Operador ternario u operador condicional
print("Es mujer" if gender else "Es hombre")
comission = (
    salaryEmployee * 10 / 100
    if gender and salaryEmployee > 4000000
    else salaryEmployee * 2 / 100
)
print(f"comission: {comission}")
print("comission", comission)
category = "B"
valuePay = 0
if category == "A":
    valuePay = 5000
elif category == "B":
    valuePay = 10000
elif category == "C":
    valuePay = 20000
elif category == "D":
    valuePay = 30000
else:
    valuePay = 1000

print(f"Valor a pagar: {valuePay}")


# Ciclo para (for)
initial = 1
limit = 6
"""
for i in range(initial, limit):
    
    if i < limit -1:
        print(i,end=",")#El end"," sirve para que no aparezca una linea larga de numeros sino que los separa por comas
    else:
        print(i)
"""

# Con operador ternario
"""
for i in range(initial, limit):
    print(i, end="," if i < limit - 1 else "")
"""

# Imprimir un ciclo con los numeros pares del 2 al 10
for i in range(1, 10):
    if i % 2 == 0:
        print(i, end=",")

# Ciclos para recorrer objetos iterables
for nro in numbers:
    print(nro)
print("_______")
for i in range(0, len(numbers)):
    print(numbers[i])

# Cantidad de numeros pares e impares

countEven = 0
countOdd = 0
for num in numbers:
    if num % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print(f"Cantidad de numeros pares: {countEven} e impares: {countOdd}")
print("Recorrer una tupla")
for n in todd:
    print(n)
print("Recorrer una set")
for num in tpair:
    print(num)

# Ciclo para recorrer un diccionario person

for key, value in person.items():
    print(f"{key}: {value}")
print("Mostrar datos del diccionario person de otra forma")
for item in person:
    print(f"{item}: {person[item]}")
print(person["cc"])
print("Mostrando los datos de la lista de diccionarios")
for person in persons:
    print(
        f"ID: {person['id']}, Nombre: {person['firstName']}, Direccion: {person['addres']}"
    )
    print("Buscando el id del diccionario de la lista persons")

idSearch = int (input("Ingrse el id de la persona: "))
found = False
for per in persons:
    if per["id"] == idSearch:
        #print(f"ID: {per['id']}, Nombre: {per['firstName']}, Direccion: {per['addres']}")
        personFind = per
        found = True #Variable bandera
        break
if found:
    print(personFind["firstName"])
else:
    print("No se encontro el id de la persona")
    
# Funciones

def sum(a,b):
    return a + b

def message(text):
    print(text)
    
# Llamando a la función
message ("Hola mundo desde python con metodos")
message ("Bienvenido al sistema")
a = "Buendos dias"
message (a)
print (sum(5,9))
num1 = int(input("Ingrese valor 1: "))
num2 = int(input("Ingrese valor 2: "))
resultado = sum(num1,num2)
if sum(num1,num2) > 20:
    message("El resultado es mayor a 20")
else:
    sum(num1,num2) < 20
    message("El resultado es menor a 20")
    
print(operAritmetic(34,0,"/"))
valIva = calcIva(100000)
print(f"El valor del iva de 100000 es {valIva}")
print(factorial(300))

numIndice = int(input("ingrese valor 1:  "))
numCantidadSubRadical = int(input("ingrese valor 2:  "))
resultado = operAritmetic(numIndice, numCantidadSubRadical, 'sqrt')
print(f"La raíz es: {resultado}")