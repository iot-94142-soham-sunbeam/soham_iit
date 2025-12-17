
from geometry import area_circle, area_rectangle

# User input
choice = int(input("Choose an option:\n1. Area of Circle\n2. Area of Rectangle\nEnter choice: "))

if choice == 1:
    r = float(input("Enter radius of the circle: "))
    print("Area of Circle:", area_circle(r))

elif choice == 2:
    l = float(input("Enter length of the rectangle: "))
    w = float(input("Enter width of the rectangle: "))
    print("Area of Rectangle:", area_rectangle(l, w))

else:
    print("Invalid choice")

