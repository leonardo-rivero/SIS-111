

def calcular_descuento_producto():
    precio_original= 100
    descuento=20
    precio_descuento = (precio_original*descuento)/100
    precio_final =precio_original-precio_descuento
    return precio_final

var_precio_f=calcular_descuento_producto()
print(var_precio_f)

def calcular_el_salario_mejorado(precio_original, descuento):
    precio_descuento = (precio_original*descuento)/100
    precio_final =precio_original-precio_descuento
    return precio_final

def calcular_el_salario_mejoradox2(precio_original, descuento):
    return precio_original-(precio_original*descuento)/100
def calcular_el_descuento_mejoradox3(precio_original, descuento):
    return precio_original *(1-descuento/100)

precio_original=int(input("ingrese el precio del producto"))
descuento=int(input("ingrese la cantidad de descuento"))
var_precio_ff=calcular_el_salario_mejorado(precio_original, descuento)
print(var_precio_ff)




#EDAD MINIMA PARA VOTAR }
def edad_minima_para_votar():
    print("la edad minima es de 18 años")

def edad_minima_para_votar_mejorada(edad):
    if edad>18:
        return edad


#mayor entre 2 numeros

def mayor_2_numeros(numA, numB):
    if (numB==numA): return "iguales"

    if numA>numB:
        return numA
    else:
        return numB
    
def mayor_2_numeros_mejorados(numA, numB):
    if(numA==numB): return "iguales"
    return numA if numB<numA   else numB
numA= int(input("ingrese numero a"))
numB= int(input("ingrese el valor B"))
var_num_mayor=mayor_2_numeros(numA, numB)
print(var_num_mayor)







# recoger digitos

def recorrer_digitos(num):
    while(num>0):
        dig=num%10
        var_temporal= "par" if(dig%2==0) else "impar"
        print(var_temporal)
       
        print(dig)
        num=num//10

def suma_de_digitos(num):
    suma=0
    while(num>0):
        dig= num%10
        suma=suma+dig
        num=num//10
    return suma

#salida
recorrer_digitos(6546354210)
var_suma= suma_de_digitos(897174)
print(var_suma)