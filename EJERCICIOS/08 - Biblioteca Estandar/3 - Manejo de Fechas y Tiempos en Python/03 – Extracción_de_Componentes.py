from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

hoy = datetime.now()

print("Año:", hoy.year)
print("Mes:", hoy.month)
print("Día:", hoy.day)
print("Hora:", hoy.hour)
print("Minuto:", hoy.minute)
print("Segundo:", hoy.second)
print("Microsegundo:", hoy.microsecond)
print("Día de la semana:", hoy.weekday()) # 0=Lunes, 6=Domingo
print("Día del año:", hoy.timetuple().tm_yday)