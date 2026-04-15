from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

# Fecha actual
fecha_actual = date.today()
print("Fecha actual:", fecha_actual)

# DateTime actual
ahora = datetime.now()
print("Fecha y hora actual:", ahora)

# Crear fecha específica
fecha_especifica = date(2024, 1, 15)
print("Fecha específica:", fecha_especifica)

# Crear datetime específico
dt_especifico = datetime(2024, 1, 15, 14, 30, 45)
print("DateTime específico:", dt_especifico)