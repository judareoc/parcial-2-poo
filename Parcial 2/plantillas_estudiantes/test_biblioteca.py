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
    
    # Libro válido
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    assert "9780134685991" in biblioteca.catalogo

    # Duplicado
    try:
        biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    except KeyError:
        print("✓ Duplicado controlado correctamente")

    # ISBN inválido
    try:
        biblioteca.agregar_libro("123", "Libro malo", "Autor", 2020, "Programación", 2)
    except ValueError:
        print("✓ ISBN inválido detectado")

    # Año inválido
    try:
        biblioteca.agregar_libro("9780134685999", "Libro futuro", "Autor", 3020, "Programación", 1)
    except ValueError:
        print("✓ Año inválido detectado")
    
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
    biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
    assert "U001" in biblioteca.usuarios


    try:
        biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
    except ValueError:
        print("✓ Duplicado controlado")


    try:
        biblioteca.registrar_usuario("U002", "Carlos López", "carlosmail")
    except ValueError:
        print("✓ Email inválido detectado")
        
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
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")


    id_p = biblioteca.prestar_libro("9780134685991", "U001")
    assert id_p in biblioteca.prestamos


    try:
        biblioteca.prestar_libro("9780134685991", "U001")
    except LibroNoDisponible:
        print("✓ Libro no disponible detectado")


    try:
        biblioteca.prestar_libro("9780134685991", "U999")
    except UsuarioNoRegistrado:
        print("✓ Usuario no registrado detectado")
    
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
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")


    id_p = biblioteca.prestar_libro("9780134685991", "U001")
    biblioteca.prestamos[id_p]['fecha_vencimiento'] = datetime.now() - timedelta(days=3)
    resultado = biblioteca.devolver_libro(id_p)
    assert resultado['multa'] == 6.0
    print("✓ Multa calculada correctamente")
    
        
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
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    biblioteca.agregar_libro("9780135404676", "Python Crash Course", "Eric Matthes", 2019, "Programación", 3)


    res = biblioteca.buscar_libros(criterio='titulo', valor='python')
    assert len(res) >= 1
    print("✓ Búsqueda por título exitosa")


    res = biblioteca.buscar_libros(criterio='autor', valor='brett')
    assert len(res) == 1
    print("✓ Búsqueda por autor exitosa")


    res = biblioteca.buscar_libros(categoria='Programación')
    assert len(res) == 2
    print("✓ Filtro por categoría exitoso")
    
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
    biblioteca = SistemaBiblioteca()
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
    id_p = biblioteca.prestar_libro("9780134685991", "U001")
    biblioteca.devolver_libro(id_p)


    mas = biblioteca.libros_mas_prestados()
    assert mas[0][0] == "9780134685991"
    print("✓ Libros más prestados correcto")
    
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
    try:
        raise LibroNoEncontrado("1234567890123")
    except LibroNoEncontrado as e:
        print(e)
    try:
        raise LimitePrestamosExcedido("U001", 3)
    except LimitePrestamosExcedido as e:
        print(e)
    
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
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
    
    ruta = "catalogo_inicial.txt"  # Ruta relativa mejor
    biblioteca.exportar_catalogo(ruta)
    
    nueva = SistemaBiblioteca()
    res = nueva.importar_catalogo(ruta)
    
    assert res['exitosos'] >= 1
    
    print("✓ Prueba completada")


def prueba_renovar_prestamo():
    """Prueba renovación de préstamos."""
    print("\n" + "="*60)
    print(" TEST: Renovación de Préstamos")
    print("="*60)
    
    # 1. Configuración inicial
    biblioteca = SistemaBiblioteca(dias_prestamo=10) # 10 días para que sea fácil de ver
    biblioteca.agregar_libro("1111111111111", "Libro Válido", "Autor", 2020, "Test", 2)
    biblioteca.agregar_libro("2222222222222", "Libro Vencido", "Autor", 2021, "Test", 1)
    biblioteca.registrar_usuario("U-TEST", "Usuario de Prueba", "test@email.com")
    
    # --- Caso 1: Renovar un préstamo válido ---
    print("\n Caso 1: Renovar un préstamo válido.")
    try:
        id_valido = biblioteca.prestar_libro("1111111111111", "U-TEST")
        prestamo_original = biblioteca.prestamos[id_valido]
        fecha_vencimiento_original = prestamo_original['fecha_vencimiento']
        
        print(f"Fecha de vencimiento original: {fecha_vencimiento_original.strftime('%Y-%m-%d')}")
        
        biblioteca.renovar_prestamo(id_valido) # Intentamos la renovación
        
        fecha_vencimiento_nueva = prestamo_original['fecha_vencimiento']
        print(f"Nueva fecha de vencimiento:   {fecha_vencimiento_nueva.strftime('%Y-%m-%d')}")
        
        # Verificamos que la fecha realmente cambió
        if fecha_vencimiento_nueva > fecha_vencimiento_original:
            print("El préstamo se renovó correctamente y la fecha se extendió.")
        else:
            print("El préstamo se renovó pero la fecha no se actualizó.")
            
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

    # --- Caso 2: Intentar renovar un préstamo vencido ---
    print("\nIntentar renovar un préstamo ya vencido.")
    try:
        id_vencido = biblioteca.prestar_libro("2222222222222", "U-TEST")
        
        # Forzamos que el préstamo esté vencido
        print("   Simulando un retraso de 5 días...")
        biblioteca.prestamos[id_vencido]['fecha_vencimiento'] = datetime.now() - timedelta(days=5)
        
        biblioteca.renovar_prestamo(id_vencido) # Esto debería lanzar la excepción
        
        # Si el código llega aquí, la prueba falló porque no se lanzó la excepción
        print("Se renovó un préstamo que estaba vencido.")
        
    except PrestamoVencido as e:
        print(f"Se capturó la excepción esperada correctamente.")
        print(f"Mensaje: '{e}'")
    except Exception as e:
        print(f"Se lanzó una excepción incorrecta o inesperada: {type(e).__name__}")

    # --- Caso 3: Intentar renovar un préstamo inexistente ---
    print("\nIntentar renovar un préstamo con un ID inexistente.")
    try:
        id_inexistente = "P999"
        print(f"   Intentando renovar el préstamo con ID: {id_inexistente}")
        biblioteca.renovar_prestamo(id_inexistente)
        
        # Si el código llega aquí, la prueba falló
        print(f"No se lanzó ninguna excepción para un ID inexistente.")
        
    except KeyError:
        print(f"Se capturó la excepción 'KeyError' esperada para un préstamo no encontrado.")
    except Exception as e:
        print(f"Se lanzó una excepción incorrecta o inesperada: {type(e).__name__}")
    
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
    
    biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 1)
    biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
    print("Libro 'Effective Python' agregado al catálogo.")
    print("Usuario 'Ana García' registrado con ID 'U001'.")
    
    # 2️⃣ Crear préstamo
    id_p = biblioteca.prestar_libro("9780134685991", "U001")
    print(f"Préstamo '{id_p}' realizado: 'Effective Python' a 'Ana García'.")
    
    # 3️⃣ Simular retraso (5 días)
    biblioteca.prestamos[id_p]['fecha_vencimiento'] = datetime.now() - timedelta(days=5)
    biblioteca.devolver_libro(id_p)
    
    # 4️⃣ Generar reporte financiero
    reporte = biblioteca.reporte_financiero()
    print("Reporte generado:", reporte)
    
    # 5️⃣ Validaciones
    assert 'total_multas_generadas' in reporte, "Falta clave 'total_multas_generadas'"
    assert reporte['total_multas_generadas'] > 0, "No se calcularon multas"
    assert 'multas_cobradas' in reporte
    assert 'multas_pendientes' in reporte
    assert 'prestamos_con_multa' in reporte
    assert 'promedio_multa' in reporte
    
    print("✓ Reporte financiero correcto")
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
