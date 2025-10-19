#!/usr/bin/env python3
"""
PROBLEMA INTEGRADOR DE PRÁCTICA
Sistema de Gestión de Restaurante

Nombre: _______________________________
Fecha: ________________________________
"""

from datetime import datetime, time

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS
# ===========================================================================

class ErrorRestaurante(Exception):
    """Excepción base para el sistema de restaurante."""
    pass


class PlatoNoEncontrado(ErrorRestaurante):
    """Se lanza cuando un plato no existe en el menú."""
    def __init__(self, codigo_plato):
        self.codigo_plato = codigo_plato
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado en el menú")


class MesaNoDisponible(ErrorRestaurante):
    """Se lanza cuando la mesa está ocupada."""
    # TODO: Implementar __init__ con atributos numero_mesa y hora_disponible
    pass


class CapacidadExcedida(ErrorRestaurante):
    """Se lanza cuando hay más comensales que capacidad."""
    # TODO: Implementar __init__ con atributos numero_mesa, capacidad y comensales
    pass


class PedidoInvalido(ErrorRestaurante):
    """Se lanza para pedidos con problemas."""
    # TODO: Implementar __init__ con atributo razon
    pass


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA RESTAURANTE
# ===========================================================================

class SistemaRestaurante:
    """Sistema completo de gestión de restaurante."""
    
    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        """
        Inicializa el sistema.
        
        Args:
            num_mesas: Número total de mesas
            tasa_impuesto: Tasa de impuesto (IVA)
            propina_sugerida: Propina sugerida por defecto
        """
        # TODO: Inicializar estructuras de datos
        pass
    
    # ============ GESTIÓN DE MENÚ ============
    
    def agregar_plato(self, codigo, nombre, categoria, precio):
        """
        Agrega un plato al menú.
        
        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si código ya existe
        """
        # TODO: Implementar con validaciones
        pass
    
    def cambiar_disponibilidad(self, codigo, disponible):
        """
        Cambia disponibilidad de un plato.
        
        Raises:
            PlatoNoEncontrado: Si código no existe
        """
        # TODO: Implementar
        pass
    
    def buscar_platos(self, categoria=None, precio_max=None):
        """
        Busca platos por criterios.
        
        Returns:
            Lista de diccionarios con info de platos disponibles
        """
        # TODO: Implementar búsqueda con filtros
        pass
    
    # ============ GESTIÓN DE MESAS ============
    
    def configurar_mesa(self, numero, capacidad):
        """
        Configura capacidad de una mesa.
        
        Raises:
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar con validaciones
        pass
    
    def reservar_mesa(self, numero, comensales, hora):
        """
        Reserva una mesa.
        
        Raises:
            MesaNoDisponible: Si mesa ocupada
            CapacidadExcedida: Si comensales > capacidad
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar con validaciones
        pass
    
    def liberar_mesa(self, numero):
        """
        Libera una mesa (termina servicio).
        
        Raises:
            ValueError: Si mesa no existe o no está ocupada
        """
        # TODO: Implementar
        pass
    
    def mesas_disponibles(self, comensales):
        """
        Lista mesas disponibles para N comensales.
        
        Returns:
            Lista de números de mesa
        """
        # TODO: Implementar filtrado
        pass
    
    # ============ GESTIÓN DE PEDIDOS ============
    
    def crear_pedido(self, numero_mesa):
        """
        Crea un nuevo pedido para una mesa.
        
        Returns:
            id_pedido: ID único del pedido
        
        Raises:
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar creación de pedido
        pass
    
    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        """
        Agrega items al pedido.
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
            PlatoNoEncontrado: Si plato no existe
            ValueError: Si plato no disponible
        """
        # TODO: Implementar con validaciones
        pass
    
    def calcular_total(self, id_pedido, propina_porcentaje=None):
        """
        Calcula total del pedido.
        
        Returns:
            dict con subtotal, impuesto, propina, total
        """
        # TODO: Implementar cálculos
        pass
    
    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        """
        Procesa pago del pedido.
        
        Returns:
            dict con totales
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
        """
        # TODO: Implementar procesamiento de pago
        pass
    
    # ============ REPORTES Y ESTADÍSTICAS ============
    
    def platos_mas_vendidos(self, n=5):
        """
        Retorna los N platos más vendidos del día.
        
        Returns:
            Lista de tuplas (codigo, nombre, cantidad_vendida)
        """
        # TODO: Implementar conteo y ordenamiento
        pass
    
    def ventas_por_categoria(self):
        """
        Calcula ventas totales por categoría.
        
        Returns:
            dict con ventas por categoría
        """
        # TODO: Implementar agrupación
        pass
    
    def reporte_ventas_dia(self):
        """
        Genera reporte completo de ventas del día.
        
        Returns:
            dict con estadísticas completas
        """
        # TODO: Implementar reporte completo
        pass
    
    def estado_restaurante(self):
        """
        Estado actual del restaurante.
        
        Returns:
            dict con estado de mesas y pedidos
        """
        # TODO: Implementar resumen de estado
        pass
    
    # ============ UTILIDADES ============
    
    def exportar_menu(self, archivo='menu.txt'):
        """
        Exporta menú a archivo de texto.
        Formato: Codigo|Nombre|Categoria|Precio|Disponible
        """
        # TODO: Implementar exportación
        pass
    
    def importar_menu(self, archivo='menu.txt'):
        """
        Importa menú desde archivo de texto.
        
        Returns:
            dict con exitosos y errores
        """
        # TODO: Implementar importación con manejo de errores
        pass


# ===========================================================================
# EJEMPLO DE USO
# ===========================================================================

if __name__ == "__main__":
    print("=" * 70)
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("=" * 70)
    
    # Crear sistema
    restaurante = SistemaRestaurante(num_mesas=5)
    
    # Aquí puedes probar tu implementación
    print("\nAgrega tus pruebas aquí...")
