import calendar

def generator(year) :

    yearList = []

    firstDay = True

    cal = calendar.Calendar(calendar.WEDNESDAY)

    for month in cal.yeardatescalendar(year,1) :
        for week in month :
            for day in week :
                firstWeekDayDataStr = day[0].isoformat()

                if firstDay :
                    if firstWeekDayDataStr[0:4] == str(year) :
                        yearList = yearList + [firstWeekDayDataStr]
                        firstDay = False
                else :
                    if firstWeekDayDataStr != previousFirstWeekDayDataStr :
                        yearList = yearList + [firstWeekDayDataStr]

                previousFirstWeekDayDataStr = firstWeekDayDataStr

    return yearList
