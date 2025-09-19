"""
Módulo que contiene la implementación de la interfaz de usuario simplificada.
"""
from src.models.sistema_gestion_buses import SistemaGestionBuses

class InterfazUsuario:
    """
    Clase que maneja la interfaz de usuario del sistema.
    """
    
    def __init__(self):
        """Inicializa la interfaz de usuario."""
        self.sistema = SistemaGestionBuses()
        self.bus_actual = None
    
    def mostrar_menu(self):
        """Muestra el menú principal."""
        print("\n=== SISTEMA DE GESTIÓN DE BUSES ===")
        print("1. Crear nuevo bus")
        print("2. Seleccionar bus")
        print("3. Vender billete")
        print("4. Devolver billete")
        print("5. Ver estado de buses")
        print("6. Ver asientos disponibles del bus actual")
        print("0. Salir")
        print("==================================")
    
    def procesar_opcion(self):
        """Procesa la opción seleccionada por el usuario."""
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                capacidad = int(input("Ingrese la capacidad del bus: "))
                if capacidad <= 0 or capacidad >= 100:
                    print("Error: La capacidad debe ser un número positivo y menor a 100")
                    return True
                numero = self.sistema.agregar_bus(capacidad)
                print(f"Bus creado con éxito. Número: {numero}")
            except ValueError:
                print("Error: La capacidad debe ser un número válido")
                
        elif opcion == "2":
            if not self.sistema.buses:
                print("No hay buses disponibles. Cree uno primero.")
                return True
                
            print("Buses disponibles:")
            for bus in self.sistema.buses:
                print(f"- Bus {bus.numero} (Capacidad: {bus.capacidad})")
            
            numero = input("Ingrese el número del bus: ")
            bus = self.sistema.seleccionar_bus(numero)
            if bus:
                self.bus_actual = bus
                print(f"✅ Bus {numero} seleccionado correctamente.")
                print(f"🚌 Ahora trabajando con Bus #{numero}")
                print(bus.obtener_estado())
            else:
                print("❌ Bus no encontrado")
                
        elif opcion == "3":
            if not self.bus_actual:
                print("⚠️  Primero debe seleccionar un bus")
                return True

            print(f"🚌 Vendiendo billetes para Bus #{self.bus_actual.numero}")
            nombre = input("Nombre del pasajero: ").strip()
            apellido = input("Apellido del pasajero: ").strip()
            
            if not nombre or not apellido:
                print("Error: El nombre y apellido son obligatorios")
                return True
            
            try:
                cantidad = int(input("Cantidad de billetes: "))
                if cantidad <= 0:
                    print("Error: La cantidad debe ser un número positivo")
                    return True
            except ValueError:
                print("Error: La cantidad debe ser un número válido")
                return True
        
            if self.bus_actual.vender_billete(nombre, apellido, cantidad):
                print("Billete(s) vendido(s) con éxito")
                print(self.bus_actual.obtener_estado())
            else:
                print("No hay asientos suficientes disponibles")

        elif opcion == "4":
            if not self.bus_actual:
                print("⚠️  Primero debe seleccionar un bus")
                return True
                
            if not self.bus_actual.asientos:
                print(f"ℹ️  Bus #{self.bus_actual.numero} no tiene billetes vendidos para devolver")
                return True
                
            print(f"🚌 Gestionando devoluciones para Bus #{self.bus_actual.numero}")
            print("Asientos ocupados:")
            for numero in self.bus_actual.obtener_asientos_ocupados():
                venta = self.bus_actual.asientos[numero]
                print(f"Asiento {numero}: {venta.pasajero['nombre']} {venta.pasajero['apellido']}")
                
            try:
                asiento = int(input("Número de asiento a devolver: "))
                if self.bus_actual.devolver_billete(asiento):
                    print("Billete devuelto con éxito")
                    print(self.bus_actual.obtener_estado())
                else:
                    print("Asiento no encontrado o ya está libre")
            except ValueError:
                print("Error: El número de asiento debe ser válido")
                
        elif opcion == "5":
            print(self.sistema.mostrar_buses())
            
        elif opcion == "6":
            if not self.bus_actual:
                print("⚠️  Primero debe seleccionar un bus")
                return True
            
            disponibles = self.bus_actual.obtener_asientos_disponibles()
            ocupados = self.bus_actual.obtener_asientos_ocupados()
            
            print(f"\n🚌 Estado detallado del Bus #{self.bus_actual.numero}:")
            print(f"📊 Capacidad total: {self.bus_actual.capacidad}")
            print(f"✅ Asientos disponibles: {disponibles}")
            print(f"🔴 Asientos ocupados: {ocupados}")
            
        elif opcion == "0":
            return False
        else:
            print("Opción no válida. Por favor, seleccione una opción del 0 al 6.")
            
        return True
    
    def iniciar(self):
        """Inicia la interfaz de usuario."""
        print("¡Bienvenido al Sistema de Gestión de Buses!")
        
        while True:
            self.mostrar_menu()
            if not self.procesar_opcion():
                print("¡Gracias por usar el sistema!")
                break