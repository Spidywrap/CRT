#1. Running sum of 1D list
'''
arr1 = [1,2,3,4]
res = []
s = 0
for ele in arr1:
    s = s + ele 
    res.append(s)
print(res)
'''
#Another way
'''
nums = [1,2,3,4]
ans = []
for i in range(1,len(nums)+1):
    ans.append(sum(nums[:i]))
print(ans)
'''
#Another way
'''
nums = [1,2,3,4]
res1 = [sum(nums[:i]) for i in range(1,len(nums)+1)]
print(res1)
'''
#Leetcode 217
'''
nums = [1,2,3,1]
l = set(nums)
if nums == l:
    print('False')
else:
    print('True')
    '''
#Leetcode 1672 RIchest Customer Wealth
accounts = [[1,2,3],
            [3,2,1]]
max_sum = sum(accounts[0])
for i in range(len(accounts)):
    if sum(accounts[i]) > max_sum:
        max_sum = sum(accounts[i])
print(max_sum)
