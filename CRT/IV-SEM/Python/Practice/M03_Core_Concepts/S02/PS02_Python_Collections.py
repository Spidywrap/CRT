'''
set:
1. Unordered collection of unique elements
2. Mutable (can be modified after creation)
3. No duplicate elements allowed
4. Can contain elements of different data types
5. Supports mathematical set operations like union, intersection, difference, etc.
6. Defined using curly braces {} or the set() constructor
7. not indexed (cannot access elements by position)
s = {1,True,10,12.67,10}
'''
'''
A = {1,2,3}
B = {3,4,5}
A.add(4)
B.update({6,7})
print(A,B)
#removing elements
A.pop() #removes and returns an arbitrary element from the set
B.remove(4) #removes a specific element from the set
print(A,B)
'''
'''
t = (10,23,50,10,67,69)
t2 = ("venkata","rama","jyothieswar")

print(t[0])
print(t[-1])
print(t + t2)
print(t,t2)
print(t*5)
print(t[1:4])
print(t[:5])
print(t[:-1])
del t
'''
d = {'a':'sai'}
print(d)
d2 = dict(a='sai',b='venkata',c='jyothieswar')
print(d2)
print(d2['a'])
print(d2.get('b'))
print(d2.keys())
print(d2.values()) 