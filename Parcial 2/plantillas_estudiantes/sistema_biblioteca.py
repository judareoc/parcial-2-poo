#!/usr/bin/env python3
"""
PARCIAL 2 - PROBLEMA INTEGRADOR (Parte 2)
Sistema de Gestión de Biblioteca Digital

Estudiante: _______________________________
Fecha: ____________________________________
"""

from datetime import datetime, timedelta
from collections import Counter

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
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self._next_prestamo_id = 1
        
        # Configuración
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = float(multa_por_dia)
        self.limite_prestamos = limite_prestamos
        
    
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
        if not (isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()):
            raise ValueError("ISBN debe ser un string de 13 dígitos numéricos.")
        if isbn in self.catalogo:
            raise KeyError(f"El ISBN {isbn} ya existe en el catálogo.")
        if not titulo or not autor:
            raise ValueError("Título y autor no pueden estar vacíos.")
        if not (isinstance(anio, int) and 1000 <= anio <= datetime.now().year):
            raise ValueError(f"Año debe ser un entero entre 1000 y {datetime.now().year}.")
        if not (isinstance(copias, int) and copias >= 1):
            raise ValueError("El número de copias debe ser al menos 1.")

        self.catalogo[isbn] = {
            'titulo': titulo,
            'autor': autor,
            'anio': anio,
            'categoria': categoria,
            'copias_total': copias,
            'copias_disponibles': copias
        }
        print(f"Libro '{titulo}' agregado al catálogo.")
    
    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).
        
        Raises:
            LibroNoEncontrado: Si ISBN no existe
            ValueError: Si resultado sería negativo
        """
        # Implementar
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
        
        libro = self.catalogo[isbn]
        copias_actuales_totales = libro['copias_total']
        copias_actuales_disponibles = libro['copias_disponibles']

        if (copias_actuales_totales + cantidad_cambio < 0) or \
           (copias_actuales_disponibles + cantidad_cambio < 0):
            raise ValueError("La actualización resultaría en un número negativo de copias.")
        
        libro['copias_total'] += cantidad_cambio
        libro['copias_disponibles'] += cantidad_cambio
        print(f"Copias de '{libro['titulo']}' actualizadas. Total: {libro['copias_total']}, Disponibles: {libro['copias_disponibles']}.")
    
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
        # Implementar
        resultados = []
        valor_lower = str(valor).lower()

        for isbn, libro in self.catalogo.items():
            # Filtrado por categoría
            if categoria and libro['categoria'].lower() != categoria.lower():
                continue
            
            # Búsqueda por criterio
            valor_a_comparar = str(libro.get(criterio, '')).lower()
            if valor_lower in valor_a_comparar:
                # Añade el ISBN al diccionario del libro para el resultado
                info_libro = libro.copy()
                info_libro['isbn'] = isbn
                resultados.append(info_libro)
                
        return resultados
    
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
        # Implementar
        if id_usuario in self.usuarios:
            raise ValueError(f"El ID de usuario '{id_usuario}' ya está registrado.")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if '@' not in email or '.' not in email:
            raise ValueError("El formato del email no es válido.")

        self.usuarios[id_usuario] = {
            'nombre': nombre,
            'email': email,
            'fecha_registro': datetime.now(),
            'prestamos_activos': [],
            'historial': []
        }
        print(f"Usuario '{nombre}' registrado con ID '{id_usuario}'.")
    
    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.
        
        Returns:
            dict con: nombre, prestamos_activos, puede_prestar, multas_pendientes
        
        Raises:
            UsuarioNoRegistrado: Si usuario no existe
        """
        # Implementar
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        
        usuario = self.usuarios[id_usuario]
        multas_pendientes = 0.0
        
        # Calcula multas de préstamos vencidos y no devueltos
        for id_prestamo in usuario['prestamos_activos']:
            prestamo = self.prestamos[id_prestamo]
            if datetime.now() > prestamo['fecha_vencimiento']:
                dias_retraso = (datetime.now() - prestamo['fecha_vencimiento']).days
                multas_pendientes += dias_retraso * self.multa_por_dia

        return {
            'nombre': usuario['nombre'],
            'prestamos_activos': usuario['prestamos_activos'],
            'puede_prestar': len(usuario['prestamos_activos']) < self.limite_prestamos,
            'multas_pendientes': round(multas_pendientes, 2)
        }
    
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
        # Implementar
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)
        
        usuario = self.usuarios[id_usuario]
        libro = self.catalogo[isbn]

        if libro['copias_disponibles'] < 1:
            raise LibroNoDisponible(isbn, libro['titulo'])
        if len(usuario['prestamos_activos']) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)
        
        
        # Actualizar datos
        libro['copias_disponibles'] -= 1
        
        id_prestamo = f"P{self._next_prestamo_id}"
        self._next_prestamo_id += 1
        
        fecha_prestamo = datetime.now()
        fecha_vencimiento = fecha_prestamo + timedelta(days=self.dias_prestamo)
        
        self.prestamos[id_prestamo] = {
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha_prestamo': fecha_prestamo,
            'fecha_vencimiento': fecha_vencimiento,
            'fecha_devolucion': None,
            'multa': 0.0
        }
        
        usuario['prestamos_activos'].append(id_prestamo)
        usuario['historial'].append(id_prestamo)
        
        print(f"Préstamo '{id_prestamo}' realizado: '{libro['titulo']}' a '{usuario['nombre']}'.")
        return id_prestamo
    
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
        #  Implementar
        if id_prestamo not in self.prestamos:
            raise KeyError(f"Préstamo con ID '{id_prestamo}' no existe.")
        
        prestamo = self.prestamos[id_prestamo]
        if prestamo['fecha_devolucion'] is not None:
            raise ValueError(f"El préstamo '{id_prestamo}' ya fue devuelto.")

        # Calcular multa
        dias_retraso = 0
        multa = 0.0
        hoy = datetime.now()
        if hoy > prestamo['fecha_vencimiento']:
            dias_retraso = (hoy - prestamo['fecha_vencimiento']).days
            multa = round(dias_retraso * self.multa_por_dia, 2)

        # Actualizar registros
        prestamo['fecha_devolucion'] = hoy
        prestamo['multa'] = multa
        
        self.catalogo[prestamo['isbn']]['copias_disponibles'] += 1
        self.usuarios[prestamo['id_usuario']]['prestamos_activos'].remove(id_prestamo)
        
        mensaje = f"Devolución de '{self.catalogo[prestamo['isbn']]['titulo']}' completada."
        if dias_retraso > 0:
            mensaje += f" Se aplicó una multa de ${multa} por {dias_retraso} días de retraso."

        return {'dias_retraso': dias_retraso, 'multa': multa, 'mensaje': mensaje}
    
    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).
        
        Raises:
            PrestamoVencido: Si ya está vencido
            KeyError: Si préstamo no existe
        """
        # Implementar
        if id_prestamo not in self.prestamos:
            raise KeyError(f"Préstamo con ID '{id_prestamo}' no existe.")
            
        prestamo = self.prestamos[id_prestamo]
        hoy = datetime.now()
        
        if hoy > prestamo['fecha_vencimiento']:
            dias_retraso = (hoy - prestamo['fecha_vencimiento']).days
            raise PrestamoVencido(id_prestamo, dias_retraso)
        
        prestamo['fecha_vencimiento'] += timedelta(days=self.dias_prestamo)
        print(f"Prestamo '{id_prestamo}' renovado. Nueva fecha de vencimiento: {prestamo['fecha_vencimiento'].strftime('%Y-%m-%d')}.")
    
    # ============ ESTADÍSTICAS Y REPORTES ============
    
    def libros_mas_prestados(self, n=10):
        """
        Retorna los N libros más prestados.
        
        Returns:
            Lista de tuplas: [(isbn, titulo, cantidad_prestamos), ...]
            Ordenada descendentemente por cantidad
        """
        #  Implementar
        if not self.prestamos: return []
        contador_isbn = Counter(p['isbn'] for p in self.prestamos.values())
        mas_comunes = contador_isbn.most_common(n)
        return [(isbn, self.catalogo[isbn]['titulo'], cantidad) for isbn, cantidad in mas_comunes]
    
    def usuarios_mas_activos(self, n=5):
        """
        Retorna los N usuarios más activos (más préstamos históricos).
        
        Returns:
            Lista de tuplas: [(id_usuario, nombre, total_prestamos), ...]
        """
        # Implementar
        if not self.prestamos: return []
        contador_usuarios = Counter(p['id_usuario'] for p in self.prestamos.values())
        mas_activos = contador_usuarios.most_common(n)
        return [(uid, self.usuarios[uid]['nombre'], cantidad) for uid, cantidad in mas_activos]
    
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
        #  Implementar
        libros_categoria = [l for l in self.catalogo.values() if l['categoria'].lower() == categoria.lower()]
        if not libros_categoria: return {}
        
        total_libros = len(libros_categoria)
        total_copias = sum(l['copias_total'] for l in libros_categoria)
        copias_disponibles = sum(l['copias_disponibles'] for l in libros_categoria)
        copias_prestadas = total_copias - copias_disponibles
        tasa_prestamo = (copias_prestadas / total_copias) * 100 if total_copias > 0 else 0
        
        # Libro más popular de la categoría
        isbns_categoria = [isbn for isbn, libro in self.catalogo.items() if libro['categoria'].lower() == categoria.lower()]
        prestamos_categoria = [p['isbn'] for p in self.prestamos.values() if p['isbn'] in isbns_categoria]
        libro_mas_popular_titulo = "N/A"
        if prestamos_categoria:
            isbn_popular = Counter(prestamos_categoria).most_common(1)[0][0]
            libro_mas_popular_titulo = self.catalogo[isbn_popular]['titulo']

        return {
            'total_libros': total_libros,
            'total_copias': total_copias,
            'copias_prestadas': copias_prestadas,
            'tasa_prestamo': round(tasa_prestamo, 2),
            'libro_mas_popular': libro_mas_popular_titulo
        }
    
    def prestamos_vencidos(self):
        """
        Lista préstamos actualmente vencidos.
        
        Returns:
            Lista de dicts con: id_prestamo, isbn, titulo, id_usuario,
            dias_retraso, multa_acumulada
        """
        #  Implementar
        vencidos = []
        hoy = datetime.now()
        for id_p, prestamo in self.prestamos.items():
            if prestamo['fecha_devolucion'] is None and hoy > prestamo['fecha_vencimiento']:
                dias_retraso = (hoy - prestamo['fecha_vencimiento']).days
                vencidos.append({
                    'id_prestamo': id_p,
                    'isbn': prestamo['isbn'],
                    'titulo': self.catalogo[prestamo['isbn']]['titulo'],
                    'id_usuario': prestamo['id_usuario'],
                    'dias_retraso': dias_retraso,
                    'multa_acumulada': round(dias_retraso * self.multa_por_dia, 2)
                })
        return vencidos
    
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
        # implementar
        prestamos_filtrados = self.prestamos.values()
        if fecha_inicio:
            prestamos_filtrados = [p for p in prestamos_filtrados if p['fecha_prestamo'] >= fecha_inicio]
        if fecha_fin:
            prestamos_filtrados = [p for p in prestamos_filtrados if p['fecha_prestamo'] <= fecha_fin]
        
        total_multas = sum(p['multa'] for p in prestamos_filtrados)
        multas_pagadas = sum(p['multa'] for p in prestamos_filtrados if p['fecha_devolucion'] is not None and p['multa'] > 0)
        prestamos_con_multa = sum(1 for p in prestamos_filtrados if p['multa'] > 0)
        
        # Las multas pendientes son las de préstamos vencidos aún no devueltos
        multas_pendientes = sum(v['multa_acumulada'] for v in self.prestamos_vencidos())

        promedio_multa = (total_multas / prestamos_con_multa) if prestamos_con_multa > 0 else 0

        return {
            'total_multas_generadas': round(total_multas, 2),
            'multas_cobradas': round(multas_pagadas, 2),
            'multas_pendientes': round(multas_pendientes, 2),
            'prestamos_con_multa': prestamos_con_multa,
            'promedio_multa': round(promedio_multa, 2)
        }
        
    
    # ============ UTILIDADES ============
    
    def exportar_catalogo(self, archivo='catalogo.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias
        
        Maneja excepciones de archivo apropiadamente.
        """
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for isbn, libro in self.catalogo.items():
                    linea = (f"{isbn}|{libro['titulo']}|{libro['autor']}|"
                             f"{libro['anio']}|{libro['categoria']}|{libro['copias_total']}\n")
                    f.write(linea)
            print(f"Catalogo exportado exitosamente a '{archivo}'.")
        except IOError as e:
            print(f"Error al exportar el catálogo a '{archivo}': {e}")
    
    def importar_catalogo(self, archivo='catalogo_inicial.txt'):
        """
        Importa catálogo desde archivo de texto.
        
        Maneja:
        - Archivo no existe
        - Formato incorrecto
        - Duplicados (no sobrescribir)
        
        Returns:
            dict: {'exitosos': int, 'errores': [(linea, error), ...]}
        """
        exitosos = 0
        errores = []
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                for i, linea in enumerate(f, 1):
                    linea = linea.strip()
                    if not linea: continue
                    
                    partes = linea.split('|')
                    if len(partes) != 6:
                        errores.append((i, f"Formato incorrecto: se esperaban 6 campos, se encontraron {len(partes)}."))
                        continue
                    
                    try:
                        isbn, titulo, autor, anio_str, categoria, copias_str = partes
                        anio = int(anio_str)
                        copias = int(copias_str)
                        # Usamos agregar_libro para aprovechar sus validaciones
                        self.agregar_libro(isbn, titulo, autor, anio, categoria, copias)
                        exitosos += 1
                    except (ValueError, KeyError) as e:
                        # KeyError si el ISBN ya existe, ValueError por datos inválidos
                        errores.append((i, str(e)))
                    except Exception as e:
                        errores.append((i, f"Error inesperado: {e}"))
            print(f"Importación desde '{archivo}' completada.")
        except FileNotFoundError:
            print(f"Error: El archivo de importación '{archivo}' no fue encontrado.")
            return {'exitosos': 0, 'errores': [(0, f"Archivo '{archivo}' no encontrado")]}
        except IOError as e:
            print(f"Error al leer el archivo '{archivo}': {e}")
            return {'exitosos': 0, 'errores': [(0, f"Error de I/O: {e}")]}
            
        return {'exitosos': exitosos, 'errores': errores}


# ===========================================================================
# CASOS DE PRUEBA BÁSICOS
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DEL SISTEMA DE BIBLIOTECA")
    print("="*70)
    
    # Crear instancia del sistema
    biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)
    
    print("===== 1. Importando Libros desde Archivo =====")
    ruta = r"C:\Users\Juan Restrepo\OneDrive - Universidad Libre\Escritorio\Parcial 2 poo\Parcial 2\plantillas_estudiantes\catalogo_inicial.txt"
    resultado_import = biblioteca.importar_catalogo(ruta)
    print(f"Importación exitosa: {resultado_import['exitosos']} libros.")
    if resultado_import['errores']:
        print("Errores durante la importación:")
        for linea, error in resultado_import['errores']:
            print(f"  - Línea {linea}: {error}")
    print("-" * 20)
    
    print("\n===== 2. Registrando Usuarios =====")
    biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
    biblioteca.registrar_usuario("U002", "Carlos López", "carlos@email.com")
    biblioteca.registrar_usuario("U003", "Beatriz Fernández", "bea@email.com")
    print("-" * 20)


    print("\n===== 3. Realizando Préstamos Válidos =====")
    try:
        id_p1 = biblioteca.prestar_libro("9780134685991", "U001") # Effective Python
        id_p2 = biblioteca.prestar_libro("9780135404676", "U001") # Python Crash Course
        id_p3 = biblioteca.prestar_libro("9788437604947", "U002") # La casa de los espíritus
        print(f"Préstamos realizados: {id_p1}, {id_p2}, {id_p3}")
    except ErrorBiblioteca as e:
        print(f"Error inesperado: {e}")
    print("-" * 20)


    print("\n===== 4. Buscando Libros =====")
    print("Buscando libros de 'Programación':")
    resultados = biblioteca.buscar_libros(criterio='categoria', valor='Programación')
    for libro in resultados:
        print(f"  - {libro['titulo']} de {libro['autor']}")
    print(f"Total encontrados: {len(resultados)}")
    print("-" * 20)

    print("\n===== 5. Devolución con Retraso (Simulación) =====")
    # --- Simulación de retraso: Modificamos la fecha de vencimiento a hace 5 días ---
    try:
        prestamo_a_modificar = biblioteca.prestamos[id_p1]
        prestamo_a_modificar['fecha_vencimiento'] = datetime.now() - timedelta(days=5)
        print(f"Simulando retraso para el préstamo {id_p1}...")

        resultado_dev = biblioteca.devolver_libro(id_p1)
        print(f"Resultado de la devolución: {resultado_dev['mensaje']}")
    except KeyError:
        print("Error: El préstamo a simular no fue encontrado.")
    print("-" * 20)


    print("\n===== 6. Estadísticas y Reportes =====")
    print("Libros más prestados:")
    print(biblioteca.libros_mas_prestados(3))

    print("\nEstadísticas de la categoría 'Programación':")
    print(biblioteca.estadisticas_categoria("Programación"))

    print("\nReporte Financiero:")
    print(biblioteca.reporte_financiero())

    print("\nPrestamos Vencidos (antes de simular otro):")
    print(biblioteca.prestamos_vencidos())
    # Simulamos que el préstamo de Carlos también está vencido
    biblioteca.prestamos[id_p1]['fecha_vencimiento'] = datetime.now() - timedelta(days=2)
    print("\nPrestamos Vencidos (después de simular otro):")
    print(biblioteca.prestamos_vencidos())
    print("-" * 20)
        
    print("\n✓ Sistema inicializado")
  