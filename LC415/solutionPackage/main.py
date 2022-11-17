# main.py

from Solution import *
# This is our entry point to test the code
# We will test the solution class
#for Leetcode problem 415


mysolution = Solution()

'''
result = mysolution.addStrings("123", "456")
print(result) 

result = mysolution.addStrings("aaa", "bbb")
print(result)

result = mysolution.addStrings("-123", "456")
print(result)

result = mysolution.addStrings("123.5", "456.1")
print(result)

result = mysolution.addStrings("123a", "456b")
print(result)
'''
# LEts build a list of test cases and expected results

num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expectedResult = [579, 1110, 3000]
# Write a loop to try all test cases
for i in range (0,3):
    result = mysolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else:
        print("test Failed. Change profession")
        print("expected result", expectedResult[i], "actual result", result)
    