# Aclaraciones del Parcial - Leer Antes de Comenzar

**IMPORTANTE:** Este documento resuelve ambigüedades en el enunciado. Léelo completamente antes de empezar el examen.

---

## PARTE 1: EJERCICIOS

### Ejercicio 1: Calculadora Científica

**Mensajes de error requeridos:**
- Operación inválida: `"Operación inválida: '{operacion}'. Operaciones válidas: suma, resta, multiplicacion, division, potencia, modulo"`
- Tipos inválidos: `"Los parámetros deben ser numéricos (int o float)"`
- División por cero: `"No se puede realizar {operacion} por cero"`

**Validaciones:**
- Rechazar None, strings, listas, etc. con ValueError
- Solo aceptar int o float

---

### Ejercicio 2: ValidadorPassword

**Caracteres especiales definidos:**
```
!@#$%^&*()_+-=[]{}|;:,.<>?/
```
Cualquiera de estos caracteres cuenta como especial.

**Mensajes de error sugeridos:**
- `"Longitud mínima no cumplida (mínimo X caracteres)"`
- `"Falta al menos una letra mayúscula"`
- `"Falta al menos una letra minúscula"`  
- `"Falta al menos un número"`
- `"Falta al menos un carácter especial"`

**Nota:** Los mensajes exactos no afectan la puntuación siempre que sean descriptivos.

---

### Ejercicio 3: GestorInventario

**Interpretación de "bajo el límite":**
- `productos_bajo_stock(limite=10)` retorna productos con `cantidad < 10`
- NO incluye productos con cantidad exactamente igual al límite

**Ejemplo:**
```python
# Stock: P001=5, P002=10, P003=15
productos_bajo_stock(10)  # Retorna: {'P001': 5}
```

**Orden en empates (top_productos):**
- Orden descendente por valor
- En caso de empate, mantener orden de aparición

---

### Ejercicio 4: Calendario

**Formato de generar_calendario:**
```
Lu Ma Mi Ju Vi Sa Do
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
```
- Días con 2 caracteres de ancho (espacio adelante si es 1 dígito)
- Un espacio entre días
- Sin espacios al final de cada línea

**Validación de dia_inicio:**
- Si está fuera del rango 0-6, usar comportamiento por defecto (no lanzar error)
- Puedes aplicar módulo 7 si prefieres

---

### Ejercicio 5: Análisis de Datos

**Definición de "venta individual más alta":**
- Es la venta con el **valor total más alto**
- Fórmula: `cantidad * precio * (1 - descuento)`
- Retornar el diccionario completo de esa venta

**Definición de "secuencia":**
- Serie de **al menos 2 números consecutivos** que cumplen la condición
- Ejemplo: `[1, 2, 3]` tiene 1 secuencia ascendente de longitud 3
- Ejemplo: `[1, 2, 1, 3, 4]` tiene 2 secuencias ascendentes ([1,2] y [1,3,4])

**Aporte anual en simular_crecimiento:**
- El aporte se añade **al inicio de cada año**
- Luego se calcula el interés sobre (balance + aporte)
- Ejemplo año 1: balance = (1000 + 100) * 1.05 = 1155

**Números repetidos:**
- Solo incluir números que aparezcan **más de una vez**
- Ejemplo: `[1, 2, 2, 3]` → `{2: 2}` (el 1 y 3 no se incluyen)

---

## PARTE 2: PROBLEMA INTEGRADOR

### Excepciones Personalizadas

**Implementación requerida:**
- Debes implementar las **6 excepciones personalizadas** especificadas en el enunciado
- Sigue la estructura del ejemplo mostrado (ErrorBiblioteca y LibroNoEncontrado)
- Cada excepción debe tener los atributos especificados
- Usa los mensajes exactos indicados (con f-strings)

**Mensajes requeridos:**
- LibroNoEncontrado: `f"Libro con ISBN {isbn} no encontrado"`
- LibroNoDisponible: `f"No hay copias disponibles de '{titulo}'"`
- UsuarioNoRegistrado: `f"Usuario con ID '{id_usuario}' no está registrado"`
- LimitePrestamosExcedido: `f"Usuario {id_usuario} excede límite de {limite} préstamos"`
- PrestamoVencido: `f"Préstamo {id_prestamo} está vencido por {dias_retraso} días"`

**Nota:** Las excepciones que solo necesitan `pass` (ErrorBiblioteca) pueden no tener `__init__`.

---

### Formato de ID de Préstamo

**Formato requerido:**
```
"P" + número secuencial de 6 dígitos
Ejemplos: "P000001", "P000002", "P000123"
```

Puedes usar un contador interno que se incrementa con cada préstamo.

---

### Sistema de Multas

**Funcionamiento:**
1. Al devolver con retraso, la multa se calcula: `dias_retraso * multa_por_dia`
2. La multa calculada se añade a `usuario['multas_pendientes']`
3. El método `devolver_libro` retorna la multa pero NO la cobra (solo la registra)

**Para reporte_financiero:**
- `'multas_pagadas'`: Suma de multas de préstamos devueltos (asume que fueron pagadas)
- `'multas_pendientes'`: Suma de `usuario['multas_pendientes']` de todos los usuarios
- `'total_multas'`: Suma de todas las multas generadas (pagadas + pendientes)

---

### Campos en buscar_libros

**Retorna lista de diccionarios con estos campos:**
```python
{
    'isbn': str,
    'titulo': str,
    'autor': str,
    'anio': int,
    'categoria': str,
    'copias_disponibles': int
}
```

---

### Tasa de Préstamo

**Fórmula:**
```python
tasa_prestamo = (copias_prestadas / total_copias) * 100
```
Donde `copias_prestadas = total_copias - copias_disponibles`

---

### Importar Catálogo

**Manejo de duplicados:**
- Los libros con ISBN duplicado se **saltan** (no se sobrescriben)
- Se registran en la lista de errores con el mensaje: `"ISBN {isbn} ya existe (saltado)"`

---

### Estructura de prestamos_activos

```python
usuarios[id_usuario]['prestamos_activos'] = ["P000001", "P000002", ...]
```
Es una **lista de strings** (IDs de préstamos), no objetos completos.

---

## 🎯 SUPUESTOS GENERALES PERMITIDOS

Si encuentras alguna ambigüedad no cubierta aquí:

1. **Toma la interpretación más lógica y simple**
2. **Documéntala en un comentario** en tu código
3. **Sé consistente** con tu interpretación a lo largo del código

**Ejemplo:**
```python
# Supuesto: Si email no tiene '.' después del '@', lo considero inválido
if '@' not in email or '.' not in email.split('@')[1]:
    raise ValueError("Email inválido")
```

---

## ⚠️ IMPORTANTE

- Estas aclaraciones son **parte oficial del enunciado**
- Seguir estas especificaciones es **requerido** para obtener puntos completos
- Si algo sigue sin estar claro, usa tu mejor criterio y documéntalo

---

## ✅ CHECKLIST ANTES DE COMENZAR

- [o] Leí todas las aclaraciones
- [o] Entiendo los formatos requeridos
- [o] Sé qué hacer con casos ambiguos
- [o] Tengo claro el sistema de multas
- [o] Entiendo qué es una "secuencia"

---

**¡Ahora sí, buena suerte con el examen! 🎓**
