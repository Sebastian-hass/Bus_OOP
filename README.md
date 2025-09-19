# Sistema de Gestión de Buses

Sistema de gestión de buses desarrollado en Python para la administración de ventas de billetes y control de asientos.

## Estructura del Proyecto

```
├── main.py                           # Punto de entrada
├── src/
│   ├── interfaces/
│   │   └── interfaz_usuario.py      # CLI interface
│   ├── models/
│   │   ├── bus.py                   # Clase Bus
│   │   ├── venta.py                 # Clase Venta
│   │   └── sistema_gestion_buses.py # Sistema principal
│   └── utils/
│       └── helpers.py               # Utilidades (UUID, fechas)
```

## Instalación

```bash
git clone <repository-url>
cd sistema-gestion-buses
python main.py
```

## Funcionalidades

- **Gestión de buses**: Creación y administración de múltiples buses
- **Venta de billetes**: Asignación automática de asientos disponibles
- **Devoluciones**: Liberación de asientos con reasignación inteligente
- **Estado en tiempo real**: Visualización de ocupación y disponibilidad

## Arquitectura

### Clases Principales

**`Bus`**
- Gestión de asientos mediante diccionario `{numero_asiento: Venta}`
- Asignación secuencial con reutilización de asientos liberados
- Validaciones de capacidad y disponibilidad

**`Venta`** 
- Registro de transacciones con UUID único
- Información de pasajero y asiento asignado
- Timestamp automático de creación

**`SistemaGestionBuses`**
- Administración centralizada de múltiples buses
- Numeración automática incremental
- Interface unificada de gestión

**`InterfazUsuario`**
- CLI interactiva con validaciones
- Manejo de errores y entrada de datos
- Menú contextual según estado del sistema

## Características Técnicas

### Gestión de Asientos
- Algoritmo de asignación: primer asiento disponible
- Estructura: `Dict[int, Venta]` para O(1) lookup
- Reasignación automática de asientos liberados

### Validaciones
- Capacidad positiva en creación de buses
- Verificación de disponibilidad antes de venta
- Validación de entrada de datos numéricos y strings

### Manejo de Estado
- Estado inmutable de ventas (properties de solo lectura)
- Sincronización automática entre bus y sistema
- Consistencia de datos garantizada

## API Interna

### Bus
```python
bus.vender_billete(nombre: str, apellido: str, cantidad: int) -> bool
bus.devolver_billete(numero_asiento: int) -> bool
bus.obtener_estado() -> str
```

### Sistema
```python
sistema.agregar_bus(capacidad: int) -> str
sistema.seleccionar_bus(numero: str) -> Optional[Bus]
sistema.mostrar_buses() -> str
```

## Uso

```bash
$ python main.py

=== SISTEMA DE GESTIÓN DE BUSES ===
1. Crear nuevo bus
2. Seleccionar bus  
3. Vender billete
4. Devolver billete
5. Ver estado de buses
0. Salir
```

## Dependencias

- Python 3.7+
- Módulos estándar: `uuid`, `datetime`, `typing`

## Estructura de Datos

### Bus
```python
{
    "numero": "1",
    "capacidad": 50,
    "asientos": {1: Venta_obj, 3: Venta_obj}  # asiento 2 libre
}
```

### Venta
```python
{
    "id": "uuid-string",
    "fecha": datetime,
    "cantidad": 1,
    "pasajero": {"nombre": str, "apellido": str, "asiento": int}
}
```# Sistema de Gestión de Buses

Sistema de gestión de buses desarrollado en Python para la administración de ventas de billetes y control de asientos.

## Estructura del Proyecto

```
├── main.py                           # Punto de entrada
├── src/
│   ├── interfaces/
│   │   └── interfaz_usuario.py      # CLI interface
│   ├── models/
│   │   ├── bus.py                   # Clase Bus
│   │   ├── venta.py                 # Clase Venta
│   │   └── sistema_gestion_buses.py # Sistema principal
│   └── utils/
│       └── helpers.py               # Utilidades (UUID, fechas)
```

## Instalación

```bash
git clone <repository-url>
cd sistema-gestion-buses
python main.py
```

## Funcionalidades

- **Gestión de buses**: Creación y administración de múltiples buses
- **Venta de billetes**: Asignación automática de asientos disponibles
- **Devoluciones**: Liberación de asientos con reasignación inteligente
- **Estado en tiempo real**: Visualización de ocupación y disponibilidad

## Arquitectura

### Clases Principales

**`Bus`**
- Gestión de asientos mediante diccionario `{numero_asiento: Venta}`
- Asignación secuencial con reutilización de asientos liberados
- Validaciones de capacidad y disponibilidad

**`Venta`** 
- Registro de transacciones con UUID único
- Información de pasajero y asiento asignado
- Timestamp automático de creación

**`SistemaGestionBuses`**
- Administración centralizada de múltiples buses
- Numeración automática incremental
- Interface unificada de gestión

**`InterfazUsuario`**
- CLI interactiva con validaciones
- Manejo de errores y entrada de datos
- Menú contextual según estado del sistema

## Características Técnicas

### Gestión de Asientos
- Algoritmo de asignación: primer asiento disponible
- Estructura: `Dict[int, Venta]` para O(1) lookup
- Reasignación automática de asientos liberados

### Validaciones
- Capacidad positiva en creación de buses
- Verificación de disponibilidad antes de venta
- Validación de entrada de datos numéricos y strings

### Manejo de Estado
- Estado inmutable de ventas (properties de solo lectura)
- Sincronización automática entre bus y sistema
- Consistencia de datos garantizada

## API Interna

### Bus
```python
bus.vender_billete(nombre: str, apellido: str, cantidad: int) -> bool
bus.devolver_billete(numero_asiento: int) -> bool
bus.obtener_estado() -> str
```

### Sistema
```python
sistema.agregar_bus(capacidad: int) -> str
sistema.seleccionar_bus(numero: str) -> Optional[Bus]
sistema.mostrar_buses() -> str
```

## Uso

```bash
$ python main.py

=== SISTEMA DE GESTIÓN DE BUSES ===
1. Crear nuevo bus
2. Seleccionar bus  
3. Vender billete
4. Devolver billete
5. Ver estado de buses
0. Salir
```

## Dependencias

- Python 3.7+
- Módulos estándar: `uuid`, `datetime`, `typing`

## Estructura de Datos

### Bus
```python
{
    "numero": "1",
    "capacidad": 50,
    "asientos": {1: Venta_obj, 3: Venta_obj}  # asiento 2 libre
}
```

### Venta
```python
{
    "id": "uuid-string",
    "fecha": datetime,
    "cantidad": 1,
    "pasajero": {"nombre": str, "apellido": str, "asiento": int}
}
```
