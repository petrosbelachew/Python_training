"""
Fill out the functions to calculate the area and circumference of a circle.
Print the result to the user.
"""

PI = 3.14159


def area(r):
   return(PI * r **2)


def circumference(r):
     2 * PI * r


def surfacearea():
     4 * PI*r*r


def Volume():
   (4 / 3) * (PI * r * r * r)


radius = input("Circle radius: ")

print(f'Area: {area(radius)}')  # <-- Call the area function and print the result
print(f'Circumference: {circumference(r)}')  # <-- Call the circumference function and print
print(f'SurfaceArea: {surfacearea(r)}')  # <-- Call the Surfacearea function and print the result
print(f'Volume: {Volume(r)}')  # <-- Call the Volume function and print
