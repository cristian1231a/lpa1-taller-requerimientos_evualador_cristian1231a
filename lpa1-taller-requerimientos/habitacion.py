

class Habitacion:
    def __init__(self, numero, tipo, precio, estado):
        self.numero = numero
        self.tipo = tipo  # Ejemplo: Simple, Doble, Suite
        self.precio = precio
        self.estado = "Disponible" if estado == 0 else "Ocupada"
        self.fechas_reserva = []


    def cambiar_estado(self, nuevo_estado):
        while nuevo_estado not in [0, 1]:
            print("Estado inválido. Use 0 para 'Disponible' o 1 para 'Ocupada'.")
            nuevo_estado = int(input("Ingrese el nuevo estado (0 para Disponible, 1 para Ocupada): "))
        self.estado = "Disponible" if nuevo_estado == 0 else "Ocupada"

    def agregar_reserva(self, fecha_inicio, fecha_fin):
         self.fechas_reserva.append((fecha_inicio, fecha_fin))

    def mostrar_info(self):
        info = f"Número: {self.numero}\nTipo: {self.tipo}\nPrecio: {self.precio}\nEstado: {self.estado}\n"
        if self.fechas_reserva:
            info += "Reservas:\n" + "\n".join([f"Desde {inicio} hasta {fin}" for inicio, fin in self.fechas_reserva])
        return info

    def agregar_habitacion(hotel, hoteles):
        while True:
            if not hoteles:
                print("No hay hoteles registrados para agregar habitaciones.")
                break
            
            print("\nHoteles disponibles:")
            for i, hotel in enumerate(hoteles):
                print(f"{i + 1}. {hotel.nombre}")
            
            opcion = input("¿Desea agregar una habitación? (s/n): ")
            if opcion.lower() != 's':
                print("\nLista de hoteles registrados:")
                for hotel in hoteles:
                    hotel.mostrar_info()
                break
            
            seleccion = int(input("Seleccione el número del hotel donde desea agregar una habitación: "))
            if seleccion < 1 or seleccion > len(hoteles):
                print("Selección inválida.")
                continue
            
            hotel_seleccionado = hoteles[seleccion - 1]
            
            numero = int(input("Ingrese el número de la habitación: "))
            tipo = input("Ingrese el tipo de habitación (Simple, Doble, Suite): ")
            precio = float(input("Ingrese el precio de la habitación: "))
            estado_hab = int(input("Ingrese el estado de la habitación (0 para Disponible, 1 para Ocupada): "))
            while estado_hab not in [0, 1]:
                print("Estado inválido. Use 0 para 'Disponible' o 1 para 'Ocupada'.")
            habitacion = Habitacion(numero, tipo, precio, estado_hab)
            hotel_seleccionado.agregar_habitacion(habitacion)

            print(f"\nHabitación agregada al hotel {hotel_seleccionado.nombre}")
            hotel_seleccionado.mostrar_info()

    def ver_habitaciones(hoteles): # Funcion para ver las habitaciones disponibles
        if not hoteles:
            print("No hay hoteles registrados.")
            return
        
        print("\nHoteles disponibles:")
        for i, hotel in enumerate(hoteles):
            print(f"{i + 1}. {hotel.nombre}")
        
        seleccion = int(input("Seleccione el número del hotel para ver sus habitaciones: "))
        if seleccion < 1 or seleccion > len(hoteles):
            print("Selección inválida.")
            return
        
        hotel_seleccionado = hoteles[seleccion - 1]
        if not hotel_seleccionado.habitaciones:
            print("No hay habitaciones registradas en este hotel.")
            return
        
        for habitacion in hotel_seleccionado.habitaciones:
            print(habitacion.mostrar_info())
            cambio = input("¿Desea cambiar el estado de esta habitación? (s/n): ")
            if cambio.lower() == 's':
                nuevo_estado = int(input("Ingrese el nuevo estado (0 para Disponible, 1 para Ocupada): "))
                habitacion.cambiar_estado(nuevo_estado)
            reserva = input("¿Desea agregar una reserva? (s/n): ")
            if reserva.lower() == 's':
                fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
                habitacion.agregar_reserva(fecha_inicio, fecha_fin)