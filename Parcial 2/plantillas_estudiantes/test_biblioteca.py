#!/usr/bin/env python3
"""
PARCIAL 2 - CASOS DE PRUEBA
Sistema de Biblioteca Digital

Estudiante: _______________________________
Fecha: ____________________________________
"""

from sistema_biblioteca import *

def prueba_agregar_libros():
    """Prueba agregar libros al catálogo."""
    print("\n" + "="*60)
    print(" TEST: Agregar Libros")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Agregar libro válido
    # - Intentar agregar libro duplicado
    # - Agregar libro con ISBN inválido
    # - Agregar libro con año inválido
    
    print("✓ Prueba completada")


def prueba_registrar_usuarios():
    """Prueba registro de usuarios."""
    print("\n" + "="*60)
    print(" TEST: Registrar Usuarios")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Registrar usuario válido
    # - Intentar registrar usuario duplicado
    # - Registrar con email inválido
    
    print("✓ Prueba completada")


def prueba_prestar_libros():
    """Prueba sistema de préstamos."""
    print("\n" + "="*60)
    print(" TEST: Préstamos")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(limite_prestamos=3)
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Préstamo exitoso
    # - Intentar prestar libro no disponible
    # - Exceder límite de préstamos
    # - Préstamo con usuario no registrado
    
    print("✓ Prueba completada")


def prueba_devolver_libros():
    """Prueba devolución y cálculo de multas."""
    print("\n" + "="*60)
    print(" TEST: Devolución y Multas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(multa_por_dia=2.0)
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Devolución a tiempo (sin multa)
    # - Devolución con retraso (con multa)
    # - Intentar devolver préstamo inexistente
    
    print("✓ Prueba completada")


def prueba_buscar_libros():
    """Prueba búsqueda de libros."""
    print("\n" + "="*60)
    print(" TEST: Búsqueda de Libros")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Búsqueda por título
    # - Búsqueda por autor
    # - Búsqueda con filtro de categoría
    # - Búsqueda sin resultados
    
    print("✓ Prueba completada")


def prueba_estadisticas():
    """Prueba generación de estadísticas."""
    print("\n" + "="*60)
    print(" TEST: Estadísticas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Libros más prestados
    # - Usuarios más activos
    # - Estadísticas por categoría
    # - Préstamos vencidos
    
    print("✓ Prueba completada")


def prueba_excepciones():
    """Prueba manejo de excepciones personalizadas."""
    print("\n" + "="*60)
    print(" TEST: Excepciones Personalizadas")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Verificar que se lanzan correctamente:
    # - LibroNoEncontrado
    # - LibroNoDisponible
    # - UsuarioNoRegistrado
    # - LimitePrestamosExcedido
    
    print("✓ Prueba completada")


def prueba_importar_exportar():
    """Prueba importar/exportar catálogo."""
    print("\n" + "="*60)
    print(" TEST: Importar/Exportar")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Exportar catálogo
    # - Importar catálogo
    # - Manejo de errores en importación
    
    print("✓ Prueba completada")


def prueba_renovar_prestamo():
    """Prueba renovación de préstamos."""
    print("\n" + "="*60)
    print(" TEST: Renovación de Préstamos")
    print("="*60)
    
    biblioteca = SistemaBiblioteca()
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Renovar préstamo válido
    # - Intentar renovar préstamo vencido
    # - Renovar préstamo inexistente
    
    print("✓ Prueba completada")


def prueba_reporte_financiero():
    """Prueba reporte financiero."""
    print("\n" + "="*60)
    print(" TEST: Reporte Financiero")
    print("="*60)
    
    biblioteca = SistemaBiblioteca(multa_por_dia=2.0)
    
    # TODO: Implementar pruebas
    # Casos a probar:
    # - Reporte sin multas
    # - Reporte con multas
    # - Reporte con rango de fechas
    
    print("✓ Prueba completada")


# ===========================================================================
# EJECUTAR TODAS LAS PRUEBAS
# ===========================================================================

def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del sistema."""
    print("\n" + "="*70)
    print(" EJECUTANDO SUITE COMPLETA DE PRUEBAS")
    print("="*70)
    
    pruebas = [
        prueba_agregar_libros,
        prueba_registrar_usuarios,
        prueba_prestar_libros,
        prueba_devolver_libros,
        prueba_buscar_libros,
        prueba_estadisticas,
        prueba_excepciones,
        prueba_importar_exportar,
        prueba_renovar_prestamo,
        prueba_reporte_financiero
    ]
    
    exitosas = 0
    fallidas = 0
    
    for prueba in pruebas:
        try:
            prueba()
            exitosas += 1
        except Exception as e:
            print(f"✗ Error en {prueba.__name__}: {e}")
            fallidas += 1
    
    print("\n" + "="*70)
    print(" RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"✓ Exitosas: {exitosas}/{len(pruebas)}")
    print(f"✗ Fallidas: {fallidas}/{len(pruebas)}")
    print("="*70)


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
