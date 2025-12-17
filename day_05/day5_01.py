import math

def basic_operations():
    print("Square Root of 25:", math.sqrt(25))
    print("Power (2^3):", math.pow(2, 3))
    print("Factorial of 5:", math.factorial(5))

def trigonometry():
    angle = math.radians(30)
    print("Sin(30°):", math.sin(angle))
    print("Cos(30°):", math.cos(angle))
    print("Tan(30°):", math.tan(angle))

def logarithmic_operations():
    print("Log base 10 of 100:", math.log10(100))
    print("Natural log of 10:", math.log(10))

def constants():
    print("Value of Pi:", math.pi)
    print("Value of e:", math.e)

if __name__ == "__main__":
    basic_operations()
    trigonometry()
    logarithmic_operations()
    constants()
import os

def current_directory():
    print("Current Working Directory:", os.getcwd())

def list_files():
    print("Files in current directory:")
    for file in os.listdir():
        print(file)

def create_and_remove_directory():
    dir_name = "test_directory"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created")
    else:
        print(f"Directory '{dir_name}' already exists")

    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed")

def environment_variables():
    print("PATH Environment Variable:")
    print(os.environ.get("PATH"))

if __name__ == "__main__":
    current_directory()
    list_files()
    create_and_remove_directory()
    environment_variables()
