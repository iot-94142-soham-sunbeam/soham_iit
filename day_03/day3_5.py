def greet(name, message="Good Morning"):
    print(message, name)

# Function calls
greet("Alice")
greet("Bob", "Hello")
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

# Calling using keyword arguments
student_info(course="Python", name="Rahul", age=20)
def add(a, b):
    return a + b

def operate(func, x, y):
    return func(x, y)

# Passing add function to operate
result = operate(add, 10, 5)
print("Result:", result)
