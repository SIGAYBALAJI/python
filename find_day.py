import datetime
import calendar
def find_day(date):
    born=datetime.datetime.strptime(date,'%d %m %y').weekday()
    return (calendar.day_name[born])
date="14 12 2001"
print(find_day(date))
