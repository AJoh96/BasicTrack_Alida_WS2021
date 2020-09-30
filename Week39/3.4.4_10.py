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

#4c. Write a loop that adds all the numbers from the list into a variable called total. You should set the total
#variable to have the value 0 before you start adding them up, and print the value in total after the loop
#has completed.

total = 0
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = sum(numbers)
print(total)


for number in [12, 10, 32, 3, 66, 17, 42, 99, 20]:
    product = number * number
    print(product)
