'''
Ejercicio #2. Leer información de 10 frutas {nombre, color, precio} para preparar un salpicón; 
el programa debe permitir mostrar las 10 frutas ingresadas al mismo tiempo+(1)
'''
print("----- PREPARANDO UN SALPICÓN -----")

frutas=[]

for i in range(5):
    fruta={}
    fruta['nombre']=input("Digite el nombre de la fruta: ")
    fruta['color']=input("Digite el color de la fruta: ")
    fruta['precio']=input("Digite el precio de la fruta: ")
    frutas.append(fruta)
    
print(frutas)