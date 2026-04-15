from datetime import datetime, date, time, timedelta
import time as time_module
import calendar

# DateTime a timestamp
timestamp = datetime.now().timestamp()
print("Timestamp actual:", timestamp)
# Timestamp a DateTime
dt_desde_timestamp = datetime.fromtimestamp(timestamp)
print("DateTime desde timestamp:", dt_desde_timestamp)
# Timestamp actual directamente
timestamp_actual = time_module.time()
print("Timestamp con time module:", timestamp_actual)