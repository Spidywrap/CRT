'''
1) Print n natural numbers


n = int(input())
for i in range(1,n+1):
    print(i,end=' ')
'''
'''
2) print n even numbers

n = int(input())
for i in range(1,n+1):
    print(2*i,end=' ')
    '''
'''
3) print n odd numbers

n = int(input())
for i in range(1,n+1,2):
    print(i,end=' ')
    '''
'''
4) Print n Fibonacci numbers

n = int(input())
a,b = 0,1
for i in range(n):
    print(a,end=' ')
    a,b = b , a+b
    '''
'''
5) Print multiplication table of a given number

n = int(input())
for i in range(1,11):
    print(n,"x",i,"=",n*i)
'''
'''
6) Print the square of first n natural numbers

n = int(input())
for i in range(1,n+1):
    print(i*i,end = ' ')
    '''
'''
7) Print alternative series of n natural numbers such as 1 -2 +3 -4 +5 -6 ....

n = int(input())
for i in range(1,n+1):
    if i % 2 == 0:
        print(-i,end=' ')
    else:
        print(i,end=' ')
        '''
'''
8) Print serier like 1 2 4 7 11 16 22 .... n terms

n = int(input())
a = 1
sum = 0
for i in range(1,n+1):
    sum = sum + (i - 1)
    a = 1 + sum
    print(a,end=' ')
    '''
'''
9) Print series like 1, 2, 6, 24, 120, 720 .... n terms

n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
    print(fact,end=' ')
    '''