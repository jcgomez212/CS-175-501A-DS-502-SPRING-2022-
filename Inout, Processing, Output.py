#Input, Processing, Output.py
#Juliana Gomez, s1321300
#CS-175/501A, DS-502
#Spring 2022

#1 print_sum.py
list1 = range(1,11)
sum1 = sum(list1)
print('1.',sum1)
#
print(' ')
#2 print_product.py
from functools import reduce
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nums_product = reduce((lambda x, y: x * y), nums)
print('2.',nums_product)
#
print(' ')
#3 account_balance.py
balance = 1000.00
interest = 0.05
amount = balance * interest
balance1 = amount + balance
print("3. The amount after 1 year is ", balance1)
balance2 = (balance1 * interest)+ balance1
print("   The amount after 2 years is ", balance2)
balance3 = (balance2 * interest) + balance2
print("   The amount after 3 years is ", balance3)
#
print(' ')
#4 name_printer1.py
print("4.     +-----------+")
print("       |  Juliana  |")
print("       +-----------+")
#
print(' ')
#5 math_ops.py
a = int(input("5. Enter first number: "))
b = int(input("   Enter second number: "))
sum = a + b
difference = a - b
product = a * b
average = (a + b) / 2
distance = abs(difference)
if a > b:
    print(f'{a} is a maximum number')
else:
    print(f'{b} is a maximum number')
if a < b:
    print(f'{a} is a minimum number')
else:
    print(f'{b} is a minimum number') 
print("The sum is",sum,','\
      "the difference is",difference,','\
      "the product is ",product,','\
      "the average is ",average,','\
      "and the distance is ",distance)
#
print(' ')
#6 f_to_c_temp.py
#formula: T(°C) = (T(°F) - 32) × 5/9
kb_input = input('6. Enter a temperature in fahrenheit: ')
f_temp = float(kb_input)
c_temp = (f_temp - 32) * (5 / 9)
print('The temperature in celcius: ', c_temp)




