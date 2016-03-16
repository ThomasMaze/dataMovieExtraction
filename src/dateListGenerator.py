import calendar
import datetime as dt
from sys import exit

def dateGenerator(start_date=dt.date(2012,1,1)):

    stop_date = dt.date.today()

    cal = calendar.Calendar(calendar.WEDNESDAY)
    year = cal.yeardatescalendar(start_date.year,1)

    #intializing week and month index
    wIndex = 0
    mIndex = start_date.month-1
    while year[mIndex][0][wIndex][0] < start_date :
        wIndex = wIndex + 1

    #intializing the current date to the first Wednesday after start date
    current_date = year[mIndex][0][wIndex][0]

    dateList = []

    while current_date <= stop_date :

        if current_date.month == mIndex+1:
            dateList = dateList + [current_date.isoformat()]

        wIndex = wIndex + 1

        try:
            current_date = year[mIndex][0][wIndex][0]
        except IndexError:
            wIndex = 0
            mIndex = mIndex + 1

            if mIndex >= 12 :
                dateList = dateList + dateGenerator(dt.date(start_date.year+1,1,1))
                break
            else :
                current_date = year[mIndex][0][wIndex][0]

    return dateList
