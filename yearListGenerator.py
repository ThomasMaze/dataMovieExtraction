import calendar
import datetime as dt

def yearGenerator(year) :

    yearList = []

    firstDay = True

    cal = calendar.Calendar(calendar.WEDNESDAY)

    for month in cal.yeardatescalendar(year,1) :
        for week in month :
            for day in week :
                firstWeekDayDataStr = day[0].isoformat()

                if firstDay :
                    if firstWeekDayDataStr[0:4] == str(year):
                        yearList = yearList + [firstWeekDayDataStr]
                        firstDay = False
                else :
                    if firstWeekDayDataStr != previousFirstWeekDayDataStr and firstWeekDayDataStr < dt.date.isoformat(dt.datetime.now()):
                        yearList = yearList + [firstWeekDayDataStr]

                previousFirstWeekDayDataStr = firstWeekDayDataStr

    return yearList

def generateList() :

    todayISO = dt.datetime.isocalendar(dt.datetime.now())
    yearList = range(2012, todayISO[0]+1)

    wednesdayList = []

    for year in yearList:
        wednesdayList = wednesdayList + yearGenerator(year)

    return wednesdayList
