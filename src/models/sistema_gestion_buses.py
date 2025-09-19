"""
Módulo que contiene la implementación del Sistema de Gestión de Buses.
"""
from typing import Optional, List
from src.models.bus import Bus

class SistemaGestionBuses:
    """
    Clase que gestiona múltiples buses en el sistema.
    """
    
    def __init__(self):
        """Inicializa el sistema de gestión de buses."""
        self.buses = []
        self._contador_buses = 0
    
    def agregar_bus(self, capacidad: int) -> str:
        """
        Agrega un nuevo bus al sistema.
        
        Args:
            capacidad: Número de asientos del bus
            
        Returns:
            str: Número asignado al bus
        """
        self._contador_buses += 1
        numero_bus = str(self._contador_buses)
        nuevo_bus = Bus(numero_bus, capacidad)
        self.buses.append(nuevo_bus)
        return numero_bus
    
    def seleccionar_bus(self, numero: str) -> Optional[Bus]:
        """
        Selecciona un bus por su número.
        
        Args:
            numero: Número del bus a seleccionar
            
        Returns:
            Optional[Bus]: Bus seleccionado o None si no existe
        """
        for bus in self.buses:
            if bus.numero == numero:
                return bus
        return None
    
    def mostrar_buses(self) -> str:
        """
        Muestra el estado de todos los buses.
        
        Returns:
            str: Información de todos los buses
        """
        if not self.buses:
            return "No hay buses registrados en el sistema."
            
        resultado = "=== ESTADO DE LOS BUSES ===\n"
        for bus in self.buses:
            resultado += f"\n{bus.obtener_estado()}"
            resultado += "-------------------------"
        return resultado