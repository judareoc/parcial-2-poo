#!/usr/bin/env python3
"""
PARCIAL 2 - EJERCICIOS (Parte 1)
Estudiante: _______________________________
Fecha: ____________________________________
"""

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS (10 puntos)
# ===========================================================================

def calculadora_cientifica(operacion, a, b):

    try:
        # Validar que los operandos sean numéricos
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Los parámetros 'a' y 'b' deben ser numéricos (int o float).")

        # Validar operación
        if operacion not in ["suma", "resta", "multiplicacion", "division", "potencia", "modulo"]:
            raise ValueError(f"Operación inválida: '{operacion}'. Operaciones válidas: suma, resta, multiplicacion, division, potencia, modulo.")

        # Realizar operación según el tipo
        if operacion == "suma":
            resultado = a + b
        elif operacion == "resta":
            resultado = a - b
        elif operacion == "multiplicacion":
            resultado = a * b
        elif operacion == "division":
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = a / b
        elif operacion == "potencia":
            resultado = a ** b
        elif operacion == "modulo":
            if b == 0:
                raise ZeroDivisionError("No se puede calcular el módulo con divisor cero.")
            resultado = a % b

        # Retornar resultado redondeado a 2 decimales
        return round(resultado, 2)

    except ValueError as e:
        print(f"Error de valor: {e}")
    except ZeroDivisionError as e:
        print(f"Error matemático: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        



# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================

class ValidadorPassword:
    
    
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
       
       # se inicializan los atributos 
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial
        

    def validar(self, password):
      
      #se genera una lista para guardar errores
        errores = []
        
        # valida que el largo de la contraseña sea mayor a la  longitud minima 
        if len(password) < self.min_longitud :
            errores.append("longitud minima no cumplida")
            
        # valida que tenga una mayuscula en la contraseña
        if self.requiere_mayuscula and not any('A' <= c <= 'Z' for c in  password):
            errores.append("Falta mayuscula")
            
        # valida que contenga minusculas en la contraseña 
        if self.requiere_minuscula and not any( 'a' <= c <='b' for c in password):
            errores.append("Falta minuscula")
            
        # valida que consega almenos 1 numero en la contraseña
        if self.requiere_numero and not any('0' <= c <= '9' for c in password):
            errores.append("Falta un numero")
            
        # valida de la lista de caracteres especiales que almenos tenga 1     
        caracteres_especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
        if self.requiere_especial and not any(c in caracteres_especiales for c in password):
            errores.append("Falta caracter especial")
            
        #retorna los valores 
        if errores:
            return (False,errores)
        else:
            return (True, [])
    
    def es_fuerte(self, password):
        
        #valida todos los argumentos al tiempo para validar un true or false
        caracteres_especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
        return(
            len(password)>= 12 and 
            any('A'<= c <='Z' for c in password) and
            any('a'<= c <='z' for c in password)and
            any('0'<= c <= '9' for c in password) and 
            any(c in caracteres_especiales for c in password)
        )


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================

class GestorInventario:
    """Sistema de gestión de inventario."""
    
    def __init__(self):
        """
        Inicializa el inventario.
        Estructura: {codigo: {'nombre', 'precio', 'cantidad', 'categoria'}}
        """
        # TODO: Inicializar estructuras de datos
        self.inventario = {}
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        
        #valida si el producto ya esta 
        if codigo in self.inventario:
            raise ValueError(f"El producto con código '{codigo}' ya existe en el inventario.")
           
       #ingresa el producto al inventario 
        self.inventario[codigo] = {
            'nombre' : nombre,
            'precio' : float(precio),
            'cantidad': int(cantidad),
            'categoria' : categoria
        } 
        
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza el stock de un producto.
        
        Args:
            cantidad_cambio: Positivo para añadir, negativo para reducir
        
        Raises:
            ValueError: Si producto no existe o stock resultante sería negativo
        """
        # TODO: Implementar
        if codigo not in self.inventario:
            raise ValueError(f"El producto con el codigo :{codigo} no exite.")
        
        nuevo_stock = self.inventario[codigo]['cantidad']+ cantidad_cambio
        if nuevo_stock < 0:
            raise ValueError("El stock no puede ser negativo ")
        
        self.inventario[codigo]['cantidad'] = nuevo_stock
            
    
    def buscar_por_categoria(self, categoria):
        """
        Busca productos por categoría.
        
        Returns:
            list: Lista de tuplas (codigo, nombre, precio)
        """
        # TODO: Implementar
        resultado = []
        for codigo,dato in self.inventario.items():
            if dato['categoria'].lower() == categoria.lower():
                resultado.append((codigo,dato['nombre'],dato['precio']))
        return resultado
    
    def productos_bajo_stock(self, limite=10):
        """
        Encuentra productos con stock bajo el límite.
        
        Returns:
            dict: {codigo: cantidad} de productos bajo el límite
        """
        # TODO: Implementar
        return {
            codigo : dato['cantidad']
            for codigo,dato in self.inventario.items()
            if dato['cantidad'] < limite
        }
    
    def valor_total_inventario(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Suma de (precio * cantidad) de todos los productos
        """
        # TODO: Implementar
        total = 0
        for dato in self.inventario.values():
            total += dato['cantidad'] * dato['precio']
            return round(total,2)
    
    def top_productos(self, n=5):
        """
        Retorna los N productos con mayor valor en inventario.
        
        Returns:
            list: Lista de tuplas (codigo, valor_total) ordenadas descendentemente
        """
        # TODO: Implementar
        valores = [
            (codigo, datos['precio'] * datos['cantidad'])
            for codigo, datos in self.inventario.items()
        ]
        valores.sort(key=lambda x: x[1], reverse=True)
        return valores[:n]



# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si divisible por 100: no bisiesto
    - EXCEPTO si divisible por 400: bisiesto
    
    Returns:
        bool: True si es bisiesto, False en caso contrario
    """
    # TODO: Implementar
    if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
        return True
    return False


def dias_en_mes(mes, anio):
    """
    Retorna el número de días en un mes específico.
    
    Args:
        mes: Número del mes (1-12)
        anio: Año (considera bisiestos)
    
    Returns:
        int: Número de días en el mes
    
    Raises:
        ValueError: Si mes es inválido (no está entre 1 y 12)
    """
    # TODO: Implementar
    if mes < 1 and mes > 12 :
        raise ValueError("El mes debe estar entre 1 y 12 ")
    
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if mes == 2 and es_bisiesto(anio):
        return 29
    return dias_por_mes[mes - 1]




def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera representación string del calendario de un mes.
    
    Args:
        mes: Mes (1-12)
        anio: Año
        dia_inicio: Día de la semana del primer día (0=Lunes, 6=Domingo)
    
    Returns:
        str: Calendario formateado
        
    Formato:
    Lu Ma Mi Ju Vi Sa Do
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    ...
    """
    # TODO: Implementar
    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12.")
    if dia_inicio < 0 or dia_inicio > 6:
        raise ValueError("El día de inicio debe estar entre 0 (Lunes) y 6 (Domingo).")

    dias_mes = dias_en_mes(mes, anio)
    
    # Encabezado
    encabezado = "Lu Ma Mi Ju Vi Sa Do\n"
    calendario = "   " * dia_inicio  # Espaciado inicial

    dia = 1
    while dia <= dias_mes:
        calendario += f"{dia:2d} "  # ancho fijo para alineación
        dia_inicio += 1
        if dia_inicio % 7 == 0:
            calendario += "\n"
        dia += 1
    
    return encabezado + calendario.strip()

# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================

def analizar_ventas(ventas):
    """
    Analiza lista de ventas y genera estadísticas.
    
    Args:
        ventas: Lista de dicts con 'producto', 'cantidad', 'precio', 'descuento'
    
    Returns:
        dict: {
            'total_ventas': float,
            'promedio_por_venta': float,
            'producto_mas_vendido': str,
            'venta_mayor': dict,
            'total_descuentos': float
        }
    """
    # TODO: Implementar
    if not ventas:
        return {
            'total_ventas': 0.0,
            'promedio_por_venta': 0.0,
            'producto_mas_vendido': None,
            'venta_mayor': {},
            'total_descuentos': 0.0
        }

    total_ventas = 0.0
    total_descuentos = 0.0
    producto_cantidades = {}
    venta_mayor = None
    max_valor = float('-inf')
    
    for venta in ventas:
        
        cantidad = venta['cantidad']
        precio = venta['precio']
        descuento = venta['descuento']
        producto =venta['producto']

        subtotal = cantidad * precio
        total = subtotal * (1 - descuento)
        ahorro = subtotal * descuento
        
        total_ventas += total
        total_descuentos = ahorro
        producto_cantidades[producto] = producto_cantidades.get(producto, 0) + cantidad
        if total > max_valor:
            max_valor = total
            venta_mayor = venta

    producto_mas_vendido = max(producto_cantidades, key=producto_cantidades.get)
    promedio_por_venta = total_ventas / len(ventas)

    return {
        'total_ventas': round(total_ventas, 2),
        'promedio_por_venta': round(promedio_por_venta, 2),
        'producto_mas_vendido': producto_mas_vendido,
        'venta_mayor': venta_mayor,
        'total_descuentos': round(total_descuentos, 2)
    }

        

def encontrar_patrones(numeros):
    """
    Encuentra patrones en una secuencia de números.
    
    Returns:
        dict: {
            'secuencias_ascendentes': int,
            'secuencias_descendentes': int,
            'longitud_max_ascendente': int,
            'longitud_max_descendente': int,
            'numeros_repetidos': dict
        }
    """
    # TODO: Implementar
    if not numeros:
        return {
            'secuencias_ascendentes': 0,
            'secuencias_descendentes': 0,
            'longitud_max_ascendente': 0,
            'longitud_max_descendente': 0,
            'numeros_repetidos': {}
        }

    secuencias_asc, secuencias_desc = 0, 0
    max_asc, max_desc = 1, 1
    actual_asc, actual_desc = 1, 1
    repeticiones = {}

    for i in range(1, len(numeros)):
        # Contar repeticiones
        repeticiones[numeros[i]] = repeticiones.get(numeros[i], 0) + 1

        # Secuencia ascendente
        if numeros[i] > numeros[i - 1]:
            actual_asc += 1
            max_asc = max(max_asc, actual_asc)
        else:
            if actual_asc > 1:
                secuencias_asc += 1
            actual_asc = 1

        # Secuencia descendente
        if numeros[i] < numeros[i - 1]:
            actual_desc += 1
            max_desc = max(max_desc, actual_desc)
        else:
            if actual_desc > 1:
                secuencias_desc += 1
            actual_desc = 1

    # Contar última secuencia si terminó en el final
    if actual_asc > 1:
        secuencias_asc += 1
    if actual_desc > 1:
        secuencias_desc += 1

    # Filtrar solo números realmente repetidos
    repetidos = {num: cant for num, cant in repeticiones.items() if cant > 1}

    return {
        'secuencias_ascendentes': secuencias_asc,
        'secuencias_descendentes': secuencias_desc,
        'longitud_max_ascendente': max_asc,
        'longitud_max_descendente': max_desc,
        'numeros_repetidos': repetidos
    }



def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    
    Args:
        principal: Monto inicial
        tasa_anual: Tasa de interés (0.05 para 5%)
        anios: Número de años
        aporte_anual: Aporte adicional al inicio de cada año
    
    Returns:
        list: Lista de dicts con 'anio', 'balance', 'interes_ganado'
    """
    # TODO: Implementar
    ""
    resultados = []
    balance = principal

    for anio in range(1, anios + 1):
        interes_ganado = balance * tasa_anual
        balance += interes_ganado + aporte_anual
        resultados.append({
            'anio': anio,
            'balance': round(balance, 2),
            'interes_ganado': round(interes_ganado, 2)
        })
    
    return resultados


# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DE EJERCICIOS")
    print("="*70)
    
    # Aquí puedes añadir tus propias pruebas
    
    print("\nEjercicio 1: Calculadora \n")
    #Pruebas 
    print("la division de 10 / 3 es: ",calculadora_cientifica("division", 10, 3))  # Retorna: 3.33
    print("la potencia de 2 a la 8 es : ",calculadora_cientifica("potencia", 2, 8))   # Retorna: 256.0
    print("La division es :",calculadora_cientifica("division", 10, 0))  # Lanza ZeroDivisionError
    print("la raiz es :",calculadora_cientifica("raiz", 4, 2))       # Lanza ValueError
    
    print("\nEjercicio 2: Validador de Password \n")
    
    validador = ValidadorPassword(min_longitud=8)
    print(validador.validar("Abc123!"))         # (False, ['Longitud mínima no cumplida'])
    print(validador.validar("Abc123!@"))        # (True, [])
    print(validador.validar("abcdefgh"))        # (False, ['Falta mayúscula', ...])
    print(validador.es_fuerte("Abc123!@#$Xyz")) # True
    
    print("\nEjercicio 3: Gestor de Inventario \n")
    
    inv = GestorInventario()
    inv.agregar_producto("P001", "Laptop", 1200.00, 15, "Electrónica")
    inv.agregar_producto("P002", "Mouse", 25.50, 5, "Accesorios")
    inv.agregar_producto("P003", "Teclado", 85.00, 8, "Accesorios")

    inv.actualizar_stock("P001", -3)  # Reduce stock
    print(inv.productos_bajo_stock(10))  # {'P002': 5, 'P003': 8}
    print(inv.buscar_por_categoria("Accesorios"))  # [('P002', 'Mouse', 25.5), ...]
    print(inv.valor_total_inventario())  # Suma total
    print(inv.top_productos(2))  # Top 2 productos por valor
    
    print("\nEjercicio 4: Calendario \n")
    
    print(es_bisiesto(2024))  # True
    print(es_bisiesto(2100))  # False
    print(es_bisiesto(2000))  # True
    print(dias_en_mes(2, 2024))  # 29
    print(dias_en_mes(2, 2023))  # 28
    print(generar_calendario(1, 2024, 0))  # Calendario de enero 2024
    
    print("\nEjercicio 5: Análisis de Datos\n")
    from pprint import pprint
    ventas = [
    {'producto': 'Laptop', 'cantidad': 2, 'precio': 1000, 'descuento': 0.1},
    {'producto': 'Mouse', 'cantidad': 10, 'precio': 20, 'descuento': 0.0},
    {'producto': 'Laptop', 'cantidad': 3, 'precio': 1000, 'descuento': 0.15}
    ]
    pprint(analizar_ventas(ventas))

    numeros = [1, 2, 3, 2, 1, 2, 3, 4, 5, 3, 3, 3]
    pprint(encontrar_patrones(numeros))

    pprint(simular_crecimiento(1000, 0.05, 5, 100))
