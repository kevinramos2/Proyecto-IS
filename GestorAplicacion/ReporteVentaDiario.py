from datetime import datetime
from GestorAplicacion.Producto import Producto
from GestorAplicacion.Venta import Venta
from GestorAplicacion.Gasto import Gasto
import tkinter as tk
from tkinter import *

class ReporteDeVentas:

    def __init__(self) -> None:
        self.fecha_actual = datetime.now().strftime('%Y-%m-%d')
        self.ventas_del_dia = [venta for venta in Venta._todas_las_ventas if venta.fecha.strftime('%Y-%m-%d') == self.fecha_actual]

    def HayVentas(self):
        return bool(self.ventas_del_dia)
    
    def anadir_ventas(self):
        if self.HayVentas():
            for venta in self.ventas_del_dia:
                venta_info = f"ID Venta: {venta.id_venta} | Cliente: {venta.id_cliente} | Total: ${venta.total:.2f} | Estado: {venta.estado}\n"
                for producto, cantidad in venta.productos:
                    venta_info += f"    - Producto: {producto.nombre} | Cantidad: {cantidad} | Precio Unitario: ${producto.get_precio():.2f} COP\n"
                    
                self.productos_listbox.insert(tk.END, venta_info)

    def generar_Reporte_diario_tkinter(self, ventana):
        # Sección para el informe del reporte
        informe_frame = LabelFrame(ventana, text="Informe", bg="#F0F0F0", font=("arial", 12, "bold"))
        informe_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Ajustar la cuadrícula para centrar los elementos
        informe_frame.columnconfigure(0, weight=1)
        informe_frame.columnconfigure(1, weight=3)

        # Label para total de ventas
        total_ventas_label = Label(informe_frame, text="Total de ventas en el dia:", bg="#F0F0F0",font=("arial",12,"italic"))
        total_ventas_label.grid(row=0, column=0, padx=5, pady=(5, 2), sticky="e")

        total_dia = sum(venta.total for venta in self.ventas_del_dia)

        self.total_de_venta_label = Label(informe_frame, text=total_dia,font=("arial",12,"bold"),bg="#F0F0F0")
        self.total_de_venta_label.grid(row=0, column=1, padx=5, pady=(5, 2), sticky="w")

        # Lable para cantidad de ventas
        cantidad_ventas_label = Label(informe_frame, text="Cantidad de ventas en el dia:", bg="#F0F0F0",font=("arial",12,"italic"))
        cantidad_ventas_label.grid(row=1, column=0, padx=5, pady=(5, 2), sticky="e")

        cantidad_dia = len(self.ventas_del_dia)

        self.cantidad_dia_label = Label(informe_frame, text=cantidad_dia,font=("arial",12,"bold"),bg="#F0F0F0")
        self.cantidad_dia_label.grid(row=1, column=1, padx=5, pady=(5, 2), sticky="w")

        # Listbox para mostrar las ventas agregados
        self.productos_listbox = Listbox(informe_frame, width=80)
        self.productos_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Scrollbar para la Listbox
        scrollbar = Scrollbar(informe_frame, orient=VERTICAL, command=self.productos_listbox.yview)
        scrollbar.grid(row=3, column=2, sticky='ns')
        self.productos_listbox.config(yscrollcommand=scrollbar.set)

        scrollbar1 = Scrollbar(informe_frame, orient=HORIZONTAL, command=self.productos_listbox.xview)
        scrollbar1.grid(row=4, column=0, sticky='ew',columnspan=2)
        self.productos_listbox.config(xscrollcommand=scrollbar1.set)

        self.anadir_ventas()

        # Label para Arqueo:
        gastos_del_dia = sum(gasto.valor for gasto in Gasto.getGastosDia())
        Arqueo_text = f"Ganancias o Perdidas: {total_dia - gastos_del_dia}"
        Arqueo_label = Label(informe_frame, text=Arqueo_text, fg="red")
        Arqueo_label.grid(row=5, column=0, columnspan=2, pady= 5)

        

    def generar_reporte_diario():
        #fecha actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        
        #filtra ventas dia actual
        ventas_del_dia = [venta for venta in Venta._todas_las_ventas if venta.fecha.strftime('%Y-%m-%d') == fecha_actual]
        
        if not ventas_del_dia:
            return "No se registraron ventas en el día."
        
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
