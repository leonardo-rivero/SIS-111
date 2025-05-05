#mostras la relacion den umeros
num1=int(input("introduzca el primer numero"))
num2=int(input("introduzca el segundo numero"))
num3=int(input("introduzca el tercero numero"))
num4=int(input("introduzca el cuarto numero"))
num5=int(input("introduzca el ultimo numero"))
if num1<num2 and num2<num3 and num3<num4 and num4<num5:
    print("ESTA DE FORMA ASCENDENTE")
elif num1>num2 and num2>num3 and num3>num4 and num4>num5:
    print("ESTA DE FORMA DESCENDENTE")
else:
    print("ES ALEATORIO")


#BUSQUEDA DE NUMEROS
listadenum=int(input("ingrese lista de numeros "))
numbusqueda=int(input("numero a buscar"))
while listadenum>0:
    num=listadenum%10
    listadenum=listadenum//10
    if num==numbusqueda:
        print("numero encontrado")


#contar par e inpar 
numcont=int(input("ingrese numero"))
par=0
inpar=0
while numcont>0:
    dig=numcont%10
    numcont=numcont//10
    if dig%2==0:
        par=par+1
    else:
        inpar=inpar+1
print("pares encontrados")
print(par)
print("impares encontrados")
print(inpar)

#rendimiento
resultado1=int(input("ingrese nota1 del equipo a "))
resultado2=int(input("ingrese nota2 del equipo a "))
resultado3=int(input("ingrese nota3 del equipo a "))
resultado4=int(input("ingrese nota4 del equipo a "))
resultado5=int(input("ingrese nota1 del equipo b "))
resultado6=int(input("ingrese nota2 del equipo b "))
resultado7=int(input("ingrese nota3 del equipo b "))
resultado8=int(input("ingrese nota4 del equipo b "))
promedioA=(resultado1+resultado2+resultado3+resultado4)/4
promedioB=(resultado5+resultado6+resultado7+resultado8)/4
if promedioA<promedioB:
    print("EL EQUIPO B TIENE MEJOR RENDIMIENTO")
elif promedioA>promedioB:
    print("el equipo a tiene mejor reendimiento")
else:
    print("son iguales")

#producto maximo
print("ingresa 4 numeros")
num6=int(input())
num7=int(input())
num8=int(input())
num9=int(input())
producto1=num6*num7
producto2=num6*num8
producto3=num6*num9
producto4=num7*num8
producto5=num7*num9
producto6=num8*num9
if  producto1>producto2 and producto1>producto3 and producto1>producto4 and producto1>producto5 and producto1>producto6:
    print("el producto mas alto es")
    print(producto1)
elif  producto2>producto1 and producto2>producto3 and producto2>producto4 and producto2>producto5 and producto2>producto6:
    print("el producto mas alto es")
    print(producto2)
elif producto3>producto2 and producto1<producto3 and producto3>producto4 and producto3>producto5 and producto3>producto6:
    print("el producto mas alto es")
    print(producto3)
elif producto4>producto2 and producto4>producto3 and producto1<producto4 and producto4>producto5 and producto4>producto6:
    print("el producto mas alto es")
    print(producto4)
elif producto5>producto2 and producto5>producto3 and producto5>producto4 and producto1<producto5 and producto5>producto6:
    print("el producto mas alto es")
    print(producto5)
else:
    print("el producto mas alto es")
    print(producto6)


#meta de ahorro
meta=int(input("ingresa la meta a alcanzar"))
ingreso=int(input("ingrese el dinero del primer dia"))
dias=0
while ingreso>=meta:
    ingeso=ingreso+2
    dias=dias+1
print("la meta se alcanzo en")
print(dias)
print("dias")

#palindromos 

numero=str(input("ingrese el numero"))
reverso=numero[::-1]
if numero==reverso:
    print("es palindromo")
else:
    print("no es palindromo")

#combinaciones de numeros
nume1=str(input("ingrese numero 1"))
nume2=str(input("ingrese numero 2"))
nume3=str(input("ingrese numero 3"))
nume4=str(input("ingrese numero 4"))
print('combinaciones')
print(nume1+nume2)
print(nume1+nume3)
print(nume1+nume4)
print(nume2+nume3)
print(nume3+nume4)
print(nume2+nume4)

#verificador de primos 

primo=int(input("ingrese un numero"))
div=1
while primo/div==1:
    if primo==div:
        print("el numero es primo")
    else:
        print("el numerono es primo")
    div=div+1

#suma de pares 
def suma_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma += numero
    return suma

# Ejemplo de uso
numeros=[1,2,3,4,5,6]
resultadosuma=suma_pares(numeros)
print(f'la suma de los pares es{resultadosuma}')
