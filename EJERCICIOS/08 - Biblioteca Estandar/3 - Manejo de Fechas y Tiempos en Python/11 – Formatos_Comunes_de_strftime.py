from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

hoy = datetime.now()
formatos = {
 "%Y": "Año con 4 dígitos",
 "%y": "Año con 2 dígitos",
 "%m": "Mes (01-12)",
 "%d": "Día (01-31)",
 "%H": "Hora (00-23)",
 "%I": "Hora (01-12)",
 "%M": "Minuto (00-59)",
 "%S": "Segundo (00-59)",
 "%f": "Microsegundos",
 "%A": "Nombre día completo",
 "%a": "Nombre día abreviado",
 "%B": "Nombre mes completo",
 "%b": "Nombre mes abreviado",
 "%p": "AM/PM",
 "%Z": "Zona horaria",
 "%z": "UTC offset"
}
for formato, descripcion in formatos.items():
 print(f"{formato}: {hoy.strftime(formato)} - {descripcion}")