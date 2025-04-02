from rich.console import Console
from rich.table import Table


console = Console()
clientes = []
class Clientes:

    def __init__(self, nombre, telefono, correo_electronico, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.direccion = direccion

    def menu_clientes():
        while True:
            print("1. Crear nuevo cliente")
            print("2. Mostrar clientes")
            print("3. Volver al menu principal")
            print("4. Cerrar programa")

            opcion_menu_clientes = input("Seleccione una opcion: ")

            if opcion_menu_clientes == "1":
                Clientes.crear_cliente()
            elif opcion_menu_clientes == "2":
                Clientes.mostrar_clientes()
            elif opcion_menu_clientes == "3":
                return
            elif opcion_menu_clientes == "4":
                break

            
            

        
    def crear_cliente():
        cliente = Clientes("Pedro", "3209998877", "pedro@gmail.com", "Calle 36 #3420")
        clientes.append(cliente)
        print("Cliente creado con exito")

            
    def mostrar_clientes():
         if not clientes:
                print("No hay clientes registrados")
                return
         table = Table(title="Información de los clientes")
         table.add_column("Nombre", style="bold")
         table.add_column("Telefono")
         table.add_column("Correo")
         table.add_column("Direccion")
        
         for cliente in clientes:
            table.add_row(cliente.nombre, cliente.telefono, cliente.correo_electronico, cliente.direccion)

         console.log(table)






