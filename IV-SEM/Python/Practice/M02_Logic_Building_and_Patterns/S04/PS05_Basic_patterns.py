'''
1. Square Star Pattern

n = int(input())
for i in range(n):
    for k in range(n):
        print('*', end=' ')
    print()
'''
'''
2. Right Angled Triangle

n = int(input())
for i in range(n):
    for j in range(i + 1):
        print('*',end=' ')
    print()
    '''
'''
3. Inverted Right Angled triangle

n = int(input())
for i in range(n):
    for j in range(n - i):
        print('*', end=' ')
    print()
    '''
'''
4. Number Pyramid

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print(j + 1, end=' ')
    print()
    '''
'''
5. Repeated Number Pattern
'''
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(i + 1, end = ' ')
    print()