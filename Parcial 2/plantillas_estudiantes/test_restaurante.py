import unittest
import os
from sistema_gestion_restaurante import (
    SistemaRestaurante,
    PlatoNoEncontrado,
    MesaNoDisponible,
    CapacidadExcedida,
    PedidoInvalido,
    ErrorRestaurante
)

class TestSistemaRestaurante(unittest.TestCase):
    
    def setUp(self):
        """Configura un nuevo sistema de restaurante para cada prueba."""
        self.restaurante = SistemaRestaurante(num_mesas=5, tasa_impuesto=0.10, propina_sugerida=0.10)
        
        # Configuración inicial
        self.restaurante.configurar_mesa(1, 4)
        self.restaurante.configurar_mesa(2, 2)
        
        # Menú inicial
        self.restaurante.agregar_plato("E001", "Sopa", "entrada", 50.0)
        self.restaurante.agregar_plato("P001", "Filete", "plato_fuerte", 200.0)
        self.restaurante.agregar_plato("B001", "Agua", "bebida", 20.0)

    def test_1_agregar_plato_exito_y_error(self):
        """Prueba agregar un plato exitosamente y fallar con duplicado."""
        self.restaurante.agregar_plato("D001", "Pastel", "postre", 80.0)
        self.assertIn("D001", self.restaurante.menu)
        self.assertEqual(self.restaurante.menu["D001"]["nombre"], "Pastel")
        
        # Prueba de error por código duplicado
        with self.assertRaises(KeyError):
            self.restaurante.agregar_plato("E001", "Otra Sopa", "entrada", 60.0)
            
        # Prueba de error por categoría inválida
        with self.assertRaises(ValueError):
            self.restaurante.agregar_plato("X001", "Error", "comida", 10.0)

    def test_2_reservar_mesa_exito_y_errores(self):
        """Prueba reservar mesa y las excepciones de capacidad y disponibilidad."""
        # Éxito
        self.restaurante.reservar_mesa(1, 4, "19:00")
        self.assertTrue(self.restaurante.mesas[1]['ocupada'])
        
        # Error: Capacidad Excedida
        with self.assertRaises(CapacidadExcedida):
            self.restaurante.reservar_mesa(2, 3, "20:00") # Mesa 2 solo tiene capacidad 2
            
        # Error: Mesa No Disponible
        with self.assertRaises(MesaNoDisponible):
            self.restaurante.reservar_mesa(1, 1, "20:00") # Mesa 1 ya está ocupada
            
    def test_3_flujo_pedido_calculo_total(self):
        """Prueba el flujo completo: reservar, pedir, agregar y calcular total."""
        self.restaurante.reservar_mesa(1, 2, "14:00")
        id_pedido = self.restaurante.crear_pedido(1)
        
        # Agregar items
        self.restaurante.agregar_item(id_pedido, "E001", 1) # 50
        self.restaurante.agregar_item(id_pedido, "P001", 2) # 200 * 2 = 400
        # Subtotal = 450
        
        # Calcular total (Impuesto 10%, Propina 15%)
        # Subtotal = 450
        # Impuesto = 450 * 0.10 = 45
        # Propina = 450 * 0.15 = 67.5
        # Total = 450 + 45 + 67.5 = 562.5
        
        totales = self.restaurante.calcular_total(id_pedido, propina_porcentaje=0.15)
        
        self.assertAlmostEqual(totales['subtotal'], 450.0)
        self.assertAlmostEqual(totales['impuesto'], 45.0)
        self.assertAlmostEqual(totales['propina'], 67.5)
        self.assertAlmostEqual(totales['total'], 562.5)

    def test_4_pagar_pedido_y_liberar_mesa(self):
        """Prueba que el pedido se marca como pagado y se añade a ventas."""
        self.restaurante.reservar_mesa(2, 2, "15:00")
        id_pedido = self.restaurante.crear_pedido(2)
        self.restaurante.agregar_item(id_pedido, "B001", 5) # 5 * 20 = 100
        
        # Pagar
        self.restaurante.pagar_pedido(id_pedido, propina_porcentaje=0.20)
        
        # Verificar estado
        self.assertTrue(self.restaurante.pedidos[id_pedido]['pagado'])
        self.assertIn(id_pedido, self.restaurante.ventas_dia)
        self.assertAlmostEqual(self.restaurante.pedidos[id_pedido]['total'], 130.0) # 100 + 10 (imp) + 20 (prop)
        
        # Error: No se puede agregar item a pedido pagado
        with self.assertRaises(PedidoInvalido):
            self.restaurante.agregar_item(id_pedido, "E001", 1)
            
        # Liberar mesa
        self.restaurante.liberar_mesa(2)
        self.assertFalse(self.restaurante.mesas[2]['ocupada'])

    def test_5_excepciones_pedido_y_plato(self):
        """Prueba las excepciones PlatoNoEncontrado y PedidoInvalido."""
        self.restaurante.reservar_mesa(1, 1, "16:00")
        id_pedido = self.restaurante.crear_pedido(1)
        
        # Error: Plato No Encontrado
        with self.assertRaises(PlatoNoEncontrado):
            self.restaurante.agregar_item(id_pedido, "X999", 1)
            
        # Error: Plato no disponible
        self.restaurante.cambiar_disponibilidad("P001", False)
        with self.assertRaises(ValueError):
            self.restaurante.agregar_item(id_pedido, "P001", 1)
            
        # Error: Pedido no existe
        with self.assertRaises(PedidoInvalido):
            self.restaurante.calcular_total("PEDIDO_FALSO")

    def test_6_reportes_ventas(self):
        """Prueba que los reportes de ventas se calculan correctamente."""
        # Pedido 1 (Mesa 1)
        self.restaurante.reservar_mesa(1, 2, "12:00")
        id1 = self.restaurante.crear_pedido(1)
        self.restaurante.agregar_item(id1, "E001", 2) # 2x Sopa (100)
        self.restaurante.agregar_item(id1, "P001", 1) # 1x Filete (200)
        self.restaurante.pagar_pedido(id1, 0.10) # Subtotal 300
        self.restaurante.liberar_mesa(1)
        
        # Pedido 2 (Mesa 2)
        self.restaurante.reservar_mesa(2, 1, "13:00")
        id2 = self.restaurante.crear_pedido(2)
        self.restaurante.agregar_item(id2, "P001", 1) # 1x Filete (200)
        self.restaurante.pagar_pedido(id2, 0.10) # Subtotal 200
        self.restaurante.liberar_mesa(2)

        # Prueba Platos más vendidos
        mas_vendidos = self.restaurante.platos_mas_vendidos(3)
        self.assertEqual(len(mas_vendidos), 2)
        self.assertEqual(mas_vendidos[0], ("P001", "Filete", 2))
        self.assertEqual(mas_vendidos[1], ("E001", "Sopa", 2))
        
        # Prueba Ventas por categoría
        ventas_cat = self.restaurante.ventas_por_categoria()
        self.assertAlmostEqual(ventas_cat['entrada'], 100.0)
        self.assertAlmostEqual(ventas_cat['plato_fuerte'], 400.0)
        self.assertAlmostEqual(ventas_cat['bebida'], 0.0)
        
        # Prueba Reporte general
        reporte = self.restaurante.reporte_ventas_dia()
        self.assertEqual(reporte['total_pedidos'], 2)
        self.assertAlmostEqual(reporte['subtotal_ventas'], 500.0) # 300 + 200
        self.assertAlmostEqual(reporte['total_ingresos'], 600.0) # (300*1.2) + (200*1.2)
        self.assertEqual(reporte['plato_mas_vendido'], "Filete")

    def test_7_buscar_platos(self):
        """Prueba el filtro de búsqueda de platos."""
        self.restaurante.agregar_plato("E002", "Ensalada", "entrada", 100.0)
        self.restaurante.cambiar_disponibilidad("E001", False) # Sopa no disponible
        
        # Buscar por categoría
        entradas = self.restaurante.buscar_platos(categoria="entrada")
        self.assertEqual(len(entradas), 1)
        self.assertEqual(entradas[0]['codigo'], "E002")
        
        # Buscar por precio
        baratos = self.restaurante.buscar_platos(precio_max=60.0)
        self.assertEqual(len(baratos), 1) # Solo el Agua (20)
        self.assertEqual(baratos[0]['codigo'], "B001")
        
        # Buscar todos los disponibles
        todos = self.restaurante.buscar_platos()
        self.assertEqual(len(todos), 3) # Ensalada, Filete, Agua

    def test_8_importar_menu(self):
        """Prueba la importación de menú desde un archivo."""
        contenido_menu = (
            "I001|Tacos|plato_fuerte|150.0|True\n"
            "I002|Flan|postre|70.0|True\n"
            "I003|Pozole|entrada\n" # Línea con error
            "E001|Sopa Nueva|entrada|55.0|True\n" # Código duplicado
        )
        archivo_prueba = "test_menu_import.txt"
        
        with open(archivo_prueba, "w", encoding="utf-8") as f:
            f.write(contenido_menu)
            
        reporte = self.restaurante.importar_menu(archivo_prueba)
        
        # Verificar reporte
        self.assertEqual(reporte['exitosos'], 2)
        self.assertEqual(len(reporte['errores']), 2)
        self.assertEqual(reporte['errores'][0][0], 3) # Línea 3
        self.assertEqual(reporte['errores'][1][0], 4) # Línea 4
        
        # Verificar que los platos exitosos están en el menú
        self.assertIn("I001", self.restaurante.menu)
        self.assertIn("I002", self.restaurante.menu)
        self.assertEqual(self.restaurante.menu["I001"]["precio"], 150.0)
        
        # Verificar que el duplicado no sobrescribió
        self.assertEqual(self.restaurante.menu["E001"]["precio"], 50.0)
        
        # Limpiar archivo
        os.remove(archivo_prueba)

if __name__ == '__main__':
    unittest.main()