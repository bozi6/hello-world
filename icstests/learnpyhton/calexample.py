#  calexample.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 01. 27. 9:33
import os
from datetime import datetime
from pathlib import Path

import pytz
from icalendar import Calendar, Event, vCalAddress, vText

#  init the calendar
cal = Calendar()

# Some properties are required to be compliant
cal.add("prodid", "-//My calendar product//example.com//")
cal.add("version", "2.0")

# Add subcomponents
event = Event()
event.add("name", "Awesome Meeting")
event.add("description", "Define the rodamap of our awesome project")
event.add("dtstart", datetime(2024, 1, 25, 8, 0, 0, tzinfo=pytz.UTC))
event.add("dtend", datetime(2024, 1, 25, 10, 0, 0, tzinfo=pytz.UTC))

# Add the organizer
organizer = vCalAddress("MAILTO:jdoe@example.com")

# Add parameters of the event
organizer.params["name"] = vText("John Doe")
organizer.params["role"] = vText("CEO")
event["organizer"] = organizer
event["location"] = vText("New York, USA")

event["uid"] = "20240108T1148/465386452853@example.com"
event.add("priority", 5)
attendee = vCalAddress("MAILTO:rdoe@example.com")
attendee.params["name"] = vText("Richard Roe")
attendee.params["role"] = vText("REQ-PARTICIPANT")
event.add("attendee", attendee, encode=0)

attendee = vCalAddress("MAILTO:jsmith@example.com")
attendee.params["name"] = vText("John Smith")
attendee.params["role"] = vText("REQ-PARTICIPANT")
event.add("attendee", attendee, encode=0)

# Add the event to calendar
cal.add_component(event)

# Write to disk
directory = Path.cwd() / "MyCalendar"
try:
    directory.mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("Folder already exists")
else:
    print("Folder was created")

f = open(os.path.join(directory, "pelda.ics"), "wb")
f.write(cal.to_ical())
f.close()


#  Created the event let's read it.
sorsz = 0
e = open("../honvedegyuttes@gmail.com.ics", "rb")
ecal = Calendar.from_ical(e.read())
for component in ecal.walk():
    if component.name == "VEVENT":
        print(sorsz, "Summary:", component.get("summary"))
        sorsz += 1
        # print("Description:", component.get("description"))
        # print("Organizer:", component.get("organizer"))
        # print("Location:", component.get("location"))
        # print("Dtstart: ", component.decoded("dtstart"))
        # print("Dtend: ", component.decoded("dtend"))
e.close()
