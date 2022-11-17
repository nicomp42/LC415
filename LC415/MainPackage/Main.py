# Main.py

from solutionPackage.Solution import *

# This is our entry point to the test code
# We will test the Solution class
# for LeetCode problem 415
# The solution has been provided by Professor Nicholson

# instantiate an object of type Solution
mySolution = Solution()

'''
result = mySolution.addStrings("123", "456")
print(result)  # we expect 123+456=579

# Do a test that we know is going to fail
result = mySolution.addStrings("aaa", "bbb")
print(result)  # we don't know what to expect

# What if we try a negative number?
result = mySolution.addStrings("-123", "456")
print(result)  # we don't know what to expect

# What if we try floats?
result = mySolution.addStrings("123.5", "456.1")
print(result)  # we expect 123.5+456.1=579.6

# What if we add a letter?
result = mySolution.addStrings("123a", "456b")
print(result)  # we don't know what to expect
'''

# Let's build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]
# Write a loop to try all the test cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else:
        print("test failed")
        print("expected result", expectedResult[i], "; actual result", result)