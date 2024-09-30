#Write a program to fill in a letter template given below with name and date

"""
Dear <Name>,
you are selected
<Date>
"""
import datetime
name = input("Enter your name: ")
print(f"Dear {name},\nyou are selected\n{datetime.date.today()}")