#print("This is my first py file")

# a = int(input("Enter a number: "))
#
# if a > 5:
#     print("a is  biger than the number")
# else:
#     print("A is small")

# operand_1 = int(input("Enter the number: "))
# operand_2 = int(input("Enter the number: "))
#
# operator = input("Enter the operator ('+', '-') :")
#
# if operator == '+':
#     print(f"{operand_1} + {operand_2} = {operand_1+operand_2}")
# elif operator == '-':
#     print(f"{operand_1} + {operand_2} = {operand_1 + operand_2}")
# else:
#     print("Unknown operator")

# def add(x,y):
#     return x+y
#
# def square(z):
#     return z*z
#
# print(square(add(6,1)))

# Factorial using recurssion

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

print(fact(8))



