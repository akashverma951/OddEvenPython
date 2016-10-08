#program to identify the even/odd state of given number
#function to print OddEven of given number

def even(number):
    if number == 0:
        return True
    return odd(number - 1)

def odd(number):
    if number == 0:
        return False
    return even(number - 1)

def isEven(number):
    if even(number):
        print("Number is even")
    else:
        print("Number is odd")

number = int(input("enter the number"))

isEven(number)
