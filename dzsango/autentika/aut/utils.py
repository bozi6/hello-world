#  utils.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 01. 05. 22:23
from calendar import HTMLCalendar

from .models import Aut


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

        # format a day as td
        # filter events by day

    def formatday(self, day, events):
        events_per_day = events.filter(datum__day=day)
        d = ""
        for event in events_per_day:
            d += f"<li> {event.musor} </li>"

            if day != 0:
                return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
            return "<td></td>"

    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"

    def formatmonth(self, withyear=True):
        events = Aut.objects.filter(datum__year=self.year, datum__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0"class="calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        return cal
