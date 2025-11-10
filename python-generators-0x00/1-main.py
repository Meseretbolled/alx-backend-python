#!/usr/bin/python3
from itertools import islice
from 0-stream_users import stream_users  # import the generator function

# print only the first 6 users
for user in islice(stream_users(), 6):
    print(user)
