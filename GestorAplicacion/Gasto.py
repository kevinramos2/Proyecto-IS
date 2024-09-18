from datetime import datetime

class Gasto:
    _todos_los_gastos = []

    def __init__(self, valor, concepto, fecha=None):
        self.valor = valor
        self.concepto = concepto
        self.fecha = fecha or datetime.now()
        
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
