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

### GRAFICO ###

#Definimos el tamaño del grafico
plt.figure(figsize=(8, 4))

#Dibujamos el grafico
plt.plot(
    #Eje X
    ventas_por_mes["mes"],
    #Eje Y
    ventas_por_mes["sales_amount"],
    marker="o"
)

#Agregamos el titulo al grafico
plt.title("Evolución de ventas")
#Agregamos el nombre del eje X
plt.xlabel("Mes")
#Agregamos el nombre del eje Y
plt.ylabel("Facturación")

#Rotamos la posicion de los valores para que no se superpongan
plt.xticks(rotation=45)

#Ajustamos automaticamente los espacios del grafico
plt.tight_layout()

#Guardamos el grafico
plt.savefig("resultados/grafico_resultados.png")

#Avisamos que el grafico se genero correctamente y su ubicacion
print(f"\nGráfico generado correctamente.\nUbicado en: resultados/grafico_resultados.png")