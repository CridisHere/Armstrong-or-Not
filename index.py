#WAP in Python to check whether a number is Armstrong or not.
# A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
# For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.
num = int(input("Enter a number: "))

def isArmstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

isArmstrong(num)