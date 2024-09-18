from datetime import datetime
from GestorAplicacion.Producto import Producto
from GestorAplicacion.Venta import Venta

class ReporteDeVentas:

    def generar_reporte_diario():
        print("Reporte de ventas diario")
        print("------------------------")
        
        #fecha actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        print(f"Fecha: {fecha_actual}")
        
        #filtra ventas dia actual
        ventas_del_dia = [venta for venta in Venta._todas_las_ventas if venta.fecha.strftime('%Y-%m-%d') == fecha_actual]
        
        if not ventas_del_dia:
            print("No se registraron ventas en el día.")
            return
        
        #resumen ventas
        total_dia = sum(venta.total for venta in ventas_del_dia)
        print(f"Total ventas: ${total_dia:.2f} COP")
        print(f"Cantidad de ventas: {len(ventas_del_dia)}")

        print("\nDetalle de ventas:")
        for venta in ventas_del_dia:
            print(f"ID Venta: {venta.id_venta} | Cliente: {venta.id_cliente} | Total: ${venta.total:.2f} | Estado: {venta.estado}")
            for producto, cantidad in venta.productos:
                print(f"    - Producto: {producto.nombre} | Cantidad: {cantidad} | Precio Unitario: ${producto.get_precio():.2f} COP")
            print("")

    def generar_reporte_resumido():
        print("Reporte resumido de ventas")
        print("--------------------------")
        
        total_ventas = sum(venta.total for venta in Venta._todas_las_ventas)
        cantidad_ventas = len(Venta._todas_las_ventas)
        
        print(f"Total ventas registradas: ${total_ventas:.2f} COP")
        print(f"Cantidad total de ventas: {cantidad_ventas}")
