"""
# Print all natural numbers from 1 to n using while loop
n = int(input('enter the value of n:'))
print('natural numbers from 1 to n ')
i = 1
while n >= i:
    print(i)
    i += 1
---------------------------------------------------------
# Write a python pgm to print all natural numbers in reverse(from n to 1)
n = int(input('Enter a number:'))
print('Desired output as given natural no. in reverse order:')
i = 1
while n >= i:
    print(n)
    n = n-1
-------------------------------------------------------------------
# Write a program to print all alphabates from a to z---using while loop
i = 65
while i < 91:
    print(chr(i))
    i = i +1
---------------------------------------------------------
# WAPP to print all even numbers between 1 to 100---using while loop
n = 1
while n < 100:
    n = n + 1
    n % 2 == 0
    print(n)
----------------------------------------------------------------
# WAPP to print all odd numbers between 1 to 100
n = 1
while n < 100:
    n % 2 != 0
    print(n)
    n = n+1

Second approach
n = 0
while n < 100:
    n = n + 1
    n % 2 != 0
    print(n)
------------------------------------------------------------------
#WAPP to find sum of all natural numbers between 1 to n
n = int(input('Enter the value of n:'))
sum = 0
i = 0
while i < n:
    i = i + 1
    sum = sum + i
print(sum)
-----------------------------------
#WAPP to find sum of all even numbers between 1 to n
n = int(input('Enter the value of n:'))
sum = 0
i = 0
while i < n:
    i =i + 1
    if i % 2 == 0:
        sum = sum + i
        print(sum)
------------------------------------
Second approach:
n = int(input('Enter the range of n:'))
i = 0
while i < n:
    i = i + 1
    if i % 2 == 0:
        sum = i *(i-1)/2
    print(sum)
--------------------------------------------------------
# WAPP to find sum of all odd numbers between 1 to n
n = int(input('Enter the value of n:'))
sum1 = 0
for i in range(1,n):
    if i % 2 != 0:
        sum1 = sum1 + i
        print(sum1)
--------------------------------------------------
# WAPP to print multiplication table for any number.take user input
n = int(input('Enter a number with your choice:'))
for i in range (1,11):
    table = i * n
    print(table)
-------------------------------------------------------------
# WAPP to count a number of digits in a number
n = str(input('Enter the any number:'))
print(len(n))
---------------
n = input('Enter a number:')
print(str(len(n)))
------------------------------------------------------------
# WAPP to find first  and last digits of a  number.
n = input('Enter a number:')
if (n.isnumeric):
    for i in range(len(n)):
        if i == 0:
            print(f'first no: is {n[0]}')
        elif i == len(n)-1:
                print(f'last no:{n[-1]}')
else:
    print('Enter a valid input')
-------------------------------------------------------------
# WAPP to find sum of the first and last digits of a number
n = input('Enter a number:')
reverse = n[::-1]
n = int(n)
reverse = int(reverse)

first_digit = reverse % 10
last_digit = n % 10

total_sum = first_digit + last_digit
print('Sum of first and last digits',total_sum)
---------------------------------------------------------
# WAPP to swap first and last digits of a number
n = input('Enter a number:')
first_digit = n[0]
print(first_digit)
last_digit = n[-1]
print(last_digit)
a = n[1:-1]
print(a)
b = last_digit + a +first_digit
print(b)
----------------------------------------------------------
# WAPP to calculate sum of all digits of a number
n = int(input('Enter the number:'))
n1 = str(n)
sum = 0
for digits in str(n1):
    sum += int(digits)
print(sum)
=================================
n = input('Enter a number:')
b = int(n)
a = len(n)
print(a)
sum = 0
for i in range(a):
    sum = sum + (b % 10)
    b = b // 10
print(sum)
-----------------------------------------------
# WAPP to calculate product of digits of a number.
n = input('Enter a number:')
n1 = str(n)
#sum = 0
mul = 1
for i in str(n1):
    mul = mul * int(i)
    #sum = sum + n2
print(mul)
-----------------------------------------------------------------
#WAPP enter a number and print its reverse.
a = input('enter a number:')
reverse = a[::-1]
print(reverse)
--------------------------------------------------------------
#WAPP to check whether a number is palindrome or not.
n = input('Enter a number:')
n1 = str(n)
if n == n1[::-1]:
    print('Given number is palindrom.')
else:
    print('Given number is not a palindrom.')
-----------------------------------------------------------------
#WAPP to find frequency of each digits in a given number
n = input('Enter any number:')
print(n.count('1'))
print(n.count('2'))
print(n.count('3'))
print(n.count('4'))
print(n.count('5'))
print(n.count('6'))
print(n.count('7'))
print(n.count('8'))
print(n.count('9'))
print(n.count('0'))
-----------------------------------------------------------------
#WAPP to enter a digits and print it in words.
n = int(input('Enter a digits from 0 to 9:'))
print('Entered digits in the words:')
if n == 0 :
    print('Zero')
elif n == 1:
    print('One')
elif n == 2:
    print('Two')
elif n == 3:
    print('Three')
elif n == 4:
    print('Four')
elif n == 5:
    print('Five')
elif n == 6:
    print('Six')
elif n == 7:
    print('Seven')
elif n == 8:
    print('Eight')
elif n == 9:
    print('Nine')
else:
    print('Please entered a valid integer number.')
-------------------------------------------------------------------------------
# WAPP to find power of a number using for loop.
n = int(input('Enter a number:'))
result = 1
for i in range(11):
    result = result * n
    print(result)
----------------------------------------------------------------------------------
# WAPP to calculate factorial of a number.
n = int(input('Enter a number:'))
if n < 0:
    print('Factorial of negative number is not available.')
elif n == 0:
    print('Factorial of zero is 1')
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print('Factorial of given Number is =', fact)
----------------------------------------------------------------------------
# WAPP to find HCF(GCD) of two numbers.
num1 = int(input('Enter the first Number :'))
num2 = int(input('Enter the another Number:'))
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1,max(num1,num2)):
    if ((num1 % i == 0) and (num2 % i == 0)):
        hcf = i
print('HCF of given Numbers is:', hcf)
--------------------------------------------------------------------------------
# WAPP to find LCM of two numbers.
num1 = int(input('First Number:'))
num2 = int(input('Second Number:'))
if num1 > num2:
    greater = num1
else:
    greater = num2
while(True):
    if ((greater % num1) == 0 and (greater % num2) == 0):
        lcm = greater
        break
    greater += 1
print('L.C.M. of given two numbers is:', lcm)
--------------------------------------------------------------------------
# WAPP to check whether a number is prime number or not.
flag = False
num = int(input('Enter a Number:'))
if num <= 0:
    print('Negative number and zero is not allowed,only positive numbers are allowed.')
elif num == 1:
    print('1 is not a prime number.')
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, 'is not a prime number.')
    else:
        print(num, 'is a prime number.')
========================================================================
num = int(input('Enter a Number:'))
if num <= 0:
    print('Negative number and zero is not allowed,only positive numbers are allowed.')
elif num == 1:
    print('1 is not a prime number.')
elif num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, 'is not a prime number.')
            break
    else:
        print(num, 'is a prime number.')
--------------------------------------------------------------------------------------------
# WAPP to print all prime numbers between 1 to n.
lower = 1
upper = int(input('Enter your number:'))
print('The Prime Numbers in between 1 to', upper,'are:')
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, 'is not a prime number.') # make this line comment to fetch only prime numbers list
                break
        else:
            print(num, 'is a prime number.')
------------------------------------------------------------------------------------------
# WAPP to to find sum all prime numbers between 1 to n.
lower = 1
upper = int(input('Enter a range of numbers:'))
sum = 0
print('Here is a sum of all prime numbers:')
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                #print(num ,'not a prime number')
                break
        else:
            #print(num,'is a prime number')
            sum = sum + num
            print(sum)
---------------------------------------------------------------------------------
# WAPP to check whether a number is a Armstrong number or not.
# Armstrong Numbers: e.g. 153
153 = (1*1*1)+(5*5*5)+(3*3*3)
================
num = int(input('Enter any number:'))
n = str(num)
sum = 0
for digit in n :
    print(digit)
    i = int(digit)
    cube = i*i*i
    sum = sum + cube
    if sum == num:
        print(num, 'is a Armstrong Number')
        break
else:
    print(num,'is not a Armstrong Number')
-----------------------------------------------------------------------
# WAPP to print Fibonacci series up to n terms.
a = 0
b = 1
n = int(input('Enter the value of n:'))
if n < 0:
    print('You have entered wrong value,please enter the positive number.')
elif n == 0:
    n = a
elif n == 1:
    n = b
else:
    for i in range(0,n):
        c = a + b
        a = b
        b = c
        print(c)
---------------------------------------------------------------------------
# WAPP to print given star patterns
*
* *
* * *
* * * *
* * * * *

for i in range(1,6):
    print(' *'* i)
--------------------------------------------------------------------------------
# WAPP to print the given number patterns
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

for i in range(1,6):
    for j in range(i):
        print(i,end= " ")
    print(' ')
===========================
for i in range(1,6):
    for j in range(i):
        print(chr(64+i),end= " ")
    print('')
-----------------------------------------------------------
"""

