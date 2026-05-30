import pandas as pd
import matplotlib.pyplot as plt

#Cargamos datos
ventas = pd.read_csv("datos/dataset.csv")

#### RESUMEN DE VENTAS ####

#Calculamos ventas totales, maximas , minimas y promedio de ventas
ventas_totales = ventas["sales_amount"].sum()
venta_maxima = ventas["sales_amount"].max()
venta_minima = ventas["sales_amount"].min()
promedio_ventas = ventas["sales_amount"].mean()

#Mostramos los calculos
print("\n----- RESUMEN DE VENTAS -----")
print("Ventas totales:", ventas_totales)
print("Venta máxima:", venta_maxima)
print("Venta mínima:", venta_minima)
print("Promedio:", round(promedio_ventas, 2))

#### VENTAS POR MES ####

#Convertimos las fechas al formato fecha (en el csv vienen como strings por defecto)
ventas["sales_date"] = pd.to_datetime(ventas["sales_date"])

#Creamos una columna con año y mes
ventas["mes"] = ventas["sales_date"].dt.strftime("%Y-%m")

#Agrupamos ventas por mes
ventas_por_mes = (
    ventas.groupby("mes")["sales_amount"]
    .sum()
    .reset_index()
)

#Mostramos las ventas por mes
print("\nVentas por mes:")
print(ventas_por_mes)
