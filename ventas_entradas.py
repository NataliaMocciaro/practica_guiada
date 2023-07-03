

#declaración de variables - valores

entradas_populares = 100
entradas_exclusivas = 50
entradas_vip = 20

valor_populares = 1000
valor_exclusivas = 2000
valor_vip = 3000

total_recaudado = 0
total_clientes = 0

def calculos_para_entradas_vip(cant):
#asignado a Omar
    pass

def calculos_para_entradas_exclusivas(cant):
    #asignado a Damian
    global total_recaudado
    total_a_pagar = valor_exclusivas * cant
    total_recaudado += total_a_pagar
    print('El total a pagar es: $', total_a_pagar)

def calculos_para_entradas_populares(cant):
    #asignado a Agustín
    pass

while True:

    #Ingreso y fin del sistema
    print("""Ingrese:
1- Para realizar una venta
2- Para finalizar la venta""")
    venta = int(input())

    if venta == 2:
        print("Recaudación total: ", total_recaudado)
        print("Clientes atendidos: ", total_clientes)
        print("\nSobrantes: ")
        print("Entradas Vip: ", entradas_vip)
        print("Entradas Exclusivas: ", entradas_exclusivas)
        print("Entradas Populares: ", entradas_populares)
        print("\nGracias por utilizar el sistema")
        exit()
    
    elif venta == 1:

        total_clientes = total_clientes + 1
        while True:

            # cada compra
            print(
"""Tipo de entradas:
1- Entradas populares
2- Entradas exclusivas
3- Entradas vip
4- Finalizar Compra""")
            compra = int(input())
        
            if compra == 4:
                break
            elif compra == 3:
                cantidad_solicitada = int(input("Cuantas entradas necesita: "))
                calculos_para_entradas_vip(cantidad_solicitada)
            elif compra == 2:
                cantidad_solicitada = int(input("Cuantas entradas necesita: "))
                calculos_para_entradas_exclusivas(cantidad_solicitada)
            elif compra == 1:
                cantidad_solicitada = int(input("Cuantas entradas necesita: "))
                calculos_para_entradas_populares(cantidad_solicitada)
            else:
                print("Debe esegir una opción correcta")  

    else:
        print("Debe esegir una opción correcta")