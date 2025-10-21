import sys
from datetime import datetime

# ======================================================================
# PARTE 1: EXCEPCIONES PERSONALIZADAS
# ======================================================================

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
    def __init__(self, numero_mesa, hora_disponible="N/A"):
        self.numero_mesa = numero_mesa
        self.hora_disponible = hora_disponible
        super().__init__(f"Mesa {numero_mesa} no disponible. Disponible a las {hora_disponible}")

class CapacidadExcedida(ErrorRestaurante):
    """Se lanza cuando hay más comensales que capacidad."""
    def __init__(self, numero_mesa, capacidad, comensales):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.comensales = comensales
        super().__init__(f"Mesa {numero_mesa} tiene capacidad para {capacidad}, se solicitaron {comensales} lugares")

class PedidoInvalido(ErrorRestaurante):
    """Para pedidos con problemas (ej. no existe, ya pagado)."""
    def __init__(self, razon):
        self.razon = razon
        super().__init__(f"Pedido inválido: {razon}")

# ======================================================================
# PARTE 2: CLASE PRINCIPAL DEL SISTEMA
# ======================================================================

class SistemaRestaurante:
    """
    Sistema completo de gestión de restaurante.
    
    Estructuras de datos:
    - menu: {codigo: {'nombre', 'categoria', 'precio', 'disponible'}}
    - mesas: {numero: {'capacidad', 'ocupada', 'reservacion', 'pedido_actual'}}
    - pedidos: {id_pedido: {'mesa', 'items', 'subtotal', 'propina', 'impuesto', 'total', 'hora', 'pagado'}}
    - ventas_dia: lista de ids de pedidos completados
    """
    
    CATEGORIAS_VALIDAS = {"entrada", "plato_fuerte", "postre", "bebida"}

    def __init__(self, num_mesas=10, tasa_impuesto=0.16, propina_sugerida=0.15):
        """
        Inicializa el sistema.
        
        Args:
            num_mesas: Número total de mesas (1 a num_mesas)
            tasa_impuesto: Tasa de impuesto (IVA)
            propina_sugerida: Propina sugerida por defecto
        """
        self.num_mesas = num_mesas
        self.tasa_impuesto = tasa_impuesto
        self.propina_sugerida = propina_sugerida
        
        # Estructuras de datos principales
        self.menu = {}
        # Inicializa todas las mesas con capacidad 0 (requieren configuración)
        self.mesas = {
            i: {'capacidad': 0, 'ocupada': False, 'reservacion': None, 'pedido_actual': None}
            for i in range(1, num_mesas + 1)
        }
        self.pedidos = {}
        self.ventas_dia = []

    
    # ============ GESTIÓN DE MENÚ ============
    
    def agregar_plato(self, codigo, nombre, categoria, precio):
        """
        Agrega un plato al menú.
        
        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si código ya existe
        """
        if not codigo or not nombre:
            raise ValueError("Código y nombre no pueden estar vacíos")
        if codigo in self.menu:
            raise KeyError(f"Código de plato '{codigo}' ya existe")
        if categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoría '{categoria}' inválida. Válidas: {self.CATEGORIAS_VALIDAS}")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("Precio debe ser un número positivo")
            
        self.menu[codigo] = {
            'nombre': nombre,
            'categoria': categoria,
            'precio': float(precio),
            'disponible': True
        }
    
    def cambiar_disponibilidad(self, codigo, disponible):
        """
        Cambia disponibilidad de un plato.
        
        Raises:
            PlatoNoEncontrado: Si código no existe
        """
        if codigo not in self.menu:
            raise PlatoNoEncontrado(codigo)
        self.menu[codigo]['disponible'] = bool(disponible)
    
    def buscar_platos(self, categoria=None, precio_max=None):
        """
        Busca platos por criterios.
        
        Returns:
            Lista de diccionarios con info de platos disponibles
        """
        resultados = []
        for codigo, plato in self.menu.items():
            if not plato['disponible']:
                continue
            
            # Filtro por categoría
            if categoria and plato['categoria'] != categoria:
                continue
            
            # Filtro por precio
            if precio_max is not None and plato['precio'] > precio_max:
                continue
                
            # Agrega el código al diccionario de resultados
            info_plato = plato.copy()
            info_plato['codigo'] = codigo
            resultados.append(info_plato)
            
        return resultados
    
    # ============ GESTIÓN DE MESAS ============
    
    def configurar_mesa(self, numero, capacidad):
        """
        Configura capacidad de una mesa.
        
        Raises:
            ValueError: Si validaciones fallan
        """
        if numero not in self.mesas:
            raise ValueError(f"Mesa {numero} no existe. Rango válido: 1-{self.num_mesas}")
        if not (1 <= capacidad <= 12):
            raise ValueError("Capacidad debe estar entre 1 y 12")
            
        self.mesas[numero]['capacidad'] = capacidad
    
    def reservar_mesa(self, numero, comensales, hora):
        """
        Reserva una mesa.
        
        Raises:
            MesaNoDisponible: Si mesa ocupada
            CapacidadExcedida: Si comensales > capacidad
            ValueError: Si validaciones fallan
        """
        if numero not in self.mesas:
            raise ValueError(f"Mesa {numero} no existe")
            
        mesa = self.mesas[numero]
        
        if mesa['capacidad'] == 0:
            raise ValueError(f"Mesa {numero} no ha sido configurada. Use configurar_mesa()")
        if mesa['ocupada']:
            hora_res = mesa['reservacion']['hora'] if mesa['reservacion'] else "N/A"
            raise MesaNoDisponible(numero, hora_disponible=hora_res)
        if comensales > mesa['capacidad']:
            raise CapacidadExcedida(numero, mesa['capacidad'], comensales)
        
        # Validación simple de formato de hora
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            raise ValueError("Formato de hora inválido. Use 'HH:MM'")
            
        mesa['ocupada'] = True
        mesa['reservacion'] = {'comensales': comensales, 'hora': hora}
    
    def liberar_mesa(self, numero):
        """
        Libera una mesa (termina servicio).
        
        Raises:
            ValueError: Si mesa no existe o no está ocupada
        """
        if numero not in self.mesas:
            raise ValueError(f"Mesa {numero} no existe")
        if not self.mesas[numero]['ocupada']:
            raise ValueError(f"Mesa {numero} ya está libre")
            
        self.mesas[numero]['ocupada'] = False
        self.mesas[numero]['reservacion'] = None
        self.mesas[numero]['pedido_actual'] = None
    
    def mesas_disponibles(self, comensales):
        """
        Lista mesas disponibles para N comensales.
        
        Returns:
            Lista de números de mesa con capacidad suficiente
        """
        return [
            num for num, mesa in self.mesas.items()
            if not mesa['ocupada'] and mesa['capacidad'] >= comensales
        ]
    
    # ============ GESTIÓN DE PEDIDOS ============
    
    def crear_pedido(self, numero_mesa):
        """
        Crea un nuevo pedido para una mesa.
        
        Returns:
            id_pedido: ID único del pedido (formato: "PED" + timestamp)
        
        Raises:
            ValueError: Si validaciones fallan
        """
        if numero_mesa not in self.mesas:
            raise ValueError(f"Mesa {numero_mesa} no existe")
        
        mesa = self.mesas[numero_mesa]
        
        if not mesa['ocupada']:
            raise ValueError(f"Mesa {numero_mesa} debe estar ocupada (reservada) para crear pedido")
        if mesa['pedido_actual']:
            raise ValueError(f"Mesa {numero_mesa} ya tiene un pedido activo ({mesa['pedido_actual']})")
            
        # Generar ID único
        timestamp = int(datetime.now().timestamp() * 1000)
        id_pedido = f"PED{timestamp}"
        
        self.pedidos[id_pedido] = {
            'mesa': numero_mesa,
            'items': {}, # {codigo: {'nombre', 'precio_unitario', 'cantidad'}}
            'subtotal': 0.0,
            'propina': 0.0,
            'impuesto': 0.0,
            'total': 0.0,
            'hora': datetime.now().strftime("%H:%M:%S"),
            'pagado': False
        }
        
        mesa['pedido_actual'] = id_pedido
        return id_pedido
    
    def agregar_item(self, id_pedido, codigo_plato, cantidad=1):
        """
        Agrega items al pedido.
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
            PlatoNoEncontrado: Si plato no existe
            ValueError: Si plato no disponible o cantidad <= 0
        """
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        
        pedido = self.pedidos[id_pedido]
        
        if pedido['pagado']:
            raise PedidoInvalido("No se pueden agregar items a un pedido pagado")
        if codigo_plato not in self.menu:
            raise PlatoNoEncontrado(codigo_plato)
        
        plato = self.menu[codigo_plato]
        
        if not plato['disponible']:
            raise ValueError(f"Plato '{plato['nombre']}' no está disponible")
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("Cantidad debe ser un entero positivo")
            
        # Agregar o actualizar item en el pedido
        if codigo_plato in pedido['items']:
            pedido['items'][codigo_plato]['cantidad'] += cantidad
        else:
            pedido['items'][codigo_plato] = {
                'nombre': plato['nombre'],
                'precio_unitario': plato['precio'],
                'cantidad': cantidad
            }
    
    def calcular_total(self, id_pedido, propina_porcentaje=None):
        """
        Calcula total del pedido.
        
        Returns:
            dict: {'subtotal', 'impuesto', 'propina', 'total'}
        
        Raises:
            PedidoInvalido: Si pedido no existe
        """
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
            
        pedido = self.pedidos[id_pedido]
        
        # 1. Calcular Subtotal
        subtotal = 0.0
        for item in pedido['items'].values():
            subtotal += item['precio_unitario'] * item['cantidad']
            
        # 2. Calcular Impuesto
        impuesto = subtotal * self.tasa_impuesto
        
        # 3. Calcular Propina
        if propina_porcentaje is None:
            propina_porcentaje = self.propina_sugerida
        
        propina = subtotal * propina_porcentaje
        
        # 4. Calcular Total
        total = subtotal + impuesto + propina
        
        return {
            'subtotal': subtotal,
            'impuesto': impuesto,
            'propina': propina,
            'total': total
        }
    
    def pagar_pedido(self, id_pedido, propina_porcentaje=None):
        """
        Procesa pago del pedido.
        
        Returns:
            dict con totales (mismo que calcular_total)
        
        Raises:
            PedidoInvalido: Si pedido no existe o ya pagado
        """
        if id_pedido not in self.pedidos:
            raise PedidoInvalido("Pedido no existe")
        
        pedido = self.pedidos[id_pedido]
        
        if pedido['pagado']:
            raise PedidoInvalido("Pedido ya fue pagado")
            
        # Calcular totales finales
        totales = self.calcular_total(id_pedido, propina_porcentaje)
        
        # Actualizar el pedido con los montos
        pedido.update(totales)
        pedido['pagado'] = True
        
        # Registrar en ventas del día
        self.ventas_dia.append(id_pedido)
        
        return totales
    
    # ============ REPORTES Y ESTADÍSTICAS ============
    
    def platos_mas_vendidos(self, n=5):
        """
        Retorna los N platos más vendidos del día.
        
        Returns:
            Lista de tuplas: [(codigo, nombre, cantidad_vendida), ...]
        """
        conteo_platos = {}
        for id_pedido in self.ventas_dia:
            pedido = self.pedidos[id_pedido]
            for codigo, item in pedido['items'].items():
                conteo_platos[codigo] = conteo_platos.get(codigo, 0) + item['cantidad']
                
        # Ordenar por cantidad (valor del dict)
        platos_ordenados = sorted(conteo_platos.items(), key=lambda item: item[1], reverse=True)
        
        # Formatear salida
        resultado = []
        for codigo, cantidad in platos_ordenados[:n]:
            nombre = self.menu.get(codigo, {}).get('nombre', 'DESCONOCIDO')
            resultado.append((codigo, nombre, cantidad))
            
        return resultado
    
    def ventas_por_categoria(self):
        """
        Calcula ventas totales por categoría (basado en subtotal).
        
        Returns:
            dict: {categoria: total_ventas}
        """
        ventas = {cat: 0.0 for cat in self.CATEGORIAS_VALIDAS}
        
        for id_pedido in self.ventas_dia:
            pedido = self.pedidos[id_pedido]
            for codigo, item in pedido['items'].items():
                if codigo in self.menu:
                    categoria = self.menu[codigo]['categoria']
                    monto = item['precio_unitario'] * item['cantidad']
                    if categoria in ventas:
                        ventas[categoria] += monto
                        
        return ventas
    
    def reporte_ventas_dia(self):
        """
        Genera reporte completo de ventas del día.
        
        Returns:
            dict con métricas clave
        """
        total_pedidos = len(self.ventas_dia)
        
        if total_pedidos == 0:
            return {
                'total_pedidos': 0,
                'subtotal_ventas': 0.0,
                'total_impuestos': 0.0,
                'total_propinas': 0.0,
                'total_ingresos': 0.0,
                'ticket_promedio': 0.0,
                'plato_mas_vendido': "N/A"
            }
            
        subtotal_ventas = sum(self.pedidos[idp]['subtotal'] for idp in self.ventas_dia)
        total_impuestos = sum(self.pedidos[idp]['impuesto'] for idp in self.ventas_dia)
        total_propinas = sum(self.pedidos[idp]['propina'] for idp in self.ventas_dia)
        total_ingresos = sum(self.pedidos[idp]['total'] for idp in self.ventas_dia)
        
        ticket_promedio = total_ingresos / total_pedidos
        
        top_plato_list = self.platos_mas_vendidos(1)
        plato_mas_vendido = top_plato_list[0][1] if top_plato_list else "N/A"
        
        return {
            'total_pedidos': total_pedidos,
            'subtotal_ventas': subtotal_ventas,
            'total_impuestos': total_impuestos,
            'total_propinas': total_propinas,
            'total_ingresos': total_ingresos,
            'ticket_promedio': ticket_promedio,
            'plato_mas_vendido': plato_mas_vendido
        }
    
    def estado_restaurante(self):
        """
        Estado actual del restaurante.
        
        Returns:
            dict con estado de mesas y pedidos
        """
        mesas_ocupadas = sum(1 for m in self.mesas.values() if m['ocupada'])
        mesas_disponibles = self.num_mesas - mesas_ocupadas
        
        # Pedidos activos son los que existen pero no están pagados
        pedidos_activos = sum(1 for p in self.pedidos.values() if not p['pagado'])
        
        pedidos_completados_hoy = len(self.ventas_dia)
        
        return {
            'mesas_ocupadas': mesas_ocupadas,
            'mesas_disponibles': mesas_disponibles,
            'pedidos_activos': pedidos_activos,
            'pedidos_completados_hoy': pedidos_completados_hoy
        }
    
    # ============ UTILIDADES ============
    
    def exportar_menu(self, archivo='menu.txt'):
        """
        Exporta menú a archivo de texto.
        Formato: Codigo|Nombre|Categoria|Precio|Disponible
        """
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for codigo, plato in self.menu.items():
                    linea = (
                        f"{codigo}|{plato['nombre']}|{plato['categoria']}|"
                        f"{plato['precio']}|{plato['disponible']}\n"
                    )
                    f.write(linea)
            print(f"Menú exportado exitosamente a '{archivo}'")
        except IOError as e:
            print(f"Error al exportar menú: {e}", file=sys.stderr)
    
    def importar_menu(self, archivo='menu.txt'):
        """
        Importa menú desde archivo de texto.
        
        Returns:
            dict: {'exitosos': int, 'errores': [(linea, error), ...]}
        """
        exitosos = 0
        errores = []
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                for i, linea in enumerate(f):
                    linea_num = i + 1
                    linea = linea.strip()
                    if not linea:
                        continue
                        
                    try:
                        partes = linea.split('|')
                        if len(partes) != 5:
                            raise ValueError(f"Formato incorrecto: se esperaban 5 campos, se obtuvieron {len(partes)}")
                        
                        codigo, nombre, categoria, precio_str, disponible_str = partes
                        
                        # Validación y conversión de tipos
                        precio = float(precio_str)
                        disponible = disponible_str.lower() == 'true'
                        
                        # Usar el método existente para agregar y validar
                        self.agregar_plato(codigo, nombre, categoria, precio)
                        # Establecer la disponibilidad leída del archivo
                        self.cambiar_disponibilidad(codigo, disponible)
                        
                        exitosos += 1
                        
                    except (ValueError, KeyError, IndexError) as e:
                        errores.append((linea_num, str(e)))
                        
        except FileNotFoundError:
            errores.append((0, f"Archivo '{archivo}' no encontrado"))
            
        return {'exitosos': exitosos, 'errores': errores}


# ======================================================================
# PARTE 3: CASOS DE PRUEBA MÍNIMOS
# ======================================================================

if __name__ == "__main__":
    print("--- INICIANDO SISTEMA DE RESTAURANTE ---")
    
    # Crear sistema
    restaurante = SistemaRestaurante(num_mesas=5, tasa_impuesto=0.16, propina_sugerida=0.15)

    # Configurar mesas
    print("\n--- Configurando Mesas ---")
    restaurante.configurar_mesa(1, 4)
    restaurante.configurar_mesa(2, 2)
    restaurante.configurar_mesa(3, 6)
    print("Mesas 1 (4), 2 (2), 3 (6) configuradas.")

    # Agregar platos al menú
    print("\n--- Agregando Platos ---")
    restaurante.agregar_plato("E001", "Ensalada César", "entrada", 85.00)
    restaurante.agregar_plato("P001", "Filete de Res", "plato_fuerte", 350.00)
    restaurante.agregar_plato("P002", "Pasta Alfredo", "plato_fuerte", 180.00)
    restaurante.agregar_plato("D001", "Tiramisú", "postre", 95.00)
    restaurante.agregar_plato("B001", "Limonada", "bebida", 45.00)
    print("5 platos agregados al menú.")

    # Reservar mesa
    print("\n--- Flujo Pedido Mesa 1 ---")
    restaurante.reservar_mesa(1, 3, "14:30")
    print("Mesa 1 reservada para 3 personas a las 14:30.")

    # Crear pedido
    id_pedido = restaurante.crear_pedido(1)
    print(f"Pedido {id_pedido} creado para Mesa 1.")
    
    # Agregar items
    restaurante.agregar_item(id_pedido, "E001", 2) # 85 * 2 = 170
    restaurante.agregar_item(id_pedido, "P001", 2) # 350 * 2 = 700
    restaurante.agregar_item(id_pedido, "B001", 3) # 45 * 3 = 135
    print("Items agregados: 2x Ensalada, 2x Filete, 3x Limonada.")
    # Subtotal = 170 + 700 + 135 = 1005

    # Calcular y pagar
    totales = restaurante.calcular_total(id_pedido, propina_porcentaje=0.18)
    print(f"Cálculo Total (18% propina): ${totales['total']:.2f} (Sub: ${totales['subtotal']:.2f}, Imp: ${totales['impuesto']:.2f}, Prop: ${totales['propina']:.2f})")

    resultado_pago = restaurante.pagar_pedido(id_pedido, propina_porcentaje=0.18)
    print(f"Pago procesado. Monto: ${resultado_pago['total']:.2f}")

    # Liberar mesa
    restaurante.liberar_mesa(1)
    print("Mesa 1 liberada.")

    # Reportes
    print("\n--- Reportes del Día ---")
    print(f"Platos más vendidos: {restaurante.platos_mas_vendidos(3)}")
    print(f"Ventas por categoría: {restaurante.ventas_por_categoria()}")
    print(f"Reporte general: {restaurante.reporte_ventas_dia()}")
    print(f"Estado actual: {restaurante.estado_restaurante()}")

    # Exportar menú
    restaurante.exportar_menu("menu_backup.txt")

    # Manejo de excepciones
    print("\n--- Pruebas de Excepciones ---")
    try:
        # Intentar agregar item a pedido pagado
        restaurante.agregar_item(id_pedido, "D001", 1) 
    except PedidoInvalido as e:
        print(f"Error (OK): {e}")

    try:
        restaurante.reservar_mesa(3, 10, "18:00")  # Excede capacidad
    except CapacidadExcedida as e:
        print(f"Error (OK): {e}")
        
    try:
        restaurante.reservar_mesa(1, 2, "19:00") # Mesa libre, reserva OK
        id_pedido_2 = restaurante.crear_pedido(1)
        restaurante.agregar_item(id_pedido_2, "X999", 1)  # Plato no existe
    except PlatoNoEncontrado as e:
        print(f"Error (OK): {e}")
    
    print("\n--- Prueba de Importación ---")
    # Crear un archivo de prueba para importar
    with open("menu_importar.txt", "w", encoding='utf-8') as f:
        f.write("I001|Quesadillas|entrada|90.0|True\n")
        f.write("I002|Tacos al Pastor|plato_fuerte|120.0|True\n")
        f.write("I003|Flan|postre|60.0\n") # Línea con error (faltan campos)
    
    reporte_imp = restaurante.importar_menu("menu_importar.txt")
    print(f"Importación completada: {reporte_imp}")
    print("Platos importados:")
    print(restaurante.buscar_platos(precio_max=100))