#main.py

from solutionPackage.Solution import *

# Entry point, for LeetCode problem 415. Solution has been provided.

mySolution = Solution()
result = mySolution.addStrings('123', '456')
print(result)

# Do a test that we know will fail
'''
result = mySolution.addStrings('aaa', 'bbb')
print(result)

result = mySolution.addStrings('-123', '456')
print(result)

result = mySolution.addStrings('123.5', '456.1')
print(result)

result = mySolution.addStrings('12x3.5', '4s56.1')
print(result)
'''
# Let's build a list of test cases and expected results
num1 = ['123', '999', '1000']
num2 = ['456', '111', '2000']
expectedResult = [579, 1100, 3000]

# Write a loop to try all test cases

for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print('test passed')
    else:
        print('test failed. CHANGE PROFESSIONS.')
        print('expected result', expectedResult[i], 'actual result', result)
    