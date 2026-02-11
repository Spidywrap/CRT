'''
1) write a python code for the factorial of a number.

n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
'''
'''
2) write a python code to check wheather a number is Armstrong or not.

n = int(input())
sum = 0
temp = n
order = len(str(n))
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
    if n == sum:
        print("Armstrong number")
        break
    else:
        continue
else:
    print("Not an Armstrong number")

'''
'''
3) write a python code to check whether a number is Prime or not.

n = int(input())
is_prime = True
if n <= 1:
    is_prime = False
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
'''
'''
4) Print prime numbers in a given range.

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
            '''
'''
5) Monotonic of an array.

arr = list(map(int,input().split()))
increasing = True
decreasing = True
for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
        increasing = False
    if arr[i] > arr[i-1]:
        decreasing = False
if increasing:
    print("Monotonic Increasing")
elif decreasing:
    print("Monotonic Decreasing")
else:
    print("Not Monotonic")
    '''
'''
6) Reverse integer.

n = int(input())
sign = 1
if n < 0:
    sign = -1
    n = -n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
rev = rev * sign
if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print(rev)
'''
'''
7) convert a roman numeral to an integer.

roman = input().upper()
values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
total = 0
prev = 0
for ch in reversed(roman):
    if values[ch] < prev:
        total -= values[ch]
    else:
        total += values[ch]
        prev = values[ch]
print(total)
'''
'''
8) happy number.
'''
n = int(input())
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    sum_sq = 0
    while n > 0:
        digit = n % 10
        sum_sq += digit ** 2
        n //= 10
    n = sum_sq
if n == 1:  
    print("Happy number")
else:
    print("Not a happy number")