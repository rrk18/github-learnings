print("Hello world")
def add(*args):
    return sum(args)

print(add(34,12,56,78,89,12,34))

# def division():
#     try:
#         num1=float(input("Enter first number: "))
#         num2=float(input("Enter 2nd number: "))
#         result=num1/num2
#     except TypeError:
#         print(f"You have not entered int or float value {TypeError}")
#     except ZeroDivisionError:
#         print(f"Any number")

