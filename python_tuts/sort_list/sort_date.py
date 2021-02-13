#!/usr/bin/env python3

from datetime import datetime

values = ['8-Nov-19', '21-Jun-16', '1-Nov-18', '7-Apr-19']
values.sort(key=lambda d: datetime.strptime(d, "%d-%b-%y"))

print(values)
