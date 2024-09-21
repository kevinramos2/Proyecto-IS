from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Gasto:
    _todos_los_gastos = []

    def __init__(self, valor, concepto, fecha=None):
        self.valor = valor
        self.concepto = concepto
        self.fecha = fecha
        
        Gasto._todos_los_gastos.append(self)

    def registrar_gasto():
        print("Registro de nuevo gasto")
        print("------------------------")
        
        #solicita valor gasto
        while True:
            valor = input("Ingrese el valor del gasto: ")
            try:
                valor = float(valor)
                break
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
        
        #concepto del gasto
        concepto = input("Ingrese el concepto del gasto: ")
        
        #fecha del gasto
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        
        #registra el gasto
        Gasto(valor, concepto, fecha_actual)
        print(f"Gasto registrado: {concepto}, Valor: ${valor:.2f}, Fecha: {fecha_actual}")

    @classmethod
    def Colocar_Gastos(cls):
        cls.gastos_listbox.delete(0,tk.END)
        for gasto in Gasto._todos_los_gastos:
            texto = f"Valor del gasto: {gasto.valor}  | fecha: {gasto.fecha} | Concepto: {gasto.concepto}"

            cls.gastos_listbox.insert(tk.END, texto)


    @classmethod
    def agregar_gasto(cls):
        valor_gasto = cls.valor_gasto_entry.get()
        concepto_gasto = cls.caja_texto_Concepto.get("1.0", tk.END).strip()
        try:
            numeroValorGasto = float(valor_gasto)
        except:
            messagebox.showerror("Error valor gasto", "Por favor ingrese un valor numérico válido.")
        else:
            fecha_actual = datetime.now().strftime('%Y-%m-%d')
            Gasto(numeroValorGasto, concepto_gasto, fecha_actual)

            cls.valor_gasto_entry.delete(0,tk.END)
            cls.caja_texto_Concepto.delete("1.0", tk.END)

            Gasto.Colocar_Gastos()

    @classmethod
    def registrar_gasto_tkinter(cls,ventana):
        ventana_añadir =  Toplevel(ventana)
        ventana_añadir.title("Añadir Gasto")
        ventana_añadir.geometry("500x350")

        informe_frame = LabelFrame(ventana_añadir, text="Añadir Gasto", bg="#F0F0F0", font=("arial", 12, "bold"))
        informe_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Ajustar la cuadrícula para centrar los elementos
        informe_frame.columnconfigure(0, weight=1)
        informe_frame.columnconfigure(1, weight=3)

        # Entrada para el valor del gasto
        valor_gasto_label = Label(informe_frame, text="Valor del gasto:", bg="#F0F0F0")
        valor_gasto_label.grid(row=0, column=0, padx=5, pady=(5, 2), sticky="nsew")

        cls.valor_gasto_entry = Entry(informe_frame)
        cls.valor_gasto_entry.grid(row=0, column=1, padx=5, pady=(5, 2), sticky="w")

        # Entrada para el concepto del gasto
        Concepto_gasto_label = Label(informe_frame, text="Ingrese el concepto o informacion del gasto", bg="#F0F0F0")
        Concepto_gasto_label.grid(row=1, column=0, padx=5, pady=(5, 2), sticky="w")

        cls.caja_texto_Concepto = Text(informe_frame, height=10, width=80)
        cls.caja_texto_Concepto.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew", rowspan=3)

        # Botón para agregar producto a la lista
        agregar_gasto_btn = Button(informe_frame, text="Agregar Producto", bg="#F0F0F0", fg="black", command= Gasto.agregar_gasto)
        agregar_gasto_btn.grid(row=5, column=0, columnspan=2, pady=10)
        
        

        

    @classmethod
    def generar_gastos_tkinter(cls, ventana):
        # Sección para el informe del reporte
        informe_frame = LabelFrame(ventana, text="Informe Gastos", bg="#F0F0F0", font=("arial", 12, "bold"))
        informe_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Ajustar la cuadrícula para centrar los elementos
        informe_frame.columnconfigure(0, weight=1)
        informe_frame.columnconfigure(1, weight=3)

        # Label para total de ventas
        Gastos_label = Label(informe_frame, text="Gastos totales:", bg="#F0F0F0",font=("arial",12,"italic"))
        Gastos_label.grid(row=0, column=0, padx=5, pady=(5, 2), sticky="e")

        # Boton para agregar gastos
        Boton_añadir_gastos = Button(informe_frame, text= "Agregar Gasto", command= lambda: Gasto.registrar_gasto_tkinter(ventana))
        Boton_añadir_gastos.grid(row=0,column=1,padx=5, pady=5)

        # Listbox para mostrar los gastos agregados
        cls.gastos_listbox = Listbox(informe_frame, width=80)
        cls.gastos_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew", rowspan=3)

        # Scrollbar para la Listbox
        scrollbar = Scrollbar(informe_frame, orient=VERTICAL, command=cls.gastos_listbox.yview)
        scrollbar.grid(row=3, column=2, sticky='ns')
        cls.gastos_listbox.config(yscrollcommand=scrollbar.set)

        Gasto.Colocar_Gastos()

    def generar_reporte_gastos_diario():
        print("Reporte de gastos diario")
        print("------------------------")

        #obtiene fecha actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        print(f"Fecha: {fecha_actual}")

        #filtra gastos del dia
        gastos_del_dia = [gasto for gasto in Gasto._todos_los_gastos if gasto.fecha.strftime('%Y-%m-%d') == fecha_actual]

        if not gastos_del_dia:
            print("No se registraron gastos en el día.")
            return

        #muestra resumen de gastos
        total_gastos_dia = sum(gasto.valor for gasto in gastos_del_dia)
        print(f"Total gastos: ${total_gastos_dia:.2f} COP")
        print(f"Cantidad de gastos: {len(gastos_del_dia)}")

        print("\nDetalle de gastos:")
        for gasto in gastos_del_dia:
            print(f"Concepto: {gasto.concepto} | Valor: ${gasto.valor:.2f}")
        print("")

    def generar_reporte_resumido():
        print("Reporte resumido de gastos")
        print("--------------------------")
        
        total_gastos = sum(gasto.valor for gasto in Gasto._todos_los_gastos)
        cantidad_gastos = len(Gasto._todos_los_gastos)
        
        print(f"Total gastos registrados: ${total_gastos:.2f} COP")
        print(f"Cantidad total de gastos: {cantidad_gastos}")
