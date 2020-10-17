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
#
# #if we add range its gonna add up indexes together from 0 to the lenght of range
# for i in range(len(x)):
#     currentNumber = int(x[i])
#     total = total + currentNumber
#     print(i)
# print('Total is', total)


# Chapter 2 page 20
# Finger exercise: Write a program that asks the user to input 10 integers, and
# then prints the largest odd number that was entered. If no odd number was
# entered, it should print a message to that effect
#
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
#
# number = int(input('Enter an integer: '))
#
# for pwr in range(1, 6):
#     for r in range(abs(number) + 1):
#         if r ** pwr == abs(number):
#             if number < 0 and pwr % 2 != 0:
#                 r = -r
#                 print(r, 'to the power of', pwr, 'is', number)
#             elif number >= 0:
#                 print(r, 'to the power of', pwr, 'is', number)


# number = int(input("Write your integer "))
#
# #define a for loop for power in range of > 0 and < 6
# for power in range(1, 6):
#     # define another for loop for roots
#     for root in range(abs(number + 1)):
#         #define the power formula being equal to number
#         if root**power == abs(number):
#             #define if the root gonna be +or -
#             if number < 0 and power % 2 != 0:
#                 root = -root
#                 print(root, power)
#             elif number > 0:
#                 print(root, power)

# x = 25
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += step
#     numGuesses += 1
# print('numGuesses =', numGuesses)
# if abs(ans**2 - x) >= epsilon:
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square root of', x)


# number = float(input("write your number : "))
# epsilon = 0.01
# speed = epsilon ** 2
# numGuesses = 0
# ans = 0
#
# while abs(ans ** 2 - number) >= epsilon and ans <= number:
#     ans += speed
#     numGuesses += 1
# print("numGuesses is", numGuesses)
# if abs(ans ** 2 - number) >= epsilon:
#     print("failed")
# else:
#     print(ans, "is close to the root of", number)

# What would have to be changed to make the code in Figure
# 3.4 work for finding an approximation to the cube root of both negative and
# positive numbers? (Hint: think about changing low to ensure that the answer
# lies within the region being searched.)

# x = 0.5
# epsilon = 0.01
# numGuesses = 0
# low = 0
# high = max(1, x)
# ans = (high + low)/2
# while abs(ans**2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)


# number = float(input("Write your number : "))
# while number < 0:
#     print("Negative numbers have no square roots, please write a non-negative number")
#     number = float(input("Write your number : "))
#
# epsilon = 0.01
# guesses = 0
# low = 0
# high = max(1.0, number)
# ans = (high + low) / 2
#
# while abs(ans ** 2 - number) >= epsilon:
#
#     print("low , high and answer are :", low, ",", high, "and", ans)
#     guesses += 1
#     if ans ** 2 < number:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2
# print("number of guesses are :", guesses)
# print(ans, "is the closest number to the root of", number)


# Finger exercise: What would have to be changed to make the code in Figure
# 3.4 work for finding an approximation to the cube root of both negative and
# positive numbers? (Hint: think about changing low to ensure that the answer
# lies within the region being searched.)

# number = float(input("Write your number : "))
#
# epsilon = 0.01
# guesses = 0
# if number < 0:
#     low = min(number, -1)
# else:
#     low = 0
# high = max(1.0, number)
# ans = (high + low) / 2
#
# while abs(ans ** 3 - number) >= epsilon:
#     print("low , high and answer are :", low, ",", high, "and", ans)
#     guesses += 1
#     if ans ** 3 < number:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2
# print("number of guesses are :", guesses)
# print(ans, "is the closest number to the cube root of", number)


# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0

# Global variables
# epsilon = 0.01
# k = 24.0


# Newton-Rhapson
# print('--- Newton-Rhapson algorithm ---')
#
# guess = k/2.0
# iteration = 0
# while abs(guess*guess - k) >= epsilon:
#     guess = guess - (((guess ** 2) - k) / (2 * guess))
#     iteration += 1
# print("Number of guesses is", iteration)
# print('Square root of', k, 'is about', guess)
#
#
# # Binary search
# print('--- Binary search algorithm ---')
#
# guesses = 0
# low = 0
# high = max(1.0, k)
# ans = (high + low) / 2
# while abs(ans ** 2 - k) >= epsilon:
#     guesses += 1
#     if ans ** 2 < k:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2
# print("Number of guesses is", guesses)
# print('Square root of', k, 'is about', ans)


# # function defination
# def sahar(x, y):
#     if x < y:
#         print(x,"is smallest")
#     else:
#         print(x,"is biggest")
#
# sahar(33,5)


# def sahar(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
#
# print(sahar(3 + 4, 6))


# Finger exercise: Write a function isIn that accepts two strings as arguments
# and returns True if either string occurs anywhere in the other, and False
# otherwise. Hint: you might want to use the built-in str operation in.

# def isIn(str1, str2):
#     # check which one is the smallest
#     smallestString = min(str1, str2)
#     # check which one is the biggest
#     biggestString = max(str1, str2)
#     # see if the first letter of smallest string matches any letter of biggest one
#     for index in range(len(biggestString)):
#         # if there is a match
#         if smallestString[0] == biggestString[index]:
#             # check if the smallest string is equal to the sliced part of the biggest string
#             if smallestString == biggestString[index:index+len(smallestString)]:
#                 return True
#     # if the for loop finishes without returning, then it means there is no match
#     return False
#
# print(isIn("sahahar", "har"))


# def sahar(country="Iran"):
#     print("ı am from", country)


# def f(x):
#     y = 1
#     x = x + y
#     print('x =', x)
#     return x
#
#
#
# x = 3
# y = 2
# z = f(x)
# print('z =', z)
# print('x =', x)
# print('y =', y)


# def f(x):
#     def g():
#         x = 'abc'
#         print('x =', x)
#         return x
#     def h():
#         z = x
#         print('z =', z)
#
#     x = x + 1
#     print('x =', x)
#     h()
#     g()
#     print('x =', x)
#     return g
# x = 3
# z = f(x)
# print('x =', x)
# print('z =', z)
# z()


# def f():
#     print(x)
#
#
# def g():
#     x = 1
#     print(x)
#
# x = 3
# f()
# x = 3
# g()


# def getDouble(number):
#     """Assumes number is int or float,
#         Returns doubledNumber such that doubledNumber is two times the number
#     double(2) ---> 4"""
#     doubledNumber = number * 2
#     return doubledNumber
#
# print(double(2))
# help(double)


# def fib(x):
#     """Assumes x an int >= 0
#     Returns Fibonacci of x"""
#     global numFibCalls
#     numFibCalls += 1
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
#
# def testFib(n):
#     for i in range(n + 1):
#         global numFibCalls
#         numFibCalls = 0
#         print('fib of', i, '=', fib(i))
#         print('fib called', numFibCalls, 'times.')
#
# testFib(4)

# import os
# os.chdir('C:\\Users\\ekin\\Desktop')
#
# Sahar_file = open('myDocuments.txt', 'a')
# document = input('Enter a document: ')
# Sahar_file.writeLines('This document is ' + document + '\n')
# Sahar_file.close()
#
# Sahar_file = open('myDocuments.txt', 'r')
# content = Sahar_file.read()
# Sahar_file.close()
#
# print(content)

# nameHandle = open('sahari', 'w')
#
# nameHandle.write("sahar" + "\n")
# nameHandle.close()
#
# nameHandle = open('sahari', 'r')
# for i in nameHandle:
#     print(i)
# nameHandle.close()
#
# nameHandle.writelines(s)

# Number = int(input('write your num : '))
# while Number % 2 == 0:
#     Number = int(input('write your num : '))
# print("Good job!")


# mySum = 0
# for number in float(range(10.5)):
#     mySum += 1
# print(mySum)


# s = "abcdefgh"
# print(s[::])
#
# print(len(s))

# anLetters = "aeoiu"
# #create an input for user to type a word
# word = input("write a word for me to cheer up: ")
# #create an input for user to type enthusiastic level in number
# enthusiasmLevel = int(input("write your desired enthusiasm level from 1-10 : "))
#
#
#
# # create a for loop to iterate over the word
# for character in word:
#     # see if the character is anLetters
#     if character.lower() in anLetters:
#         # print it out
#         print("give me an "+character+" ! "+character)
#     else:
#         print("give me a", character, "!", character)
#
#
# for i in range(enthusiasmLevel):
#     print(word+"!")


# Number = int(input("write a number , you wanna know cube root of : "))
# for i in range(abs(Number) + 1):
#     if Number < 0:
#         positiveNumber = abs(Number)
#         if i ** 3 == positiveNumber:
#             print( "Cube root of ",Number, "is -",i)
#             break
#         else:
#             continue
#     else:
#         if i ** 3 == Number:
#             print("Cube root of " +str(Number)+ " is", i)
#             break
#         else:
#             continue
#     print(Number,"doesnt have a perfect cube")

# number = int(input("write a number , you wanna know cube root of : "))
# for root in range(abs(number)+1):
#     if root **3 == abs(number):
#         if number < 0:
#             root = -root
#         print("cube root of " + str(number) + " is " + str(root))
#         break
#     else:
#         if root >= abs(number):
#             print(number,"doesn't have any cube root")


# string = '6.00 is 6.0001 and 6.0002'
# newString = ""
# newString += string[-1] # '2'
# newString += string[0:7:3] # '6'
# newString += string[4::30] # ' '
# newString += string[13:10:-1] # '100'
# print(newString)


# a1 = "i rule mit"
# a2 = "mit u rock"
#
# for char_a1 in a1:
#     for char_a2 in a2:
#         if char_a1 == char_a2:
#             print("common letter is ", char_a1)
#             break


# def remainder(number):
#     return number % 2 == 0
#
# print(remainder(3))


# def funcA():
#     print("indide func A")
#
# def funcB(y):
#     print("inside fun B")
#     return y
#
# def funcC(z):
#     print("inside func C")
#     return z()
#
# print(funcA())
# print( 5 + funcB(2))
# print(funcC(funcA))


#
# def a(y):
#     x = 1
#     x += 1
#     print(x)
# x = 5
# a(x)
# print(x)


# def h(x):
#     x += 1
#
#
# x = 5
# h(x)
# print(x)

# big = 0
# for i in range(3):
#     number = int(input("write your number : "))
#     if number % 2 != 0 :
#         if number > big:
#             big = number
# if big == 0:
#     print("no odd number was written")
# else:
#     print(big)


# def rootFinder():
#     number = int(input("write your number: "))
#     positiveNumber = abs(number)
#     for power in range(1,6):
#         for root in range(positiveNumber):
#             if root ** power == positiveNumber:
#                 if number < 0:
#                     root = - root
#                 return print(root,"to the power of",power,"equals to:",number)
#     print(number,"doesnt have any root in range of 1 to 6")
#
#
# rootFinder()
#
# epsilon = 0.01
# step = epsilon * 2
# ans = 0
# guess = 0
# number = int(input("write your number : "))
# while number < 0:
#     number = int(input("write your number : "))
# # assert number > 0, 'Negative number entered'
# while ans ** 2 <= number and number - epsilon > ans and ans < number:
#     ans += step
#     guess += 1
# print(ans)
# print(guess)
#
#
# epsilon = 0.01
# guess = 0
# number = int(input("write your number : "))
# maxGuess = max(number, 1)
# minGuess = min(0, number)
# ans = (maxGuess + minGuess) / 2
# while abs(ans ** 3 - number) >= epsilon:
#     guess += 1
#     if ans ** 3 < number:
#         minGuess = ans
#     else:
#         maxGuess = ans
#     ans = (maxGuess + minGuess) / 2
# print(ans)
# print(guess)

# sahar = ()
# for i in range(1, 20):
#     if i % 2 == 0:
#         sahar += (i,)

# print(sahar)


# total = 0
# a = ()
# for i in range(0, 11):
#     if i % 2 == 0:
#         a += (i,)
#         total += i
# print(a)
# print(total)


# def get_even_numbers(n1, n2):
#     even_numbers = ()
#     total = 0
#     for i in range(n1, n2):
#         if i % 2 == 0:
#             even_numbers += (i,)
#     for i in even_numbers:
#         total += i
#     return total
#
# print(get_even_numbers(0,11))

# sahar, y, ekin = 1, 1567, "hello"
# print(sahar, y, ekin)


# def findExtremeDivisors(n1, n2):
#     minVal, maxVal = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             if minVal is None or i < minVal:
#                 minVal = i
#                 print("minval is", minVal)
#             if maxVal is None or i > maxVal:
#                 maxVal = i
#                 print("maxval is", maxVal)
#
#     return (minVal, maxVal)
#
# minDivisor, maxDivisor = findExtremeDivisors(10, 20)
# print(minDivisor, maxDivisor)
#
#
#
# #Easier way
# def find_common_divisors(n1, n2):
#     result = ()
#     for i in range(2, min(n1, n2) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             result += (i,)
#     minCommon = min(result)
#     maxCommon = max(result)
#     return minCommon, maxCommon
#
# print(find_common_divisors(10, 50))

#
# s = [1, 123, 4.67, "hello world"]
# for i in s:
#     print(i)


# sahar = ["my name", "is"]
# ekin = ["sahari", "mahari"]
# love = [sahar, ekin]
# life = [sahar, ekin]
# print("love is", love)
# print("life is", life)
# print(id(sahar), id(ekin))
# sahar.extend("sahariri")
# print(sahar)
# for u in love:
#     print("love contains", u)
#     print("which contains ")
#     for e in u:
#         print(e)


# a = [1, 2, 3, 4]
# b = [1, 2, 5, 6]
# def removeDups(a, b):
#     """Assumes that L1 and L2 are lists.
#     Removes any element from L1 that also occurs in L2"""
#     for i in a[:]:
#         print(a.index(i))
#         if i in b:
#             a.remove(i)
#     return a
# print(removeDups(a, b))


# a = [ x ** 2 for x in range(0, 7) ]
# print(a)

# a = ("a", 1.23, "hello")
# s = [1, 123, 4.67, "hello world"]
# h = "   my    "
# s = "sahar loves to play for quiddich"
# print(s.split(" "))


#
# def applyToEach(L, f):
#     """Assumes L is a list, f a function
#     Mutates L by replacing each element, e, of L by f(e)"""
#     for i in range(len(L)):
#         L[i] = f(L[i])
#
# L = [1, -2, 3.33]
# print('L =', L)
# print('Apply abs to each element of L.')
# applyToEach(L, abs)
# print('L =', L)
# print('Apply int to each element of', L)
# applyToEach(L, int)
# print('L =', L)


#
# a = [1, 4, 6]
# b = [-3, 6, 89.9]
# print(list(map(abs, b)))

# flight1 = (111, "1st of October")
# flight2 = (112, "2nd of October")
# monthNumbers = {flight1:"12pm", flight2:'1pm'}
# print(monthNumbers[flight1])


#
# print("the third month is :", monthNumbers[3])
# dist = abs(monthNumbers['Jan'] - monthNumbers['Apr'])
# print(monthNumbers[1],"and",monthNumbers[4],"are",dist,"months apart")
# print(monthNumbers.values())
#
# months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5}
# keys = []
# for e in months:
#     keys.append(e)
# print(keys)
# keys.sort() # works with Python 2

# keys = [e for e in monthNumbers] # list comprehension
#
#
# EtoF = {'bread': 'pain', 'wine': 'vin', 'with': 'avec', 'I': 'Je',
#         'eat': 'mange', 'drink': 'bois', 'John': 'Jean',
#         'friends': 'amis', 'and': 'et', 'of': 'du', 'red': 'rouge'}
# FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with', 'Je': 'I',
#         'mange': 'eat', 'bois': 'drink', 'Jean': 'John',
#         'amis': 'friends', 'et': 'and', 'du': 'of', 'rouge': 'red'}
# dicts = {'English to French': EtoF, 'French to English': FtoE}
# 
#
# def translateWord(word, dictionary):
#
#     if word in dictionary.keys():
#         return dictionary[word]
#     elif word != "":
#         return '"' + word + '"'
#     return word
#
#
# print(translateWord("pain", FtoE))
#
#
# def translate(phrase, direction):
#     UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     LCLetters = 'abcdefghijklmnopqrstuvwxyz'
#     letters = UCLetters + LCLetters
#     dictionary = direction
#     translation = ''
#     word = ''
#     for c in phrase:
#         if c in letters:
#             word += c
#         else:
#             translation += translateWord(word, dictionary) + c
#             word = ''
#     return translation
#
#
# print(translate('Je bois du vin rouge.', FtoE))
# print(translate('I drink good red wine, with red meat.', EtoF))


# example for tuple inside the tuple
# bigT = ((1, "a"), (2, "a"), (3, "c"))
#
#
# def add(aTupleName):
#     numbers = ()
#     words = ()
#     for i in aTupleName:
#         if i[0] not in numbers:
#             numbers += (i[0],)
#         if i[1] not in words:
#             words += (i[1],)
#     result = (min(numbers), min(words))
#     return result
# print(add(bigT))


# a = "helloWorld"
# print(list(a))
# print(a.split("e"))
#
# b = ["p", "b", "c"]
# k = b.sort()
# print(sorted(b))
# print(b)
# print("".join(b))
# print('_'.join(b))
# print('yello'.join(b))


# recursion


# def factR(n):
#     if n == 1:
#         return n
#     else:
#         return n * factR(n - 1)

#
#
# fibonnaci
# def fib(n):
#     if n == 0 or n == 1:
#         print(n)
#         return 1
#     else:
#         print(n)
#         return fib(n - 1) + fib(n - 2)
# print(fib(3))
#
#
# def char(s):
#     s = s.lower()
#     letters = ''
#     for c in s:
#         if c in 'abcdefghijklmnopqrstuvwxyz':
#             letters = letters + c
#     return letters
#
# def isPal(s):
#     if len(s) <= 1:
#         return True
#     else:
#         print(s)
#         return s[0] == s[-1] and isPal(s[1:-1])
# print(isPal(char("madam")))


# lyrics = ["baby", "baby", "I", "love", "love", "much", "much", "much", "baby"]
# def frequency(poem):
#     myDict = {}
#     for word in poem:
#         if word not in myDict.keys():
#             myDict[word] = 1
#         else:
#             myDict[word] += 1
#     return myDict
#
# def most_common(song):
#     most_repeated_words = {}
#     frequency_dicts = frequency(song)
#     most_repeated_value = max(frequency_dicts.values())
#     for j in frequency_dicts:
#         if frequency_dicts[j] == most_repeated_value:
#             most_repeated_words[j] = most_repeated_value
#     return most_repeated_words
#
#
# def xTimes(music, minTimes):
#     theList = {}
#     for i in music:
#         if music[i] >= minTimes:
#             theList[i] = music[i]
#     return theList
#
# print(xTimes(frequency(lyrics), 2))


#newfibonnaci
empty = {}
myList = {1:1, 2:2, 3:3}


def fib(n, annbgh):
    if n in annbgh:
        return annbgh[n]
    else:
        answer = fib(n - 1, annbgh) + fib(n - 2, annbgh)
        return answer


print(fib(4, myList))



