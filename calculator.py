def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

print("Select an operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

select = int(input("Select operation (1-4): "))

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if select == 1:
    print(n1, "+", n2, "=", addition(n1, n2))
elif select == 2:
    print(n1, "-", n2, "=", subtraction(n1, n2))
elif select == 3:
    print(n1, "*", n2, "=", multiplication(n1, n2))
elif select == 4:
    print(n1, "/", n2, "=", division(n1, n2))
else:
    print("Invalid input")