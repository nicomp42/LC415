# main.py

from Solution import *

# this is our entry point to our code
# leetcode

mySolution = Solution()

'''
result = mySolution.addStrings("123", "456", "789")
print(result)

result = mySolution.addStrings ("aaa", "bbb")
print(result)
result = mySolution.addStrings ("-123", "456")
print(result)
result = mySolution.addStrings ("123.5", "456.1")
print(result)

result = mySolution.addStrings ("123a", "456a")
print(result)
'''
# Let's build a list of test cases and expected results 
num1= ["123", "999", "1000"]
num2= ["456", "111", "2000"]
expectedResult = [579, 1110, 3000]

# Write a loop to try all the test cases 
for i in num1(0,3):
    result = mySolution.addStrings(i, num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else:
        print("test FAILED.")
        print("expected result", "expectedResult[i]", "actual result", result)
