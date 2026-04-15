from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

# Calendario del mes
cal = calendar.month(2024, 1)
print("Calendario Enero 2024:")
print(cal)
# Información del mes
print("Días en mes:", calendar.monthrange(2024, 1))
print("¿Año bisiesto?", calendar.isleap(2024))
print("Día de la semana para 15/1/2024:", calendar.weekday(2024, 1, 15))