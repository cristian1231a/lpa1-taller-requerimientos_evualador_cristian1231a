from rich.console import Console
from rich.table import Table
from datetime import datetime

console = Console()

class BusquedaYFiltrado:
    @staticmethod
    def busqueda_y_filtrado(hoteles):
        if not hoteles:
            print("No hay hoteles registrados.")
            return
        
        print("\nOpciones de filtrado:")
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD) o presione Enter para omitir: ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD) o presione Enter para omitir: ")
        calificacion = input("Ingrese la calificación mínima (1-5) o presione Enter para omitir: ")
        precio_max = input("Ingrese el precio máximo o presione Enter para omitir: ")

        while True:
            print("\nIngrese el numero de la ciudad a la que desea filtrar")
            print("1. Cali")
            print("2. Bogota")
            print("3. Medellin")

            opcion = input("Seleccione una opción: ")
        
              #OPCIONES DE LA UBICACIONES
            if opcion == "1":
                ubicacion = "Cali"
                break
            elif opcion == "2":
                ubicacion = "Bogota"
                break
            elif opcion == "3":
                ubicacion = "Medellin"  
                break
            elif opcion == "9":
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        
        hoteles_filtrados = hoteles
        
        if ubicacion:
            hoteles_filtrados = [hotel for hotel in hoteles_filtrados if hotel.ubicacion.lower() == ubicacion.lower()]
        
        if calificacion:
            try:
                calificacion = float(calificacion)
                hoteles_filtrados = [hotel for hotel in hoteles_filtrados if hasattr(hotel, 'calificacion') and hotel.calificacion >= calificacion]
            except ValueError:
                print("Calificación inválida, omitiendo filtro.")
        
        if precio_max:
            try:
                precio_max = float(precio_max)
                hoteles_filtrados = [hotel for hotel in hoteles_filtrados if any(h.precio <= precio_max for h in hotel.habitaciones)]
            except ValueError:
                print("Precio inválido, omitiendo filtro.")
        
        if fecha_inicio and fecha_fin:
            try:
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
                hoteles_filtrados = [hotel for hotel in hoteles_filtrados if any(any(fecha_inicio <= datetime.strptime(res[0], "%Y-%m-%d") <= fecha_fin for res in h.fechas_reserva) for h in hotel.habitaciones)]
            except ValueError:
                print("Formato de fecha inválido, omitiendo filtro.")
        
        if not hoteles_filtrados:
            print("No se encontraron hoteles con los filtros seleccionados.")
            return
        
        for hotel in hoteles_filtrados:
            hotel.mostrar_info()
