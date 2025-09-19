"""
Utilidades generales para el sistema de gestión de buses.
"""
from datetime import datetime
import uuid

def generar_id() -> str:
    """Genera un ID único para usar en el sistema."""
    return str(uuid.uuid4())

def obtener_fecha_actual() -> datetime:
    """Retorna la fecha y hora actual."""
    return datetime.now()