'''
Name: Joshua Earley
email: earleyja@mail.uc.edu
Assignment: Assignment 13
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: 
Citations:
Anything else that's relevant:
'''
# main.py
# this is our entry point to test the code
# we will test the solution Class
# for LeetCode problem 415
# the solution has been provided by professor Bill

from solutionPackage.Solution import * 

mySolution = Solution() 
'''
result = mySolution.addStrings("123", "456")
print(result) # we expect 123 + 456 = 579
# Do a test that we know is going to fail

result = mySolution.addStrings("aaa", "bbb")
print(result) # we do not know what to expect here 

# what if we try a negative number? 
result = mySolution.addStrings("-123", "456")
print(result)

result = mySolution.addStrings("123.5", "456.1")
print(result) # we expect 123.5+456.1=579.6

result = mySolution.addStrings("123a", "456b")
print(result) #we do not know what to expect

result = mySolution.addStrings("123!", "456@")
print(result)#we do not know what to expect
'''
# lets build a list of test cases and expected results 
num1 =["123", "999", "1000"]
num2 =["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]
# write a loop to try all the test cases 
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else:
        print("test FAILED.")
        print("expected result", expectedResult[i], "actual result", result)