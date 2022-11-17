'''
main.py
'''
from Solution import *
    #This is our entry point to the test code
    # We will test the Solution class
    # for LeetCode problem 415
    #The solution has been provided by...
     #instantiate an object of type solution

mySolution = Solution()
'''
result = mySolution.addstrings("123", "456")
print(results)

result = mySolution.addStrings("aaa", "bbb")
print(results)
result = mySolution.addStrings("-123", "456")
print(result) 

result = mySolution.addStrings("123.5", "456.1")
print(result)

result = mySolution.addStrings("123a", "456b")
print(results)
'''

 
    # lets build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000" ]
expectedResult = ["579", "1110", "3000"]
# write a loop to try all the test cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else:
        print("test FAILED. Change professions.")
        print("expected result", expectedResult[i], "actual result", expectedResult[i])