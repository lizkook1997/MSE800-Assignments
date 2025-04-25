# rectangle_area.py

# Define a square function
def square(x):
    return x * x

# Inputs: sides of a rectangle (can be negative to test abs)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Make sure the values are positive
length = abs(length)
width = abs(width)

# Calculate area
area = length * width

# Round the result to 2 decimal places
rounded_area = round(area, 2)

print(f"The area of the rectangle is: {rounded_area} square units")
