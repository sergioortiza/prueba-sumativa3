import csv
import time
import os
import random
cls=("cls")


comu=['San Bernardo', 'Calera de tango', 'Buin']

def comunas():
    try:
        print("Seleccione una comuna")
        print("1. San bernardo")
        print("2. Calera de Tango")
        print("3. Buin")
        opc=int(input("Seleccione una opcion: "))
        if opc <=3 and opc >=1:
            if opc ==1:
                return 'San Bernardo'
            if opc ==2:
                return 'Calera de tango'
            if opc ==3:
                return 'Buin'
        else:
            print("Valor fuera de rango ")
    except ValueError:
        print("Ingrese solo numeros")


def registro():
    pedido= random.randint(500,5000)
    print(f"Nro.pedido={pedido}")
    cliente=input("Ingrese su nombre: ")
    direccion=input("Ingrese su direccion: ")
    comuna= comunas()
    try:
        saco5=int(input("Cuantos sacos de 5kg desea comprar?: "))
        saco10=int(input("Cuantos sacos de 10kg desea comprar?: "))
        saco15=int(input("Cuantos sacos de 15kg desea comprar?: "))
    except ValueError:
        print("Ingrese solo numeros")
    return pedido, cliente, direccion, comuna, saco5, saco10, saco15


def guardar(pedido, cliente, direccion, comuna, saco5, saco10, saco15, archivo_csv= 'datoscompra.csv', archivo_txt= 'datoscompra.txt'):
    with open(archivo_csv, 'a', newline='')as archivo:
        campos=['Pedido', 'Cliente', 'Direccion', 'Comuna', 'Saco5kg', 'Saco10kg', 'Saco15kg']
        escritor_csv= csv.DictWriter(archivo, fieldnames=campos)

        if archivo.tell()==0:
            escritor_csv.writeheader()

        escritor_csv.writerow({
            'Pedido': pedido,
            'Cliente': cliente,
            'Direccion': direccion,
            'Comuna': comuna,
            'Saco5kg': saco5,
            'Saco10kg': saco10,
            'Saco15kg': saco15
        })
    with open(archivo_txt,'a') as archivo:
        archivo.write(f"Pedido {pedido} Cliente {cliente} Direccion {direccion} Comuna {comuna} Saco5kg {saco5} Saco10kg {saco10} Saco15kg {saco15}\n")

def mostrarcsv(archivo_csv= 'datoscompra.csv'):
    with open(archivo_csv,'r', newline='')as archivo:
        lector_csv= csv.reader(archivo)
        next(lector_csv)
        for fila in lector_csv:
            print(f"pedido: {fila[0]}, cliente:  {fila[1]}, direccion:  {fila[2]}, comuna  {fila[3]}, saco5kg:  {fila[4]}, saco10kg:  {fila[5]}, saco15kg:  {fila[6]} ")


def mostrarcsv2(archivo_csv= 'datoscompra.csv'):
    with open(archivo_csv,'r', newline='')as archivo:
        lector_csv= csv.reader(archivo)
        busca= comunas()
        busca2= False
        for fila in lector_csv:
            if fila[3]== busca:
                print(f"pedido: {fila[0]}, cliente:  {fila[1]}, direccion:  {fila[2]}, comuna  {fila[3]}, saco5kg:  {fila[4]}, saco10kg:  {fila[5]}, saco15kg:  {fila[6]} ")
                busca2=True
            if not busca2:
                print("Compra no encontrada en la comuna")


def mostrar(archivo_txt= 'datoscompra.txt'):
    try:
        with open(archivo_txt, 'r') as archivo:
            print("Listando pedidos")
            for linea in archivo:
                pedido,cliente,direccion,comuna,saco5,saco10,saco15= linea.strip().split(',')
                print(f"{pedido},  {cliente},  {direccion},  {comuna},  {saco5},  {saco10},  {saco15}\n ")
            
                print("*"* 150)
    except FileNotFoundError:
        print("El archivo txt no existe")


def mostrarcomu(archivo_txt= 'datoscompra.txt'):
    with open(archivo_txt, 'r') as archivo:
        buscar= comunas()
        print(buscar)
        comunaenco= False
        for linea in archivo:
            pedido,cliente,direccion,comuna,saco5,saco10,saco15= linea.strip().split(',')
            if buscar== comuna in archivo_txt:
                print(f"{pedido},  {cliente},  {direccion},  {comuna},  {saco5},  {saco10},  {saco15}\n ")
                comunaenco= True
            if not comunaenco:
                print("Datos no encontrados")





def menu():
    while True:
        print("  Bienvenido a CatPremium  ")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        try:
            opc=int(input("Seleccione una opcion entre 1-4: "))
            if opc>=1 and opc <=4:
                if opc==1:
                    time.sleep(3)
                    os.system(cls)
                    print("Registro de pedidos")
                    cant=int(input("Cuantos pedidos desea realizar"))
                    for i in range(cant):
                        pedido, cliente, direccion, comuna, saco5, saco10, saco15= registro()
                        guardar(pedido, cliente, direccion, comuna, saco5, saco10, saco15)
                        continue    
                if opc==2:
                    print("Espere 3 segundo CARGANDO")
                    time.sleep(3)
                    os.system(cls)
                    print("*"*150)
                    mostrarcsv()
                    print("*"*150)
                if opc==3:
                    time.sleep(3)
                    os.system(cls)
                    print("*"*150)
                    print("Imprimiendo Hoja de ruta")
                    comuna=mostrarcsv2()
                    print("*"*150)
                if opc==4:
                    print("Cerrando programa")
                    break
        except ValueError:
            print()


menu()