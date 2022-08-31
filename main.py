from datetime import datetime
from datetime import date
from datetime import time
now = datetime.now()
today=date.today()
nowmthdyyr=today.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")
print("The current time is ", current_time)
print(f'Todays date is {nowmthdyyr}')
#print(now)