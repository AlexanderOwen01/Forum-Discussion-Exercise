# number 1
import math
# r = float(input("please input the radius of the circle: "))
# area = math.pi * r**2
# print(area)

# number 2
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(last_name,first_name)

# number 3
# color_list =('Red','Green','White','Black')
# print(color_list[0], color_list[3])

# number 4
# n = int(input("please input an integer"))
# x = (n)
# y = (n**2)
# z = (n**3)
# total = x+y+z
# print(int(total))

# number 5
# volume = (4/3) * math.pi * (6**3)
# print(volume)

# number 6
# given_number = float(input("enter your number: "))
# if given_number < 17:
#     print(given_number - 17)
# else:
#     print((given_number-17)**2)

# number 7
# first_number = float(input("please input the first number: "))
# second_number = float(input("please input the second number: "))
# third_number = float(input("please input the third number: "))
# if first_number == second_number == third_number:
#     print((first_number+second_number+third_number)*3)
# else:
#     print(first_number+second_number+third_number)

# number 8
# x = float(input("please insert any number: "))
# if (x % 2) == 0:
#     print("the number is even")
# else:
#     print("the number is odd")

# number 9
# letter = input("please input any letter: ")
# vowel = ["a","i","u","e","o"]
# if letter.casefold() in vowel:
#     print("the letter is a vowel")
# else:
#     print("the letter is not a vowel")

# number 10
# values = ["10", "20", "30", "40", "50"]
# user_input = input("please input a random number: ")
# if user_input in values:
#     print("unlucky bro, its in the list of values")
# else:
#     print("youre lucky this time dude, it's not in the list of values")

# number 11
# import matplotlib.pyplot as plt
# int_list = [1,13,6,78,9,2,5,34,32,134,4,10,78,5,234,90]
# plot.hist(int_list)
# can't seem to find the python packages

# number 12
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#  815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#  958,743, 527]
#
# for x in numbers:
#     if x % 2 == 0:
#         print(x)

# numbers 13
# base = float(input("please input the base of the trianle: "))
# height = float(input("please input the height of the triangle: "))
# area = (base/2) * height
# print("The area of the triangle is ", area)

# number 14
# x = int(input("please input the first number:"))
# y = int(input("please input the second number:"))
# if x < y:
#     x+y == y+x
# lcm = x
# while lcm % y != 0:
#     lcm +=x
# print(f"The two numbers are: {lcm}")

# number 15
# x = int(input("Insert number x: "))
# y = int(input("Insert number y: "))
# z = int(input("Insert number z: "))
# if x == y or x == z or y == z:
#     print("The sum is zero.")
# else:
#     total = x + y + z
#     print(total)

# number 16
# x = int(input("please input the first integer: "))
# y = int(input("please input the second integer: "))
# result = (x + y) * (x + y)
# print("the result is:", result)

# number 17
# amt = int(input("please input the amount of initial investment:"))
# roi = float(input("please input the rate of interest:"))
# years = int(input("please input the years:"))
# result = amt * ((1+(roi/100))**years)
# print(result)

# number 18
# x1 = int(input("please input the first point x: "))
# y1 = int(input("please input the first point y: "))
# x2 = int(input("please input the second point x: "))
# y2 = int(input("please input the second point y: "))
#
# x = ((x1 - x2)**2)
# y = ((y1 - y2)**2)
# z = ((x + y)**(1/2))
# print("the distance betweent the two points is: ", z)

# number 19
# x = int(input("please input a positive integer: "))
# y = int(x * (x+1)/2)
# print(y)

# number 20
# x = eval(input("please input height in feet her: "))
# y = eval(input("please input height in inches: "))
# x_cm = x * 30.25
# y_cm = y * 2.5
# height = x_cm+y_cm
# print("your height in centimeters is: ", height)

# number 21
# x = eval(input("please input the length of side A: "))
# y = eval(input("please input the length of side B: "))
# z = ((x**2 + y**2)**0.5)
# print("The hypotenuse of the triangle is: ", z)

# number 22
# weight = float(input("Please input your weight in kg: "))
# height = float(input("Please input your height in m: "))
# bmi = ((weight)/(height)**2)
# print(bmi)

# number 23
# x1 = int(input("please input the value of x1:"))
# y1 = int(input("please input the value of y1:"))
# x2 = int(input("please input the value of x2:"))
# y2 = int(input("please input the value of y2:"))
#
# result = ((x1+x2 //2)), (y1+y2//2)
# print("The midpoint of the two points is: ", result)

# number 24
# list=[]
# for x in range(2000, 3200):
#     if (x % 7 == 0) and (x % 5 !=0):
#         list.append(str(x))
# print (",".join(list))