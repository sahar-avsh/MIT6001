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


largest = None

for i in range(0, 10):
    number = int(input('Enter a number: '))
    if largest is None:
        if number % 2 != 0:
            largest = number
    else:
        if number % 2 != 0 and number > largest:
            largest = number

if largest is None:
    print("You haven't typed any odd numbers.")
else:
    print('Largest odd number is ' + str(largest))























