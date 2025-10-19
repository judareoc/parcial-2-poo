#!/usr/bin/env python3
"""
PARCIAL 2 - PROBLEMA INTEGRADOR (Parte 2)
Sistema de Gestión de Biblioteca Digital

Estudiante: _______________________________
Fecha: ____________________________________
"""

from datetime import datetime, timedelta

# ===========================================================================
# EXCEPCIONES PERSONALIZADAS (5 puntos)
# ===========================================================================

class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    """Se lanza cuando no hay copias disponibles."""
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    """Se lanza cuando el usuario no está registrado."""
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    """Se lanza cuando el usuario excede el límite de préstamos."""
    def __init__(self, id_usuario, limite):
        self.id_usuario = id_usuario
        self.limite = limite
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


class PrestamoVencido(ErrorBiblioteca):
    """Se lanza para operaciones con préstamos vencidos."""
    def __init__(self, id_prestamo, dias_retraso):
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        super().__init__(f"Préstamo {id_prestamo} está vencido por {dias_retraso} días")


# ===========================================================================
# CLASE PRINCIPAL: SISTEMA BIBLIOTECA (35 puntos)
# ===========================================================================

class SistemaBiblioteca:
    """
    Sistema completo de gestión de biblioteca digital.
    
    Estructuras de datos:
    - catalogo: {isbn: {'titulo', 'autor', 'anio', 'categoria', 'copias_total', 'copias_disponibles'}}
    - usuarios: {id_usuario: {'nombre', 'email', 'fecha_registro', 'prestamos_activos', 'historial'}}
    - prestamos: {id_prestamo: {'isbn', 'id_usuario', 'fecha_prestamo', 'fecha_vencimiento', 'fecha_devolucion', 'multa'}}
    """
    
    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        """
        Inicializa el sistema.
        
        Args:
            dias_prestamo: Días permitidos para cada préstamo
            multa_por_dia: Multa diaria por retraso
            limite_prestamos: Máximo de préstamos simultáneos por usuario
        """
        # TODO: Inicializar estructuras de datos y configuración
        pass
    
    # ============ GESTIÓN DE CATÁLOGO ============
    
    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        """
        Agrega un libro al catálogo.
        
        Validaciones:
        - ISBN debe ser string de 13 dígitos
        - Título y autor no vacíos
        - Año entre 1000 y año actual
        - Copias >= 1
        
        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si ISBN ya existe
        """
        # TODO: Implementar
        pass
    
    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).
        
        Raises:
            LibroNoEncontrado: Si ISBN no existe
            ValueError: Si resultado sería negativo
        """
        # TODO: Implementar
        pass
    
    def buscar_libros(self, criterio='titulo', valor='', categoria=None):
        """
        Busca libros por diferentes criterios.
        
        Args:
            criterio: 'titulo', 'autor', 'anio'
            valor: Valor a buscar (búsqueda parcial case-insensitive)
            categoria: Filtro opcional por categoría
        
        Returns:
            Lista de diccionarios con info de libros que coinciden
        """
        # TODO: Implementar
        pass
    
    # ============ GESTIÓN DE USUARIOS ============
    
    def registrar_usuario(self, id_usuario, nombre, email):
        """
        Registra un nuevo usuario.
        
        Validaciones:
        - Email debe contener '@' y '.'
        - Nombre no vacío
        - ID único
        
        Raises:
            ValueError: Si validaciones fallan
        """
        # TODO: Implementar
        pass
    
    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.
        
        Returns:
            dict con: nombre, prestamos_activos, puede_prestar, multas_pendientes
        
        Raises:
            UsuarioNoRegistrado: Si usuario no existe
        """
        # TODO: Implementar
        pass
    
    # ============ GESTIÓN DE PRÉSTAMOS ============
    
    def prestar_libro(self, isbn, id_usuario):
        """
        Realiza un préstamo.
        
        Validaciones:
        - Usuario registrado
        - Libro existe y disponible
        - Usuario no excede límite de préstamos
        - Usuario no tiene multas pendientes > 50
        
        Returns:
            id_prestamo: ID único del préstamo
        
        Raises:
            UsuarioNoRegistrado, LibroNoEncontrado, LibroNoDisponible,
            LimitePrestamosExcedido, ValueError (multas pendientes)
        """
        # TODO: Implementar
        pass
    
    def devolver_libro(self, id_prestamo):
        """
        Procesa devolución de libro.
        
        Calcula multa si hay retraso.
        Actualiza estado de libro y usuario.
        
        Returns:
            dict: {'dias_retraso': int, 'multa': float, 'mensaje': str}
        
        Raises:
            KeyError: Si préstamo no existe
            ValueError: Si ya fue devuelto
        """
        # TODO: Implementar
        pass
    
    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).
        
        Raises:
            PrestamoVencido: Si ya está vencido
            KeyError: Si préstamo no existe
        """
        # TODO: Implementar
        pass
    
    # ============ ESTADÍSTICAS Y REPORTES ============
    
    def libros_mas_prestados(self, n=10):
        """
        Retorna los N libros más prestados.
        
        Returns:
            Lista de tuplas: [(isbn, titulo, cantidad_prestamos), ...]
            Ordenada descendentemente por cantidad
        """
        # TODO: Implementar
        pass
    
    def usuarios_mas_activos(self, n=5):
        """
        Retorna los N usuarios más activos (más préstamos históricos).
        
        Returns:
            Lista de tuplas: [(id_usuario, nombre, total_prestamos), ...]
        """
        # TODO: Implementar
        pass
    
    def estadisticas_categoria(self, categoria):
        """
        Genera estadísticas de una categoría.
        
        Returns:
            dict: {
                'total_libros': int,
                'total_copias': int,
                'copias_prestadas': int,
                'tasa_prestamo': float,
                'libro_mas_popular': str
            }
        """
        # TODO: Implementar
        pass
    
    def prestamos_vencidos(self):
        """
        Lista préstamos actualmente vencidos.
        
        Returns:
            Lista de dicts con: id_prestamo, isbn, titulo, id_usuario,
            dias_retraso, multa_acumulada
        """
        # TODO: Implementar
        pass
    
    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        """
        Genera reporte financiero de multas.
        
        Args:
            fecha_inicio, fecha_fin: Rango de fechas (datetime)
            Si son None, usa todo el historial
        
        Returns:
            dict: {
                'total_multas': float,
                'multas_pagadas': float,
                'multas_pendientes': float,
                'prestamos_con_multa': int,
                'promedio_multa': float
            }
        """
        # TODO: Implementar
        pass
    
    # ============ UTILIDADES ============
    
    def exportar_catalogo(self, archivo='catalogo.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias
        
        Maneja excepciones de archivo apropiadamente.
        """
        # TODO: Implementar
        pass
    
    def importar_catalogo(self, archivo='catalogo.txt'):
        """
        Importa catálogo desde archivo de texto.
        
        Maneja:
        - Archivo no existe
        - Formato incorrecto
        - Duplicados (no sobrescribir)
        
        Returns:
            dict: {'exitosos': int, 'errores': [(linea, error), ...]}
        """
        # TODO: Implementar
        pass


# ===========================================================================
# CASOS DE PRUEBA BÁSICOS
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DEL SISTEMA DE BIBLIOTECA")
    print("="*70)
    
    # Crear instancia del sistema
    biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)
    
    # TODO: Añadir casos de prueba aquí
    
    print("\n✓ Sistema inicializado")
    print("  Añade tus pruebas para verificar la funcionalidad")
