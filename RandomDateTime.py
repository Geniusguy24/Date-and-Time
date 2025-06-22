import time

import random

def GetRandomDate(startdate, enddate):

    print("Printing Random date between: ", startdate, " and ", enddate)
    randomgenerator = random.random()
    dateformat = "%m/%d/%Y"

    starttime = time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(enddate, dateformat))

    randomtime = starttime = randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))

    return randomdate

print("Random Date = ", GetRandomDate("1/1/2016", "12/12/2018"))