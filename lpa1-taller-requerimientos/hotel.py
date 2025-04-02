from rich.console import Console
from rich.table import Table

from habitacion import Habitacion

console = Console() # Esta instancia sirve para que el texto con formato pueda aparecer en la consola
class Hotel:
    def __init__(self, nombre, direccion, telefono, correo, ubicacion, estado, calificacion, servicios):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.ubicacion = ubicacion
        self.estado = estado  # Activo/Inactivo
        self.calificacion = calificacion  # calificacion en numero 1 , 2  , 3 , 4 ,5
        self.servicios = servicios  # Lista de servicios
        self.ofertas = []  # Lista de ofertas especiales
        self.habitaciones = []  # Lista de habitaciones

    def agregar_oferta(self, descripcion, descuento):
        oferta = {"descripcion": descripcion, "descuento": descuento}
        self.ofertas.append(oferta)

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["Activo", "Inactivo"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado inválido. Use 'Activo' o 'Inactivo'.")

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_info(self):
        table = Table(title="Información del Hotel")
        table.add_column("Campo", style="bold")
        table.add_column("Datos")
        
        table.add_row("Nombre", self.nombre)
        table.add_row("Dirección", self.direccion)
        table.add_row("Teléfono", self.telefono)
        table.add_row("Correo", self.correo)
        table.add_row("Ubicación", self.ubicacion)
        table.add_row("Estado", self.estado)
        table.add_row("Calificacion", self.calificacion +f" Estrellas")
        table.add_row("Servicios", ', '.join(self.servicios))
        table.add_row("Ofertas", ', '.join([o['descripcion'] for o in self.ofertas]))
        table.add_row("Número de Habitaciones", str(len(self.habitaciones)))
        
        console.print(table)
        

    def ver_hoteles(hoteles):
        if not hoteles: # si no existe ningun hotel registrado aparecera este mensaje
            print("No hay hoteles registrados.")
            return
        for hotel in hoteles: # en caso de existir algun hotel registrar ejecutara mostrar_info()
            hotel.mostrar_info()

    
     
    def registrar_hotel(hoteles): # REGISTRAREMOS PRIMERO EL HOTEL
        
        while True:
            
            agregar_hotel = input("¿Desea registrar un nuevo hotel? (s/n): ")
            if agregar_hotel.lower() != 's':
                break
            tipo_de_creacion = input("Crear los datos en automatico con datos ya creados o manual? 0 = AUTOMATICO , 1 = MANUAL: ")
            if tipo_de_creacion == 1:
                nombre = input("Ingrese el nombre del hotel: ")
                direccion = input("Ingrese la dirección del hotel: ")
                telefono = input("Ingrese el teléfono del hotel: ")
                correo = input("Ingrese el correo del hotel: ")
                ubicacion = input("Ingrese la ubicación del hotel: ")
                estado = input("Ingrese el estado del hotel (Activo/Inactivo): ")
                servicios = input("Ingrese los servicios del hotel separados por coma: ").split(",")
                hotel = Hotel(nombre, direccion, telefono, correo, ubicacion, estado, servicios, [])
                hoteles.append(hotel)
            else:
                hotel = Hotel("Hotel Sherato", "Calle 10 0 02", "3251234561", "shera@gmail.com", "Cali", "Activo", "5" , ["Restaurante, Pisicina, parqueadero, Bar"])
                hotel2 = Hotel("Hotel Hilto", "Carrrra 359", "3105489866", "hilto@gmail.com", "Bogota", "Activo", "3" , ["Restaurante, , parqueadero, "])
                hotel3 = Hotel("Hotel Spik", "Calle 8790 ", "3175896012", "spik@gmail.com", "Medellin", "Activo", "4" , [", Pisicina, , Bar"])
                hotel4 = Hotel("Hotel Intecontin", "Diagonal 5154", "3201445669", "interconm@gmail.com", "Cali", "Activo", "2" , ["Restaurante, Pisicina, , Bar"])
                hoteles.append(hotel)
                hoteles.append(hotel2)
                hoteles.append(hotel3)
                hoteles.append(hotel4)

        print("*============== Hotel registrado con exito ====================*")
        Habitacion.agregar_habitacion(hotel, hoteles)
        



