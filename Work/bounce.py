# bounce.py
#
# Exercise 1.5

bounce = 1
height_of_bounce = 60 # Meters

while bounce < 11:
    print (bounce, round(height_of_bounce))
    bounce = bounce + 1
    height_of_bounce = height_of_bounce * 0.6
