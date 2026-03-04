#1. Pascal Triangle
'''
n = int(input())
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num,end=' ')
        num = num * (i-j)//(j+1)
    print()
    '''
#2. Butterfly Pattern
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*',end = '')
    print()
for i in range(n):
    for j in range(n - i):
        print('*', end='')
    print()