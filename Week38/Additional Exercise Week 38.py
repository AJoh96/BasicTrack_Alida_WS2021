#write a program to calculate the time it takes to get somewhere using
#different modes of travel

#time in minutes for 1 km
walking = 12
biking= 3
driving_car= 1

ask_distance = int(input("How long is the distance in km?"))
calculate_walking = walking * ask_distance
calculate_biking = biking * ask_distance
calclate_car = driving_car * ask_distance

print("With a car it would take", calclate_car, "minutes.","With a bike it would take (min):",calculate_biking, "Going would take following minutes:" ,calculate_walking)

