# Write a program which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse.
# (Hint: x ** 0.5 will return the square root.)
# Pythagoras!

triangle_side1 = float(input("How long is the side 1?"))
triangle_side2 = float(input("How long is the side 2?"))
# calculate the hypotenuse
hypotenuse = ((triangle_side2**2)+(triangle_side2**2))**0.5
print("The lenght is", hypotenuse, ".")
