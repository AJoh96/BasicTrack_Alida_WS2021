# All work and no play makes Jack a dull boy
# 1. store each word in a separate variable, then print out the sentence on one line using print
a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
i = "dull"
j = "boy"

print(a + b + c + d + e + f + g + h + i + j)

# 2.Add parenthesis to the expression 6*1-2 to change its value from 4 to -6
z = 6 * (1 - 2)
print(z)

# 3.Place a comment before a line of code that previously worked and record what happens when you rerun the program
# SyntaxError:invalid syntax arises

# 4.Start the Python interpreter and enter bruce + 4 at the prompt. Give an error. --> Assign a value to bruce so
# that bruce +4 evaluates to 10 bruce +4 --> NameError
bruce = 6
q = bruce + 4
print(q)

'''
5. Formula A=P*(1+(r/n))**(n*t); replace the letters with something more human-readable 
+ calculate the interest for some varying amounts of money at realistic interest rates such as 1% and -0.05%
After this, ask the user for the value of some of these variables and do the calculation
'''
# A=P*(1+(r/n))**(n*t)
P = "initial investment"
r = "annual interest rate"
n = "number of times that the interest rate is paid out"
t = "years fir that interest rate is calculate for"
A1 = 1000 * (1 + (0.01 / 3)) ** (3 * 10)
print(A1)
A2 = 5000 * (1 + (0.01 / 3)) ** (3 * 10)
A3 = 1000 * (1 + (0.01 / 5)) ** (5 * 10)
A4 = 1000 * (1 + (-0.05 / 5)) ** (5 * 10)
print(A2, A3, A4)

# get information from user
# ask_user = int(input("How much money do you want to invest?"))
# do calculation
#calculated_answer = ask_user * (1 + (0.01 / 3)) ** (3 * 10)
# give output
# print(calculated_answer)
# get information from user2
# ask_user2 = float(input("To which annual nominal interest rate do you want to invest your $1,000?"))
# do calculation
# calculated_answer2 = 1000 * (1 + (ask_user2 / 3)) ** (3 * 10)
# give output
# print(calculated_answer2)

# 6. Evaluate the following numerical expressions in your head, then use the Python interpreter to check your results:
x=5%2
y=9%5
w=15%12
v=12%15
p=6%6
q=0%7
# s=7%0
print(x,y,w,v,p,q)
# with the last example python says "ZeroDivisionError: integer division or modulo by zero!

# 7. it is 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off?
# 2pm is 14 o'clock
h=(2+12+51)//24
print(h)
g=(2+12+51)%24
print("The alarm will go off at days", h, "and", g, "hours")
# Answer: The alarm goes off in 2 days in 17 hours.

# 8. Write a Python program to solve the general version of the above problem. Ask the user for the time now (in
# hours), and ask for the number of hours to wait. Your program should output what the time will be on the clock
# when the alarm goes off.
ask_user_time = float(input("What time is it now on the clock in hours?"))
print(ask_user_time)
#Extract the number from the string


ask_hours_waiting = float(input("In how many hours should the alarm goes off?"))
print(ask_hours_waiting)

# calculated time on the alarm: I only need to account for the "rest" hours not the days

calculated_answer_hours= (ask_user_time + ask_hours_waiting)
print(calculated_answer_hours)
x = calculated_answer_hours%24
print(x)

calculated_time_on_alarm= ask_user_time + x
print("The alarm goes off at")
print(calculated_time_on_alarm)




