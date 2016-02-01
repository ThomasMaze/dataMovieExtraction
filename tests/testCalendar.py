import calendar

cal = calendar.Calendar(calendar.WEDNESDAY)

firstDay = True
yearList = []

for month in cal.yeardatescalendar(2014,1) :
    for week in month :
        for day in week :
            firstWeekDayDataStr = ''
            firstWeekDayData = day[0].isoformat()
            for it in reversed(range(0,3)):
                dataStr = str(firstWeekDayData[it])
                if firstWeekDayData[it] < 10 :
                    dataStr = '0' + dataStr
                firstWeekDayDataStr = firstWeekDayDataStr + dataStr

            if firstDay :
                print firstWeekDayDataStr
                firstDay = False
            else :
                if firstWeekDayDataStr != previousFirstWeekDayDataStr :
                    print firstWeekDayDataStr

            previousFirstWeekDayDataStr = firstWeekDayDataStr
