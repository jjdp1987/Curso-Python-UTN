from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

# Instalar primero: pip install pytz
import pytz
# Zonas horarias disponibles
print("Zonas horarias:", pytz.all_timezones[:10])
# DateTime con zona horaria
utc = pytz.utc
madrid_tz = pytz.timezone('Europe/Madrid')
dt_utc = datetime.now(utc)
dt_madrid = datetime.now(madrid_tz)
print("UTC:", dt_utc)
print("Madrid:", dt_madrid)
# Conversión entre zonas horarias
dt_convertido = dt_utc.astimezone(madrid_tz)
print("UTC convertido a Madrid:", dt_convertido)