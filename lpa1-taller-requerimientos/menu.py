from hotel import Hotel
from habitacion import Habitacion
from rich.console import Console
from rich.table import Table
from busqueda import BusquedaYFiltrado
from clientes import Clientes

console = Console()
hoteles = []  # Lista global de hoteles

class Menu_principal:

    #EN LA CONSOLA SE MOSTRARA ESTE MENU CON LA SIGUIENTES OPCIONES DONDE CADA OPCION NOS PEMITIRA, EJECUTAR UNA DIFERENTE FUNCION
    def mostrar_menu():
        while True:
            print("\nMenú Principal:")
            print("1. Registrar un nuevo hotel")
            print("2. Ver hoteles registrados")
            print("3. Agregar una habitación a un hotel")
            print("4. Ver habitaciones de un hotel")
            print("5. Busqueda y filtrado")
            print("6. Clientes")
            print("9. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            #FUNCIONES DEL MENU
            if opcion == "1":
                Hotel.registrar_hotel(hoteles)
            elif opcion == "2":
                Hotel.ver_hoteles(hoteles)
            elif opcion == "3":
                Habitacion.agregar_habitacion(hoteles)
            elif opcion == "4":
                Habitacion.ver_habitaciones(hoteles)
            elif opcion == "5":
                BusquedaYFiltrado.busqueda_y_filtrado(hoteles)
            elif opcion == "6":
                Clientes.menu_clientes()

                
            elif opcion == "9":
                break
            else:
                print("Opción inválida. Intente de nuevo.")


