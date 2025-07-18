from datetime import datetime
from zoneinfo import ZoneInfo

#Bd timezone
bd_timezone = datetime.now(ZoneInfo("Asia/Dhaka"))
current_time = datetime.now()
print("Current date and time:", current_time)

formatted_time = bd_timezone.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_time)
