from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta
from time import sleep, asctime, time

date1 = datetime(2020,7,11,8,46,50)
date2 = date(1997,11,12)
print(date1)
print(f"nasci na data: ",date2.strftime("%d/%m/%Y"))

semanas = date(2020,10,25) - date.today()
print(semanas)



# dt = date.today() + timedelta(days =+ 120)
dt = date.today() + relativedelta(months =- 3)
print(dt.strftime("%d/%m/%Y"))