#You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3
#(a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the
#starting day number, and the length of your stay, and it will tell you the name of day of the week you will return
#on.
#creating a list
week_days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]

start_day = int(input("On which day do you start your holidays?, in Day_number"))
print(start_day)
length_of_stay = int(input("How many days do you stay?, in total numbers"))
print(length_of_stay)

#returning_day = start_day + (length_of_stay%7)
#print("You will return on the day number", returning_day, ".")
print("You will return on the day", week_days[(start_day + length_of_stay) % len(week_days)], ".")
