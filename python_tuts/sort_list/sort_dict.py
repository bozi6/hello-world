#!/usr/bin/env python3


users = [
    {'name': 'John Doe', 'date_of_birth': 1987},
    {'name': 'Jane Doe', 'date_of_birth': 1996},
    {'name': 'Robert Brown', 'date_of_birth': 1977},
    {'name': 'Lucia Smith', 'date_of_birth': 2002},
    {'name': 'Patrick Dempsey', 'date_of_birth': 1994}
]

users.sort(reverse=True, key=lambda e: e['date_of_birth'])

for user in users:
    print(user)
