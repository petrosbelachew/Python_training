"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""

from math import pi

def area(r):
   return pi * r ** 2


def circumference(r):
     return 2 * PI * r


def surfacearea():
    return   4 * PI*r*r


def Volume():
    return (4 / 3) * (PI * r * r * r)


radius = float(input("Circle radius: "))

print(f'Area: {area(radius)}')  # <-- Call the area function and print the result
print(f'Circumference: {circumference(radius)}')  # <-- Call the circumference function and print
print(f'SurfaceArea: {surfacearea(radius)}')  # <-- Call the Surfacearea function and print the result
print(f'Volume: {Volume(radius}')  # <-- Call the Volume function and print
