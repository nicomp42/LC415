'''
Created on Nov 17, 2022

@author: drewsexton
'''
from solutionPackage.Solution import Solution
#This is our entry point to the test code
#we will test the solution class for LeetCode problem 415

mysolution = Solution()

'''
mySolution = Solution()
result = mySolution.addStrings("123", "456")
print(result)

result = mySolution.addStrings("aaa", "bbb")
print(result)

result = mySolution.addStrings("123.5", "2.75")
print(result)
'''
#lets build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111","2000"]
expectedResult = ["579", "1110", "3000"]
for i in range(0,3):
    result = mysolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
            print("Test passed")
    else:
            print("Update your resume")
            print("expected result", expectedResult[i], "actual result", result)

