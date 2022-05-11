"""
start on 1 jan 1900 (monday),
go through to the first of the next month
1 feb 1900,
figure out which day it is (req number days in jan and which day was the first of jan)
if sunday add 1 to counter
continue until 1 dec 2000
sort special cases after

"""


def what_day_am_i(NumberOfDaysInPreviousMonth, DayFirstOfPreviousMonth):
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    while NumberOfDaysInPreviousMonth >= 7:
        NumberOfDaysInPreviousMonth %= 7
    NumberOfLastMonth = days.index(DayFirstOfPreviousMonth)
    CurrentDay = days[NumberOfLastMonth + NumberOfDaysInPreviousMonth]
    return CurrentDay

print(what_day_am_i(31,"Monday"))
