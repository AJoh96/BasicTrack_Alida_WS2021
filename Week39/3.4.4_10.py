import math

a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)
#1.
a_string = "We like Python's turtles"
for line in range(1000):
  result = a_string * 999
  print(result)
# 3.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
for month in months:
        print("One of the months of the year is", month)


# 4.
for number in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    print(number, "\t", number**2)
