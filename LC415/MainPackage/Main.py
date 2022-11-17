#Main.py

from solutionPackage.Solution import *
#This is our entry point 
#We will test the solution class for LeetCode Problem 415  
#The solution has been provided by Bill Delmer 
#Instantiate an object of type Solution


mySolution = Solution()
"""
result = mySolution.addStrings("123", "456") #We expect 123+456 =579
print(result)
#Do a test that we know is going to fail

#Letters
result = mySolution.addStrings("aaa", "bbb") #The strings need to be numbers. THIS DOES NOT WORK
print(result)

#Negative Numbers
result = mySolution.addStrings("-123", "456") #CANNOT BE NEGATIVE. THIS DOES NOT WORK
print(result)

#Floating Numbers
result = mySolution.addStrings("123.5", "456.5") #CANNOT BE FLOATING. THIS DOES NOT WORK
print(result)

#Mixed Letters and Numbers
result = mySolution.addStrings("123a", "456b") #CANNOT BE MIXED. THIS DOES NOT WORK
print(result)
"""

#Lets build a list of test cases and expected results 
num1 = ["123","999","1000"]
num2 = ["456","111","2000" ]
expectedResult = ["579","1110","3000"]
#Write a loop to try all the test cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("Test Pass")
    else:
        print("test FAILED. Change Profession")
        print("expected result", expectedResult[i], "; actual result", result)