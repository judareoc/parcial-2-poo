# Problema Integrador de Práctica

## Sistema de Gestión de Restaurante

**Tiempo sugerido:** 1 hora

---

## Contexto

Un restaurante necesita un sistema para gestionar su menú, mesas, pedidos y facturación. El sistema debe manejar reservaciones, calcular totales con propinas e impuestos, y generar reportes de ventas.

---

## Excepciones Personalizadas (5 puntos)

Implementa la siguiente jerarquía de excepciones:

1. **ErrorRestaurante(Exception)** - Excepción base
   - Solo necesita `pass`

2. **PlatoNoEncontrado(ErrorRestaurante)** - Cuando un plato no existe
   - Atributo: `codigo_plato` (string)
   - Mensaje: `f"Plato con código '{codigo_plato}' no encontrado en el menú"`

3. **MesaNoDisponible(ErrorRestaurante)** - Cuando la mesa está ocupada
   - Atributos: `numero_mesa` (int), `hora_disponible` (string)
   - Mensaje: `f"Mesa {numero_mesa} no disponible. Disponible a las {hora_disponible}"`

4. **CapacidadExcedida(ErrorRestaurante)** - Cuando hay más comensales que capacidad
   - Atributos: `numero_mesa` (int), `capacidad` (int), `comensales` (int)
   - Mensaje: `f"Mesa {numero_mesa} tiene capacidad para {capacidad}, se solicitaron {comensales} lugares"`

5. **PedidoInvalido(ErrorRestaurante)** - Para pedidos con problemas
   - Atributo: `razon` (string)
   - Mensaje: `f"Pedido inválido: {razon}"`

**Ejemplo de implementación:**
```python
class ErrorRestaurante(Exception):
    """Excepción base para el sistema de restaurante."""
    pass

class PlatoNoEncontrado(ErrorRestaurante):
    """Se lanza cuando un plato no existe en el menú."""
    def __init__(self, codigo_plato):
        self.codigo_plato = codigo_plato
        super().__init__(f"Plato con código '{codigo_plato}' no encontrado en el menú")

# Implementa las 4 excepciones restantes...
```

---

## Clase Principal: SistemaRestaurante (35 puntos)

```python
from datetime import datetime, time

class SistemaRestaurante:
    """
    Sistema completo de gestión de restaurante.
    
    Estructuras de datos:
    - menu: {codigo: {'nombre', 'categoria', 'precio', 'disponible'}}
    - mesas: {numero: {'capacidad', 'ocupada', 'reservacion', 'pedido_actual'}}
    - pedidos: {id_pedido: {'mesa', 'items', 'subtotal', 'propina', 'impuesto', 'total', 'hora', 'pagado'}}
    - ventas_dia: lista de ids de pedidos completados
    """
    
    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        """
        Inicializa el sistema.
        
        Args:
            num_mesas: Número total de mesas (1 a num_mesas)
            tasa_impuesto: Tasa de impuesto (IVA)
            propina_sugerida: Propina sugerida por defecto
        """
        pass
    
    # ============ GESTIÓN DE MENÚ ============
    
    def agregar_plato(self, codigo, nombre, categoria, precio):
        """
        Agrega un plato al menú.
        
        Validaciones:
        - Código no vacío y único
        - Nombre no vacío
        - Categoría: "entrada", "plato_fuerte", "postre", "bebida"
        - Precio > 0
        
        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si código ya existe
        """
        pass
    
    def cambiar_disponibilidad(self, codigo, disponible):
        """
        Cambia disponibilidad de un plato.
        
        Raises:
            PlatoNoEncontrado: Si código no existe
        """
        pass
    
    def buscar_platos(self, categoria=None, precio_max=None):
        """
        Busca platos por criterios.
        
        Args:
            categoria: Filtrar por categoría (opcional)
            precio_max: Precio máximo (opcional)
        
        Returns:
            Lista de diccionarios con info de platos disponibles
        """
        pass
    
    # ============ GESTIÓN DE MESAS ============
    
    def configurar_mesa(self, numero, capacidad):
        """
        Configura capacidad de una mesa.
        
        Validaciones:
        - Número entre 1 y num_mesas
        - Capacidad entre 1 y 12
        
        Raises:
            ValueError: Si validaciones fallan
        """
        pass
    
    def reservar_mesa(self, numero, comensales, hora):
        """
        Reserva una mesa.
        
        Validaciones:
        - Mesa existe y no está ocupada
        - Comensales no excede capacidad
        - Hora en formato "HH:MM"
        
        Raises:
            MesaNoDisponible: Si mesa ocupada
            CapacidadExcedida: Si comensales > capacidad
            ValueError: Si validaciones fallan
        """
        pass
    
    def liberar_mesa(self, numero):
        """
        Libera una mesa (termina servicio).
        
        Raises:
            ValueError: Si mesa no existe o no está ocupada
        """
        pass
    
    def mesas_disponibles(self, comensales):
        """
        Lista mesas disponibles para N comensales.
        
        Returns:
            Lista de números de mesa con capacidad suficiente
        """
        pass
    
    # ============ GESTIÓN DE PEDIDOS ============
    
    def crear_pedido(self, numero_mesa):
        """
        Crea un nuevo pedido para una mesa.
        
        Validaciones:
        - Mesa existe y está ocupada
        - Mesa no tiene pedido activo
        
        Returns:
            id_pedido: ID único del pedido (formato: "PED" + timestamp)
        
        Raises:
            ValueError: Si validaciones fallan
        """
        pass
    
    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        """
        Agrega items al pedido.
        
        Validaciones:
        - Pedido existe y no está pagado
        - Plato existe y está disponible
        - Cantidad > 0
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
            PlatoNoEncontrado: Si plato no existe
            ValueError: Si plato no disponible
        """
        pass
    
    def calcular_total(self, id_pedido, propina_porcentaje=None):
        """
        Calcula total del pedido.
        
        Args:
            propina_porcentaje: Porcentaje de propina (usa sugerida si None)
        
        Returns:
            dict: {
                'subtotal': float,
                'impuesto': float,
                'propina': float,
                'total': float
            }
        
        Fórmula:
        - subtotal = suma de (precio * cantidad) de todos los items
        - impuesto = subtotal * tasa_impuesto
        - propina = subtotal * propina_porcentaje
        - total = subtotal + impuesto + propina
        """
        pass
    
    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        """
        Procesa pago del pedido.
        
        Actualiza pedido con totales y marca como pagado.
        Agrega a ventas del día.
        
        Returns:
            dict con totales (mismo que calcular_total)
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
        """
        pass
    
    # ============ REPORTES Y ESTADÍSTICAS ============
    
    def platos_mas_vendidos(self, n=5):
        """
        Retorna los N platos más vendidos del día.
        
        Returns:
            Lista de tuplas: [(codigo, nombre, cantidad_vendida), ...]
            Ordenada descendentemente por cantidad
        """
        pass
    
    def ventas_por_categoria(self):
        """
        Calcula ventas totales por categoría.
        
        Returns:
            dict: {
                'entrada': float,
                'plato_fuerte': float,
                'postre': float,
                'bebida': float
            }
        """
        pass
    
    def reporte_ventas_dia(self):
        """
        Genera reporte completo de ventas del día.
        
        Returns:
            dict: {
                'total_pedidos': int,
                'subtotal_ventas': float,
                'total_impuestos': float,
                'total_propinas': float,
                'total_ingresos': float,
                'ticket_promedio': float,
                'plato_mas_vendido': str
            }
        """
        pass
    
    def estado_restaurante(self):
        """
        Estado actual del restaurante.
        
        Returns:
            dict: {
                'mesas_ocupadas': int,
                'mesas_disponibles': int,
                'pedidos_activos': int,
                'pedidos_completados_hoy': int
            }
        """
        pass
    
    # ============ UTILIDADES ============
    
    def exportar_menu(self, archivo='menu.txt'):
        """
        Exporta menú a archivo de texto.
        Formato: Codigo|Nombre|Categoria|Precio|Disponible
        """
        pass
    
    def importar_menu(self, archivo='menu.txt'):
        """
        Importa menú desde archivo de texto.
        
        Returns:
            dict: {'exitosos': int, 'errores': [(linea, error), ...]}
        """
        pass
```

---

## Casos de Prueba Mínimos

```python
# Crear sistema
restaurante = SistemaRestaurante(num_mesas=5, tasa_impuesto=0.16, propina_sugerida=0.15)

# Configurar mesas
restaurante.configurar_mesa(1, 4)
restaurante.configurar_mesa(2, 2)
restaurante.configurar_mesa(3, 6)

# Agregar platos al menú
restaurante.agregar_plato("E001", "Ensalada César", "entrada", 85.00)
restaurante.agregar_plato("P001", "Filete de Res", "plato_fuerte", 350.00)
restaurante.agregar_plato("P002", "Pasta Alfredo", "plato_fuerte", 180.00)
restaurante.agregar_plato("D001", "Tiramisú", "postre", 95.00)
restaurante.agregar_plato("B001", "Limonada", "bebida", 45.00)

# Reservar mesa
restaurante.reservar_mesa(1, 3, "14:30")

# Crear pedido
id_pedido = restaurante.crear_pedido(1)
restaurante.agregar_item(id_pedido, "E001", 2)
restaurante.agregar_item(id_pedido, "P001", 2)
restaurante.agregar_item(id_pedido, "B001", 3)

# Calcular y pagar
totales = restaurante.calcular_total(id_pedido, propina_porcentaje=0.18)
print(f"Total a pagar: ${totales['total']:.2f}")

resultado_pago = restaurante.pagar_pedido(id_pedido, propina_porcentaje=0.18)
print(f"Pago procesado: {resultado_pago}")

# Liberar mesa
restaurante.liberar_mesa(1)

# Reportes
print(restaurante.platos_mas_vendidos(3))
print(restaurante.ventas_por_categoria())
print(restaurante.reporte_ventas_dia())
print(restaurante.estado_restaurante())

# Exportar menú
restaurante.exportar_menu("menu_backup.txt")

# Manejo de excepciones
try:
    restaurante.agregar_item(id_pedido, "X999", 1)  # Plato no existe
except PlatoNoEncontrado as e:
    print(f"Error: {e}")

try:
    restaurante.reservar_mesa(1, 10, "18:00")  # Excede capacidad
except CapacidadExcedida as e:
    print(f"Error: {e}")
```

---

## Criterios de Evaluación

### Excepciones Personalizadas (5 puntos)
- [ ] Jerarquía correcta (2 puntos)
- [ ] Atributos y mensajes (2 puntos)
- [ ] Uso de super().__init__ (1 punto)

### Gestión de Menú (6 puntos)
- [ ] Agregar platos con validaciones (2 puntos)
- [ ] Cambiar disponibilidad (1 punto)
- [ ] Búsqueda con filtros (3 puntos)

### Gestión de Mesas (7 puntos)
- [ ] Configurar y validar mesas (2 puntos)
- [ ] Reservar con validaciones (3 puntos)
- [ ] Liberar y listar disponibles (2 puntos)

### Gestión de Pedidos (10 puntos)
- [ ] Crear pedido (2 puntos)
- [ ] Agregar items con validaciones (3 puntos)
- [ ] Calcular totales correctamente (3 puntos)
- [ ] Procesar pago (2 puntos)

### Reportes y Estadísticas (8 puntos)
- [ ] Platos más vendidos (2 puntos)
- [ ] Ventas por categoría (2 puntos)
- [ ] Reporte completo del día (3 puntos)
- [ ] Estado del restaurante (1 punto)

### Importar/Exportar (4 puntos)
- [ ] Exportar menú (1 punto)
- [ ] Importar con manejo de errores (3 puntos)

---

## Entregables

1. **Archivo Python:** `sistema_restaurante.py` con toda la implementación
2. **Archivo de pruebas:** `test_restaurante.py` con al menos 8 casos de prueba
3. **Archivo de datos:** `menu_inicial.txt` con al menos 15 platos
4. **Documentación:** Comentarios explicando lógica compleja

---

## Datos de Ejemplo para menu_inicial.txt

```
E001|Ensalada César|entrada|85.00|True
E002|Sopa de Tortilla|entrada|65.00|True
E003|Guacamole con Totopos|entrada|75.00|True
P001|Filete de Res|plato_fuerte|350.00|True
P002|Pasta Alfredo|plato_fuerte|180.00|True
P003|Salmón a la Parrilla|plato_fuerte|320.00|True
P004|Tacos de Pescado|plato_fuerte|145.00|True
P005|Pizza Margarita|plato_fuerte|195.00|True
D001|Tiramisú|postre|95.00|True
D002|Cheesecake|postre|85.00|True
D003|Helado|postre|55.00|True
B001|Limonada|bebida|45.00|True
B002|Agua Mineral|bebida|35.00|True
B003|Café Americano|bebida|40.00|True
B004|Jugo Natural|bebida|50.00|True
```

---

## 💡 Consejos

1. **Estructura de datos:** Diseña bien tus diccionarios desde el inicio
2. **Validaciones:** No olvides validar TODOS los inputs
3. **Excepciones:** Usa las excepciones personalizadas apropiadamente
4. **Cálculos:** Verifica las fórmulas de impuestos y propinas
5. **IDs únicos:** Usa timestamps o contadores para IDs de pedidos
6. **Testing:** Prueba casos normales y casos edge

---

**¡Buena práctica! 🍽️**
