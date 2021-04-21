
import time
# from datetime import datetime
# from datetime import timedelta

# StartDate = datetime.strftime(datetime.today().replace(day=1), "%m/%d/%Y")
# if StartDate == "03/01/2021":
#     StartDate  = StartDate - datetime.timedelta(days=1)


# print(StartDate)
from datetime import date, timedelta, datetime

last_day_of_prev_month = date.today().replace(day=1)- timedelta(days=1)

start_day_of_prev_month = date.strftime(date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day),  "%m/%d/%Y")
 

# For printing results
print("First day of prev month:", start_day_of_prev_month)
print("Last day of prev month:", date.strftime(last_day_of_prev_month,  "%m/%d/%Y"))