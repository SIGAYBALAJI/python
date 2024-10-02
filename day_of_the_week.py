import datetime
import calendar
def findDay(date):
    born=datetime.datetime.strptime(date,' %d %m %y').weekday()
    return calendar.day_name[born]
date="20 07 2004"
print(findDay(date))