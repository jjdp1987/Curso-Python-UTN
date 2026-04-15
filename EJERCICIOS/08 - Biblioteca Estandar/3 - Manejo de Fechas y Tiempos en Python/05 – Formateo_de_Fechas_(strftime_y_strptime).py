from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

# DateTime a string (formateo)
hoy = datetime.now()
print("Formato completo:", hoy.strftime("%Y-%m-%d %H:%M:%S"))
print("Solo fecha:", hoy.strftime("%d/%m/%Y"))
print("Solo hora:", hoy.strftime("%H:%M:%S"))
print("Nombre mes:", hoy.strftime("%B"))
print("Nombre día:", hoy.strftime("%A"))
print("Formato personalizado:", hoy.strftime("Hoy es %A, %d de %B de %Y"))
# String a DateTime (parsing)
cadena_fecha = "2024-01-15 14:30:00"
dt_parseado = datetime.strptime(cadena_fecha, "%Y-%m-%d %H:%M:%S")
print("DateTime parseado:", dt_parseado)
