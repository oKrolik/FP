"""
Write a script that given an hour and minutes by user input, prints at what time the alarm clock will ring,
 knowing that the current hour is hour and the current minutes are minutes.
 The clock goes off after 6 hour and 51 minutes.
"""
import time
print(time.strftime('%H:%M', time.gmtime((int(input())+6)*3600+(int(input())+51)*60)))