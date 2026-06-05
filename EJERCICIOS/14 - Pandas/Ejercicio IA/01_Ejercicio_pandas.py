#Consigna 1 Importación y Exploración Inicial
print("\n\n-----------------------------------------------------------------------------------------------------------")
print("CONSIGNA 1 Importación y Exploración Inicial")
print("-----------------------------------------------------------------------------------------------------------\n\n")

#a- Importa la librería pandas.
import pandas as pd

#b- Carga el archivo deportistas.csv en un DataFrame (la estructura principal de Pandas).
df = pd.read_csv("deportistas.csv")

#c-  Imprime tu DataFrame inicial para verificar que se cargó correctamente.
print("\nDataFrame Inicial\n\n", df)

#d- Imprime en consola los primeros 5 registros para verificar que se cargó bien.
print("\nPrimeros 5 registros\n\n", df.head())

#e- Imprime un resumen de la información del DataFrame que te muestre los tipos de datos de cada columna y cuántos valores nulos hay.
print("\nresumen estadístico\n\n") 
df.info()

#f- Imprimir resumen estadístico de las columnas numéricas
print("\nresumen estadístico\n\n", df.describe())


#Consigna 2 Aplicar la limpieza en el código
print("\n\n-----------------------------------------------------------------------------------------------------------")
print("CONSIGNA 2 Aplicar la limpieza en el código")
print("-----------------------------------------------------------------------------------------------------------\n\n")

# a- La jugadora Antonella no tiene dato de Masa_Adiposa_kg. Vamos a rellenar ese hueco con el promedio de masa adiposa de todo el plantel.
# (Pista: Averigua cómo usar el método .fillna() en esa columna específica, combinándolo con el método .mean().)

df["Masa_Adiposa_kg"] = df["Masa_Adiposa_kg"].fillna(df["Masa_Adiposa_kg"].mean())

# b- El corredor Ariel no tiene dato en Masa_Muscular_kg. Como consideramos que es un dato crítico que no queremos estimar, vamos a eliminar su fila completa.
# (Pista: Averigua cómo usar el método .dropna() y su parámetro subset para eliminar solo las filas donde falte este dato en particular.)

df.dropna(subset=["Masa_Muscular_kg"], inplace=True)

# c- Imprime tu DataFrame final (print(df)) y un nuevo print(df.info()) para comprobar que ahora tienes 9 registros en total y cero valores nulos.

print("\nDataFrame final\n\n", df)
print("\nInformación final del DataFrame\n\n") 
df.info()


#Consigna 3 Creación de Nuevas Columnas (Ingeniería de Variables)
print("\n\n-----------------------------------------------------------------------------------------------------------")
print("CONSIGNA 3 Creación de Nuevas Columnas (Ingeniería de Variables)")
print("-----------------------------------------------------------------------------------------------------------\n\n")

# a- Crear la columna Porcentaje_Musculo: * Dividí la columna Masa_Muscular_kg por la columna Peso_kg, y al resultado multiplicalo por 100.

df["Porcentaje_Musculo"] = (df["Masa_Muscular_kg"] / df["Peso_kg"]) * 100

# b- Crear la columna Gasto_Ejercicio_kcal: Gasto = METs promedio x Peso Peso_kg
# Multiplicá la columna METs_promedio por Peso_kg

df["Gasto_Ejercicio_kcal"] = df["METs_promedio"] * df["Peso_kg"]

# c- Crear la columna Gasto_Total_Estimado_kcal:

df["Gasto_Total_Estimado_kcal"] = df["NEAT_kcal"] + df["Gasto_Ejercicio_kcal"]

# d- Presentar solo Nombre', 'Porcentaje_Musculo', 'Gasto_Total_Estimado_kcal

print("\nDataFrame final con nuevas columnas\n\n", df[["Nombre", "Porcentaje_Musculo", "Gasto_Total_Estimado_kcal"]])


#Consigna 4 Filtrado, Agrupamiento y Ordenamiento
print("\n\n-----------------------------------------------------------------------------------------------------------")
print("CONSIGNA 4 Filtrado, Agrupamiento y Ordenamiento")
print("-----------------------------------------------------------------------------------------------------------\n\n")

# a- Filtrar deportistas lesionados (Filtro Condicional):
# Kinesiología necesita la lista de los jugadores que están actualmente lesionados para ajustar sus cargas.

df_lesionados = df[df["Lesionado"] == "Sí"]
print("\nDeportistas lesionados\n\n", df_lesionados)

# b- Gasto energético por deporte (Agrupamiento):
# Queremos ver si hay diferencias significativas en el gasto total estimado entre los futbolistas y los maratonistas de nuestro plantel.

promedio_por_deporte = df.groupby("Deporte")["Gasto_Total_Estimado_kcal"].mean()
print("\nGasto total estimado por deporte\n\n", promedio_por_deporte)

# c- Ranking de masa muscular (Ordenamiento):
# Queremos ver quiénes son los deportistas con mayor porcentaje de músculo.

df.sort_values(by="Porcentaje_Musculo", ascending=False, inplace=True)
print("\nTop 3 deportistas con mayor porcentaje de músculo\n\n", df[["Nombre", "Porcentaje_Musculo"]].head(3))


#Consigna 5 Cruce de Datos (Merge) y Exportación
print("\n\n-----------------------------------------------------------------------------------------------------------")
print("CONSIGNA 5 Cruce de Datos (Merge) y Exportación")
print("-----------------------------------------------------------------------------------------------------------\n\n")

# a- Crear el segundo DataFrame (La tabla de suplementación):

data_suplementos = {
    "Deporte": ["Fútbol", "Maratón"],
    "Suplemento_Base": ["Proteína de suero", "BCAA"]
}
df_suplementos = pd.DataFrame(data_suplementos)

# b- Cruzar los datos (Merge):

df_completo = pd.merge(df, df_suplementos, on="Deporte", how="left")
print("\nDataFrame completo con suplemento asignado\n\n", df_completo[["Nombre", "Deporte", "Suplemento_Base"]])

# c- Exportar el resultado final:

df_completo.to_csv("deportistas_procesado.csv", index=False)
print("\n¡Archivo exportado con éxito!")