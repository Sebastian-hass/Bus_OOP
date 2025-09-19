"""
Módulo que contiene la implementación de la clase Venta.
"""
from datetime import datetime
from typing import Dict
from src.utils.helpers import generar_id, obtener_fecha_actual

class Venta:
    """
    Clase que representa una venta de billetes en el sistema.
    
    Attributes:
        id (str): Identificador único de la venta
        fecha (datetime): Fecha y hora de la venta
        cantidad (int): Cantidad de billetes vendidos
        pasajero (Dict): Información básica del pasajero
    """
    
    def __init__(self, cantidad: int, nombre: str, apellido: str, asiento: int):
        """
        Inicializa una nueva venta.
        
        Args:
            cantidad (int): Número de billetes vendidos
            nombre (str): Nombre del pasajero
            apellido (str): Apellido del pasajero
            asiento (int): Número de asiento asignado
        """
        self._id = generar_id()
        self._fecha = obtener_fecha_actual()
        self._cantidad = cantidad
        self._pasajero = {
            "nombre": nombre,
            "apellido": apellido,
            "asiento": asiento
        }
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def fecha(self) -> datetime:
        return self._fecha
    
    @property
    def cantidad(self) -> int:
        return self._cantidad
    
    @property
    def pasajero(self) -> Dict:
        return self._pasajero
    
    def obtener_detalles(self) -> Dict:
        """
        Obtiene los detalles completos de la venta.
        """
        return {
            'id': self._id,
            'fecha': self._fecha.isoformat(),
            'cantidad': self._cantidad,
            'pasajero': self._pasajero
        }
    
    def __str__(self) -> str:
        return (
            f"Venta {self._id}: {self._cantidad} billete(s) - "
            f"Pasajero: {self._pasajero['nombre']} {self._pasajero['apellido']} "
            f"(Asiento {self._pasajero['asiento']})"
        )