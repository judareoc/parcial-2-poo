# PARCIAL INTEGRADOR - PROGRAMACIÓN ORIENTADA A OBJETOS

**Curso:** Programación Orientada a Objetos  
**Total:** 100 puntos

---

## 📋 Instrucciones Generales

1. **Lee cuidadosamente** cada enunciado antes de comenzar
2. **Gestiona tu tiempo** apropiadamente (1 hora por sección)
3. **Escribe código limpio** con nombres descriptivos de variables
4. **Comenta tu código** cuando sea necesario
5. **Maneja las excepciones** apropiadamente
6. **Prueba tu código** antes de entregarlo

**Criterios de Evaluación:**
- Corrección funcional del código (50%)
- Manejo apropiado de excepciones (20%)
- Calidad y legibilidad del código (15%)
- Eficiencia de la solución (10%)
- Documentación y comentarios (5%)

---

## PARTE 1: EJERCICIOS

### Ejercicio 1: Expresiones Aritméticas y Validación (10 puntos)

Crea una función `calculadora_cientifica(operacion, a, b)` que:

**Requisitos:**
- Soporte las operaciones: "suma", "resta", "multiplicacion", "division", "potencia", "modulo"
- Valide que los parámetros sean numéricos (int o float)
- Lance `ValueError` con mensaje descriptivo si la operación es inválida
- Lance `ZeroDivisionError` con mensaje descriptivo si se intenta dividir por cero
- Retorne el resultado con precisión de 2 decimales

**Ejemplo:**
```python
calculadora_cientifica("division", 10, 3)  # Retorna: 3.33
calculadora_cientifica("potencia", 2, 8)   # Retorna: 256.0
calculadora_cientifica("division", 10, 0)  # Lanza ZeroDivisionError
calculadora_cientifica("raiz", 4, 2)       # Lanza ValueError
```

**Puntuación:**
- Implementación correcta de operaciones: 4 puntos
- Validación de tipos: 2 puntos
- Manejo de excepciones: 3 puntos
- Formato de resultado: 1 punto

---

### Ejercicio 2: Expresiones Relacionales y Lógicas (12 puntos)

Implementa una clase `ValidadorPassword` que valide contraseñas según reglas complejas.

**Requisitos:**
```python
class ValidadorPassword:
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
        # Inicializar parámetros de validación
        pass
    
    def validar(self, password):
        """
        Valida password según las reglas configuradas.
        
        Retorna: (bool, list) - (es_valido, lista_de_errores)
        
        Si es válido: (True, [])
        Si no es válido: (False, ['error1', 'error2', ...])
        """
        pass
    
    def es_fuerte(self, password):
        """
        Retorna True si el password tiene al menos 12 caracteres,
        contiene mayúsculas, minúsculas, números y caracteres especiales.
        """
        pass
```

**Casos de prueba requeridos:**
```python
validador = ValidadorPassword(min_longitud=8)
print(validador.validar("Abc123!"))         # (False, ['Longitud mínima no cumplida'])
print(validador.validar("Abc123!@"))        # (True, [])
print(validador.validar("abcdefgh"))        # (False, ['Falta mayúscula', ...])
print(validador.es_fuerte("Abc123!@#$Xyz")) # True
```

**Puntuación:**
- Implementación de validaciones: 6 puntos
- Uso correcto de expresiones lógicas/relacionales: 3 puntos
- Manejo de casos edge: 2 puntos
- Función es_fuerte: 1 punto

---

### Ejercicio 3: Estructuras de Datos (15 puntos)

Implementa un sistema de gestión de inventario usando diccionarios, listas y tuplas.

**Requisitos:**
```python
class GestorInventario:
    def __init__(self):
        """
        Inicializa el inventario como un diccionario:
        {
            'codigo_producto': {
                'nombre': str,
                'precio': float,
                'cantidad': int,
                'categoria': str
            }
        }
        """
        pass
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """Agrega producto. Lanza ValueError si código ya existe."""
        pass
    
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza stock (positivo=añade, negativo=reduce).
        Lanza ValueError si producto no existe.
        Lanza ValueError si stock resultante sería negativo.
        """
        pass
    
    def buscar_por_categoria(self, categoria):
        """Retorna lista de tuplas (codigo, nombre, precio) de la categoría."""
        pass
    
    def productos_bajo_stock(self, limite=10):
        """Retorna diccionario {codigo: cantidad} de productos bajo el límite."""
        pass
    
    def valor_total_inventario(self):
        """Retorna el valor total del inventario (precio * cantidad de todos)."""
        pass
    
    def top_productos(self, n=5):
        """
        Retorna lista de tuplas (codigo, valor_total) de los N productos
        con mayor valor en inventario, ordenados descendentemente.
        """
        pass
```

**Casos de prueba requeridos:**
```python
inv = GestorInventario()
inv.agregar_producto("P001", "Laptop", 1200.00, 15, "Electrónica")
inv.agregar_producto("P002", "Mouse", 25.50, 5, "Accesorios")
inv.agregar_producto("P003", "Teclado", 85.00, 8, "Accesorios")

inv.actualizar_stock("P001", -3)  # Reduce stock
print(inv.productos_bajo_stock(10))  # {'P002': 5, 'P003': 8}
print(inv.buscar_por_categoria("Accesorios"))  # [('P002', 'Mouse', 25.5), ...]
print(inv.valor_total_inventario())  # Suma total
print(inv.top_productos(2))  # Top 2 productos por valor
```

**Puntuación:**
- Estructura de datos correcta: 3 puntos
- Métodos agregar/actualizar: 4 puntos
- Métodos de búsqueda/filtrado: 4 puntos
- Cálculos y ordenamiento: 3 puntos
- Manejo de excepciones: 1 punto

---

### Ejercicio 4: Estructuras de Control (10 puntos)

Implementa una función que determine si un año es bisiesto y genere un calendario de un mes específico.

**Requisitos:**
```python
def es_bisiesto(anio):
    """
    Retorna True si el año es bisiesto.
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si es divisible por 100: no bisiesto
    - EXCEPTO si es divisible por 400: bisiesto
    """
    pass

def dias_en_mes(mes, anio):
    """
    Retorna el número de días en el mes (1-12).
    Considera años bisiestos para febrero.
    Lanza ValueError si mes es inválido.
    """
    pass

def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera una representación string del calendario del mes.
    dia_inicio: 0=Lunes, 1=Martes, ..., 6=Domingo
    
    Retorna string con formato:
    Lu Ma Mi Ju Vi Sa Do
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    ...
    """
    pass
```

**Casos de prueba:**
```python
print(es_bisiesto(2024))  # True
print(es_bisiesto(2100))  # False
print(es_bisiesto(2000))  # True
print(dias_en_mes(2, 2024))  # 29
print(dias_en_mes(2, 2023))  # 28
print(generar_calendario(1, 2024, 0))  # Calendario de enero 2024
```

**Puntuación:**
- Función es_bisiesto: 2 puntos
- Función dias_en_mes: 2 puntos
- Función generar_calendario: 5 puntos
- Validaciones: 1 punto

---

### Ejercicio 5: Estructuras de Repetición (13 puntos)

Implementa funciones de análisis de datos usando loops eficientemente.

**Requisitos:**
```python
def analizar_ventas(ventas):
    """
    Analiza lista de diccionarios de ventas.
    ventas = [
        {'producto': 'A', 'cantidad': 10, 'precio': 100, 'descuento': 0.1},
        {'producto': 'B', 'cantidad': 5, 'precio': 200, 'descuento': 0.0},
        ...
    ]
    
    Retorna diccionario con:
    {
        'total_ventas': float,  # Suma de (cantidad * precio * (1 - descuento))
        'promedio_por_venta': float,
        'producto_mas_vendido': str,  # Por cantidad
        'venta_mayor': dict,  # Diccionario de la venta individual más alta
        'total_descuentos': float  # Total ahorrado por descuentos
    }
    """
    pass

def encontrar_patrones(numeros):
    """
    Encuentra patrones en lista de números.
    
    Retorna diccionario con:
    {
        'secuencias_ascendentes': int,  # Cantidad de secuencias crecientes
        'secuencias_descendentes': int,  # Cantidad de secuencias decrecientes
        'longitud_max_ascendente': int,  # Longitud de la secuencia ascendente más larga
        'longitud_max_descendente': int,
        'numeros_repetidos': dict  # {numero: cantidad_repeticiones} solo para repetidos
    }
    """
    pass

def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    
    Retorna lista de diccionarios, uno por año:
    [
        {'anio': 1, 'balance': 1050.0, 'interes_ganado': 50.0},
        {'anio': 2, 'balance': 1102.5, 'interes_ganado': 52.5},
        ...
    ]
    """
    pass
```

**Casos de prueba:**
```python
ventas = [
    {'producto': 'Laptop', 'cantidad': 2, 'precio': 1000, 'descuento': 0.1},
    {'producto': 'Mouse', 'cantidad': 10, 'precio': 20, 'descuento': 0.0},
    {'producto': 'Laptop', 'cantidad': 3, 'precio': 1000, 'descuento': 0.15}
]
print(analizar_ventas(ventas))

numeros = [1, 2, 3, 2, 1, 2, 3, 4, 5, 3, 3, 3]
print(encontrar_patrones(numeros))

print(simular_crecimiento(1000, 0.05, 5, 100))
```

**Puntuación:**
- Función analizar_ventas: 5 puntos
- Función encontrar_patrones: 5 puntos
- Función simular_crecimiento: 2 puntos
- Eficiencia de loops: 1 punto

---

## PARTE 2: PROBLEMA INTEGRADOR

### Sistema de Gestión de Biblioteca Digital

Implementa un sistema completo de gestión de biblioteca digital que integre todos los conceptos vistos.

---

### Contexto

Una biblioteca necesita un sistema para gestionar su catálogo digital, préstamos, usuarios y estadísticas. El sistema debe ser robusto, manejar errores apropiadamente y proporcionar análisis de datos.

---

### Especificaciones Técnicas

#### 1. Excepciones Personalizadas (5 puntos)

Implementa una jerarquía de excepciones personalizadas para el sistema de biblioteca.

**Jerarquía requerida:**

1. **ErrorBiblioteca(Exception)** - Excepción base del sistema
   - Solo necesita `pass` en el cuerpo

2. **LibroNoEncontrado(ErrorBiblioteca)** - Cuando un libro no existe
   - Atributo: `isbn` (string)
   - Mensaje: `"Libro con ISBN {isbn} no encontrado"`

3. **LibroNoDisponible(ErrorBiblioteca)** - Cuando no hay copias disponibles
   - Atributos: `isbn` (string), `titulo` (string)
   - Mensaje: `"No hay copias disponibles de '{titulo}'"`

4. **UsuarioNoRegistrado(ErrorBiblioteca)** - Cuando el usuario no existe
   - Atributo: `id_usuario` (string)
   - Mensaje: `"Usuario con ID '{id_usuario}' no está registrado"`

5. **LimitePrestamosExcedido(ErrorBiblioteca)** - Cuando se excede el límite
   - Atributos: `id_usuario` (string), `limite` (int)
   - Mensaje: `"Usuario {id_usuario} excede límite de {limite} préstamos"`

6. **PrestamoVencido(ErrorBiblioteca)** - Para préstamos vencidos
   - Atributos: `id_prestamo` (string), `dias_retraso` (int)
   - Mensaje: `"Préstamo {id_prestamo} está vencido por {dias_retraso} días"`

**Ejemplo de implementación esperada:**

```python
class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass

class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")

# Implementa las 5 excepciones restantes siguiendo el mismo patrón...
```

**Requisitos:**
- Todas deben heredar de ErrorBiblioteca (excepto ErrorBiblioteca que hereda de Exception)
- Guardar los atributos especificados como atributos de instancia
- Usar `super().__init__(mensaje)` para pasar el mensaje a la clase base
- Usar f-strings para los mensajes descriptivos

---

#### 2. Clase Principal: SistemaBiblioteca (35 puntos)

```python
from datetime import datetime, timedelta

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
        pass
    
    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).
        
        Raises:
            LibroNoEncontrado: Si ISBN no existe
            ValueError: Si resultado sería negativo
        """
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
        pass
    
    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.
        
        Returns:
            dict con: nombre, prestamos_activos, puede_prestar, multas_pendientes
        
        Raises:
            UsuarioNoRegistrado: Si usuario no existe
        """
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
        pass
    
    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).
        
        Raises:
            PrestamoVencido: Si ya está vencido
            KeyError: Si préstamo no existe
        """
        pass
    
    # ============ ESTADÍSTICAS Y REPORTES ============
    
    def libros_mas_prestados(self, n=10):
        """
        Retorna los N libros más prestados.
        
        Returns:
            Lista de tuplas: [(isbn, titulo, cantidad_prestamos), ...]
            Ordenada descendentemente por cantidad
        """
        pass
    
    def usuarios_mas_activos(self, n=5):
        """
        Retorna los N usuarios más activos (más préstamos históricos).
        
        Returns:
            Lista de tuplas: [(id_usuario, nombre, total_prestamos), ...]
        """
        pass
    
    def estadisticas_categoria(self, categoria):
        """
        Genera estadísticas de una categoría.
        
        Returns:
            dict: {
                'total_libros': int,
                'total_copias': int,
                'copias_prestadas': int,
                'tasa_prestamo': float,  # % copias actualmente prestadas
                'libro_mas_popular': str  # título
            }
        """
        pass
    
    def prestamos_vencidos(self):
        """
        Lista préstamos actualmente vencidos.
        
        Returns:
            Lista de dicts con: id_prestamo, isbn, titulo, id_usuario,
            dias_retraso, multa_acumulada
        """
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
        pass
    
    # ============ UTILIDADES ============
    
    def exportar_catalogo(self, archivo='catalogo.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias
        
        Maneja excepciones de archivo apropiadamente.
        """
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
        pass
```

---

### Criterios de Evaluación Detallados

#### Excepciones Personalizadas (5 puntos)
- [ ] Jerarquía correcta de excepciones (2 puntos)
- [ ] Atributos y mensajes descriptivos (2 puntos)
- [ ] Uso correcto de `super().__init__` (1 punto)

#### Gestión de Catálogo (8 puntos)
- [ ] Validaciones completas en agregar_libro (2 puntos)
- [ ] Actualización correcta de copias (2 puntos)
- [ ] Búsqueda flexible y eficiente (4 puntos)

#### Gestión de Usuarios (5 puntos)
- [ ] Validación de email y datos (2 puntos)
- [ ] Estado completo del usuario (3 puntos)

#### Gestión de Préstamos (10 puntos)
- [ ] Validaciones completas en prestar_libro (3 puntos)
- [ ] Cálculo correcto de multas (3 puntos)
- [ ] Lógica de devolución y renovación (4 puntos)

#### Estadísticas y Reportes (8 puntos)
- [ ] Libros y usuarios más activos (2 puntos)
- [ ] Estadísticas por categoría (2 puntos)
- [ ] Préstamos vencidos con cálculos (2 puntos)
- [ ] Reporte financiero completo (2 puntos)

#### Importar/Exportar (4 puntos)
- [ ] Exportación correcta (1 punto)
- [ ] Importación con manejo de errores (3 puntos)

---

### Casos de Prueba Mínimos Requeridos

```python
# Crear instancia del sistema
biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)

# 1. Agregar libros al catálogo
biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
biblioteca.agregar_libro("9780135404676", "Python Crash Course", "Eric Matthes", 2019, "Programación", 3)
biblioteca.agregar_libro("9781449355739", "Fluent Python", "Luciano Ramalho", 2015, "Programación", 2)

# 2. Registrar usuarios
biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
biblioteca.registrar_usuario("U002", "Carlos López", "carlos@email.com")

# 3. Realizar préstamos
try:
    id_p1 = biblioteca.prestar_libro("9780134685991", "U001")
    id_p2 = biblioteca.prestar_libro("9780135404676", "U001")
    print(f"Préstamos realizados: {id_p1}, {id_p2}")
except ErrorBiblioteca as e:
    print(f"Error: {e}")

# 4. Buscar libros
resultados = biblioteca.buscar_libros(criterio='autor', valor='python')
print(f"Libros encontrados: {len(resultados)}")

# 5. Devolver con retraso (simular)
# Modifica fecha_vencimiento para simular retraso
resultado_dev = biblioteca.devolver_libro(id_p1)
print(f"Devolución: {resultado_dev}")

# 6. Estadísticas
print(biblioteca.libros_mas_prestados(3))
print(biblioteca.estadisticas_categoria("Programación"))
print(biblioteca.reporte_financiero())

# 7. Exportar catálogo
biblioteca.exportar_catalogo("catalogo_backup.txt")

# 8. Manejo de excepciones específicas
try:
    biblioteca.prestar_libro("9999999999999", "U001")  # ISBN no existe
except LibroNoEncontrado as e:
    print(f"Capturado correctamente: {e}")

try:
    for i in range(5):
        biblioteca.prestar_libro("9780134685991", "U002")  # Exceder límite
except LimitePrestamosExcedido as e:
    print(f"Límite controlado: {e}")
```

---

### Entregables

1. **Archivo Python:** `sistema_biblioteca.py` con toda la implementación
2. **Archivo de pruebas:** `test_biblioteca.py` con al menos 10 casos de prueba
3. **Archivo de datos:** `catalogo_inicial.txt` con al menos 10 libros para importar
4. **Documentación:** Comentarios en el código explicando lógica compleja

---

## 📝 Hoja de Respuestas

### Parte 1: Ejercicios

**Ejercicio 1:**
```python
# Tu código aquí
```

**Ejercicio 2:**
```python
# Tu código aquí
```

**Ejercicio 3:**
```python
# Tu código aquí
```

**Ejercicio 4:**
```python
# Tu código aquí
```

**Ejercicio 5:**
```python
# Tu código aquí
```

---

### Parte 2: Problema Integrador

```python
# sistema_biblioteca.py
# Tu implementación completa aquí
```

---

## ✅ Checklist Final

Antes de entregar, verifica:

- [ ] Todo el código está en español (comentarios, nombres de variables)
- [ ] Todas las funciones tienen docstrings
- [ ] El código compila sin errores de sintaxis
- [ ] Has probado todos los casos de prueba
- [ ] Las excepciones se manejan apropiadamente
- [ ] El código sigue buenas prácticas (nombres descriptivos, código limpio)
- [ ] Has incluido comentarios en lógica compleja
- [ ] Los cálculos matemáticos son correctos
- [ ] Las estructuras de datos son apropiadas para cada caso

---

## 📊 Tabla de Puntuación

| Sección | Puntos Máximos | Puntos Obtenidos |
|---------|----------------|------------------|
| Ejercicio 1: Expresiones Aritméticas | 10 | |
| Ejercicio 2: Expresiones Lógicas | 12 | |
| Ejercicio 3: Estructuras de Datos | 15 | |
| Ejercicio 4: Estructuras de Control | 10 | |
| Ejercicio 5: Estructuras de Repetición | 13 | |
| **Subtotal Parte 1** | **60** | |
| Problema Integrador: Sistema Biblioteca | 40 | |
| **Total** | **100** | |

---

**¡Buena suerte! 🎓**

---

**Tiempo de inicio:** __:__  
**Tiempo de finalización:** __:__  
**Tiempo total utilizado:** ______ horas ______ minutos
