"""
Punto de entrada principal de la aplicación de gestión de buses.
"""
from src.interfaces.interfaz_usuario import InterfazUsuario

def main():
    """Inicia la aplicación de gestión de buses."""
    sistema = InterfazUsuario()
    sistema.iniciar()

if __name__ == "__main__":
    main()