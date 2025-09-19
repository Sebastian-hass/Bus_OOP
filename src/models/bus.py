"""
Módulo que contiene la implementación de la clase Bus.
"""
from typing import Dict, List
from src.models.venta import Venta

class Bus:
    def __init__(self, numero: str, capacidad: int):
        """
        Inicializa un nuevo bus.
        
        Args:
            numero: Número identificador del bus
            capacidad: Número total de asientos
        """
        self.numero = numero
        self.capacidad = capacidad
        # Cambiamos a un diccionario para mapear números de asiento a ventas
        self.asientos = {}  # {numero_asiento: Venta}
        
    def _obtener_proximo_asiento_libre(self) -> int:
        """
        Obtiene el próximo número de asiento disponible.
        
        Returns:
            int: Número del próximo asiento libre
        """
        for i in range(1, self.capacidad + 1):
            if i not in self.asientos:
                return i
        return -1  # No hay asientos disponibles
        
    def vender_billete(self, nombre: str, apellido: str, cantidad: int = 1) -> bool:
        """
        Vende uno o más billetes si hay asientos disponibles.
        
        Args:
            nombre: Nombre del pasajero
            apellido: Apellido del pasajero
            cantidad: Número de billetes a vender
            
        Returns:
            bool: True si la venta fue exitosa, False si no hay asientos
        """
        # Verificar si hay suficientes asientos disponibles
        if len(self.asientos) + cantidad > self.capacidad:
            return False

        # Asignar asientos
        asientos_asignados = []
        for _ in range(cantidad):
            numero_asiento = self._obtener_proximo_asiento_libre()
            if numero_asiento == -1:
                # Deshacer asignaciones parciales si no hay suficientes asientos
                for asiento in asientos_asignados:
                    del self.asientos[asiento]
                return False
            
            venta = Venta(1, nombre, apellido, numero_asiento)
            self.asientos[numero_asiento] = venta
            asientos_asignados.append(numero_asiento)

        return True
        
    def devolver_billete(self, numero_asiento: int) -> bool:
        """
        Devuelve un billete liberando el asiento.
        
        Args:
            numero_asiento: Número del asiento a liberar
            
        Returns:
            bool: True si la devolución fue exitosa
        """
        if numero_asiento in self.asientos:
            del self.asientos[numero_asiento]
            return True
        return False
        
    def obtener_estado(self) -> str:
        """
        Retorna el estado actual del bus.
        
        Returns:
            str: Información sobre el estado del bus
        """
        disponibles = self.capacidad - len(self.asientos)
        
        # Ordenar asientos por número para una visualización más clara
        asientos_ordenados = sorted(self.asientos.items())
        
        detalle = "\n".join(
            f"Asiento {numero}: {venta.pasajero['nombre']} {venta.pasajero['apellido']}"
            for numero, venta in asientos_ordenados
        )
        
        return f"""
Bus número: {self.numero}
Capacidad total: {self.capacidad}
Asientos ocupados: {len(self.asientos)}
Asientos disponibles: {disponibles}
Pasajeros:
{detalle if detalle else 'Ninguno'}
"""

    def obtener_asientos_ocupados(self) -> List[int]:
        """
        Retorna una lista de los números de asientos ocupados.
        
        Returns:
            List[int]: Lista de números de asientos ocupados
        """
        return sorted(list(self.asientos.keys()))
        
    def obtener_asientos_disponibles(self) -> List[int]:
        """
        Retorna una lista de los números de asientos disponibles.
        
        Returns:
            List[int]: Lista de números de asientos disponibles
        """
        ocupados = set(self.asientos.keys())
        return [i for i in range(1, self.capacidad + 1) if i not in ocupados]