'''#1. count number of digits in a number
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)'''
'''#2. sum of digits in a number
n = int(input())
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
print(sum)'''
'''#3. counting even and odd digits in a number
n = int(input())
even_count = 0
odd_count = 0
while n > 0:
    x = n % 10
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n = n // 10
print(even_count, odd_count)'''
#4. sum of the digits until only one digit is left
n = int(input())
str(n)
