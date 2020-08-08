# hi = "hello"
# name = "sahar"
# print(hi)
# greeting = hi +" "+ name
# print(greeting)
# silly = (" "+name)*3
# print(silly)
# x = 1
# y = 3

# userName = input("Enter your name: ")
# print(5 * userName)

# number = input('Enter a number: ')
# if int(number) > 100 and int(number) % 2 == 0:
#     print('Your number is higher than 100 and dividable by 2')
# else:
#     print('Bruhh')
#

# x = float(input("type the x : "))
# y = float(input("type the y : "))
#
# if  x == y :
#     print ("x and y are equal so the result is 1")
# elif y and x== 0 :
#     print("0 is not dividable")
# else: print(int(x/y))
# x = int(input("write your number: "))
# if x % 2 == 0:
#     print(x, "is even")
# else:
#     print(str(x) + " is odd")


# x = int(input("write your number: "))
# if x % 3 == 0 :
#     if x % 2 == 0 :
#         print(str(x) + " is dividable by 2 and 3")
#     else: print("devidable by only 3")
# elif x % 2 == 0 :
#     print(x, "dividable by only 2")


# Write a program that examines three variables—x, y, and z—
# and prints the largest odd number among them. If none of them are odd, it
# should print a message to that effect.

# x = 22
# y = 344
# z = 3
#
# # check if x is odd
# if x % 2 != 0:
#     # x is odd; check if y is odd
#     if y % 2 != 0:
#         # x and y are odd; check if z is odd
#         if z % 2 != 0:
#             # x, y, z are odd, check which is largest
#             if x > y and x > z:
#                 print(str(x))
#             elif y > x and y > z:
#                 print(str(y))
#             else:
#                 print(str(z))
#         else:
#             # x and y are odd, z is not odd; check which is larger
#             if x > y:
#                 print(str(x))
#             else:
#                 print(str(y))
#     # x is odd, y is not odd, check if z is odd
#     elif z % 2 != 0:
#         # if x and z are odd; check which is larger
#         if x > z:
#             print(str(x))
#         else:
#             print(str(z))
#     else:
#         print(str(x))
# # x is not odd; check if y is odd
# elif y % 2 != 0:
#     # if y is odd; check if z is odd
#     if z % 2 != 0:
#         # y and z are both odd, check which is larger
#         if y > z:
#             print(str(y))
#         else:
#             print(str(z))
#     # y is odd, z is not odd
#     else:
#         print(str(y))
# # x, y are not odd, check if z is odd
# else:
#     if z % 2 != 0:
#         print(str(z))
#     # none of them are odd
#     else:
#         print('none of them are odd')


# x = 10
# y = 290
# z = 1


# #check if x is an odd number
# if x % 2 != 0:
#     #check if y is an odd number
#     if y % 2 != 0:
#         #check if z is an odd number
#         if z % 2 != 0 :
#             #all of them are odd numbers
#             #check if x is bigger than the others
#             if x > z and x > y:
#                 print(x)
#             elif y > z and y > x:
#                 print(y)
#             else:
#                 print(z)
#         #check which one is bigger y or x
#         elif y > x :
#             print(y)
#         else:
#             print(x)
#     #check if z is an odd number
#     elif z % 2 != 0 :
#         if x > z :
#             print(x)
#         else:
#             print(z)
#     else:
#         print(x)
# elif y % 2 != 0 :
#     if z % 2 != 0:
#         if y > z :
#             print(y)
#         else:
#             print(z)
#     else:
#         print(y)
# else :
#     if z % 2 != 0 :
#         print(z)
#     else:
#         print("none of them are odd")


# x = 6
# ans = 0
# iteration = x
#
# while iteration != 0:
#     ans = ans + x
#     iteration = iteration - 1
# print(x, "*", x, "=", ans)


# largest = None
#
# for i in range(0, 10):
#     number = int(input('Enter a number: '))
#     if largest is None:
#         if number % 2 != 0:
#             largest = number
#     else:
#         if number % 2 != 0 and number > largest:
#             largest = number
#
# if largest is None:
#     print("You haven't typed any odd numbers.")
# else:
#     print('Largest odd number is ' + str(largest))


# listOfTemps = [15, 17, 20, -5, 30, 2, 9]
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# day = 0
#
# for temperature in listOfTemps:
#     if day == 4:
#         print('It is', days[day], 'suckers, I am outta here.')
#         break
#     print('Temperature was', temperature, 'degree Celcius on', days[day])
#     day = day + 1
#     if temperature <= 15:
#         print('It was cold.')
#     else:
#         print('It was hot.')


# myString = "1.23, 2.4, 3.123"
# total = 0
# index = 0
# tracker = 0
#
# for character in myString:
#     if character == ',' or index == len(myString) - 1:
#         total = total + float(myString[tracker:index])
#         tracker = index + 2
#     index = index + 1
# print(total)


# x = "987654321"
# total = 0
#
# for char in x:
#     total = total + int(char)
#     print('The loop variable in this iteration is', char)
# print('Total is', total)
#
# for i in range(len(x)):
#     currentNumber = int(x[i])
#     total = total + currentNumber
# print('Total is', total)


# Chapter 2 page 20
# Finger exercise: Write a program that asks the user to input 10 integers, and
# then prints the largest odd number that was entered. If no odd number was
# entered, it should print a message to that effect

# largestOdd = None
# for i in range(5):
#     number = int(input("Write your number: "))
#     if largestOdd is None:
#         if number % 2 != 0:
#             largestOdd = number
#     else:
#         if number % 2 != 0 and number > largestOdd:
#             largestOdd = number
#
# if largestOdd is None:
#     print("You haven't entered an odd number.")
# else:
#     print('Largest odd number is', largestOdd)


# Chapter 2 page 20
# Finger exercise: Write a program that asks the user to input 5 integers, and
# then prints the smallest even number that was entered. If no even number was
# entered, it should print a message to that effect


# smallestEven = None
# # set 5 iterations first
# for i in range(5):
#     # ask for input from user and assign them to number
#     number = int(input("Write your even number: "))
#     # the first time user types in an even number, there can't be any comparison so see if it's the first even number
#     if smallestEven is None:
#         # see if the written number is even
#         if number % 2 == 0:
#             # assign the smallestEven to number
#             smallestEven = number
#     # if it is not the first time, compare the smallestEven to the new number and see which one is smaller
#     elif number % 2 == 0 and number < smallestEven:
#         smallestEven = number
#
#
# # if user didn't type in any even number for all rounds, give a message to that effect
# if smallestEven is None:
#     print("You haven't typed any even numbers.")
# # print out the final result of the smallest even number
# else:
#     print("The smallest even number is " + str(smallestEven) + ".")


# page 25
# sum the digits in the string denoted by the literal '123456789' and prints the total.
# a = "12345"
# total = None
#
# for i in a:
#     if total is None:
#         total = int(i)
#     else:
#         total = total + int(i)
#         print(total)


# Finger exercise: Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
# the sum of the numbers in s.
#
# total = 0
# tracker = 0
# s = "1.23, 2.4, 3.123"
#
# for i in range(len(s)):
#     # realize how to get the float number
#     if s[i] == ",":
#         number = float(s[tracker:i])
#         tracker = i + 2
#         # add numbers with each other
#         total = total + number
#     elif i == len(s) - 1:
#         number = float(s[tracker:i])
#         # add numbers with each other
#         total = total + number
#
# # get the final print
# print(total)


# total = 0
# tracker = 0
# s = "1.23, 2.4, 3.123"
#
# for i in range(len(s)):
#     if s[i] == ",":
#         number = float(s[tracker:i])
#         tracker = i + 2
#         total = total + number
#     elif i == len(s) - 1:
#         number = float(s[tracker:])
#         total = total + number
# print(total)


# calculate the biggest number
# biggestNum = None
# tracker = 0
# s = "-1.23, -2.4, -3.123"
#
# for i in range(len(s)):
#     if biggestNum is None:
#         if s[i] == ",":
#             number = float(s[tracker:i])
#             tracker = i + 2
#             biggestNum = number
#     elif s[i] == ",":
#         number = float(s[tracker:i])
#         tracker = i + 2
#         if number > biggestNum:
#             biggestNum = number
#     else:
#         if i == len(s) - 1:
#             number = float(s[tracker:])
#             if number > biggestNum:
#                 biggestNum = number
# print(biggestNum)


# calculate the minus
# s = "-1.23, -2.4, -3.123"
# tracker = 0
# total = None
#
# for i in range(len(s)):
#     if total is None:
#         if s[i] == ",":
#             number = float(s[tracker:i])
#             tracker = i + 2
#             total = number
#     elif s[i] == ",":
#         number = float(s[tracker:i])
#         tracker = i + 2
#         total = total - number
#     else:
#         if i == len(s) - 1:
#             number = float(s[tracker:])
#             total = total - number
# print(total)


# Finger exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

number = int(input('Enter an integer: '))

for pwr in range(1, 6):
    for r in range(abs(number) + 1):
        if r ** pwr == abs(number):
            if number < 0 and pwr % 2 != 0:
                r = -r
                print(r, 'to the power of', pwr, 'is', number)
            elif number >= 0:
                print(r, 'to the power of', pwr, 'is', number)


