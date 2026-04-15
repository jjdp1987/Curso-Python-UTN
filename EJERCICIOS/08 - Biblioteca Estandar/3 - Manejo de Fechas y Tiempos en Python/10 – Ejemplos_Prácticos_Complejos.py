from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

# Calculadora de edad
def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    # Este 'if' tiene que estar adentro del 'def'
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1 # Este 'edad' tiene que estar adentro del 'if'
    return edad

# Uso
nacimiento = date(1990, 5, 15)
print("Edad:", calcular_edad(nacimiento))

# Días hasta cumpleaños
def dias_hasta_cumple(fecha_nacimiento):
    hoy = date.today()
    proximo_cumple = date(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)

    if proximo_cumple < hoy:
        proximo_cumple = date(hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

    return (proximo_cumple - hoy).days

print("Días hasta próximo cumpleaños:", dias_hasta_cumple(nacimiento))

# Validación de fecha
def es_fecha_valida(anio, mes, dia):
    try:
        date(anio, mes, dia) # Adentro del try
        return True
    except ValueError:
        return False

print("¿31 de febrero es válido?", es_fecha_valida(2024, 2, 31))