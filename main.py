# Addition of two numbers using input statement
a = input("Enter fist value :")
b = input("Enter second value :")
add = int(a) + int(b)
print("sum of tow numbers:", add)

# subtraction of two numbers using input statement
a = input("Enter fist value :")
b = input("Enter second value :")
sub = int(a) - int(b)
print("subtraction of tow numbers:", sub)

# Multiplication of two numbers using input statement
a = input("Enter fist value :")
b = input("Enter second value :")
Mul = int(a) * int(b)
print("Multiplication of tow numbers:", Mul)

# Division of two numbers using input statement
a = input("Enter fist value :")
b = input("Enter second value :")
Div = int(a) / int(b)
print("Division of tow numbers:", Div)

# calculator for two numbers using input statements and if condition
def add(a, b):
    return a + b


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y
#  input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

if choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

if choice == '3':
    print(num1, "*", num2, "=", mul(num1, num2))

if choice == '4':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Invalid input")
