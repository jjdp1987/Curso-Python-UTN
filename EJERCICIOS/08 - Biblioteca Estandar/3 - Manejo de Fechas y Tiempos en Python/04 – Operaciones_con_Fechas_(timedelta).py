from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

hoy = datetime.now()
# Sumar días
futuro = hoy + timedelta(days=7)
print("En 7 días:", futuro)
# Restar horas
pasado = hoy - timedelta(hours=24)
print("Hace 24 horas:", pasado)
# Combinar operaciones
complejo = hoy + timedelta(days=2, hours=3, minutes=30)
print("En 2 días, 3 horas y 30 minutos:", complejo)
# Diferencia entre fechas
diferencia = futuro - pasado
print("Diferencia:", diferencia)
print("Días de diferencia:", diferencia.days)
print("Segundos de diferencia:", diferencia.total_seconds())
