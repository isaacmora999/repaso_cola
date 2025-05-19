from banco import Banco

def mostrar_menu():
    print("\n---- Menu del Banco -----")
    print("\1. Llegada de cliente")
    print("\2. Atender al cliente")
    print("\3. Mostrar clientes en espera")
    print("\4. Salir")


def main():
        banco = Banco()
        while True:
            mostrar_menu()
            opcion = input("seleccione una opcion: ")

            if opcion == "1":
                nombre = input("ingrese el nombre del cliente: ")
                banco.llega_cliente(nombre)
            elif opcion == "2":
                 banco.atender_cliente()
            elif opcion == "3":
                 banco.obtener_clientes_en_espera()
            elif opcion == "4":
                 print("saliendo del programa")
                 break     



if __name__ == "__main__":
    main()                
   
    