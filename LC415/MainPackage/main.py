'''
Created on Nov 17, 2022

@author: bluej
'''
# Entry point to test code. We will test the solution class for Leetcode 415. The solution has been provided by Bill Nicholson

from solutionPackage.Solution import *

# Instantiate an object of type solution

mySolution = Solution()
'''
result = mySolution.addStrings("123", "456")
print(result)

# Do a test that we know will fail.
result = mySolution.addStrings("AAA", "BBB")
print(result)

# Try a negative number
result = mySolution.addStrings("-123", "456")
print(result)

# Try float numbers
result = mySolution.addStrings("123.5", "456.1")
print(result)

# Try letters and numbers
result = mySolution.addStrings("123a", "456b")
print(result)

# Try special characters and numbers
result = mySolution.addStrings("123!", "456@")
print(result)
'''
# Let's build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expected_results = ["579", "1110", "3000"]
# Write a loop to try all cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expected_results[i]:
        print("test passed")
    else:
        print("test FAILED. Change professions.")
        print("expected result", expected_results[i], type(expected_results[i]), "actual result", result, type(result))
        