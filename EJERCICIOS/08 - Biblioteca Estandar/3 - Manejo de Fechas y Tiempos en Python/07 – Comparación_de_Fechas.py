from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

fecha1 = datetime(2024, 1, 15)
fecha2 = datetime(2024, 1, 20)
print("fecha1 < fecha2:", fecha1 < fecha2)
print("fecha1 > fecha2:", fecha1 > fecha2)
print("fecha1 == fecha2:", fecha1 == fecha2)
print("fecha1 != fecha2:", fecha1 != fecha2)
# Comparar con fecha actual
hoy = datetime.now()
print("¿fecha1 es pasado?", fecha1 < hoy)
print("¿fecha2 es futuro?", fecha2 > hoy)