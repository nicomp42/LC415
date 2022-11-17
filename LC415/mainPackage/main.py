#main.py

from solutionPackage.Solution import *
# This is our entry point to the test code
#We will test the solution class
#The solution has been provided by.......


# instantiate an object of type solution
mySolution = Solution()
'''
result = mySolution.addStrings("123", "456")
print(result)  # we expect to get 123 + 456= 579
#Do a test that will fail 
result = mySolution.addStrings("aaa", "bbb")
print(result)  # we do not know what to expect 
result = mySolution.addStrings("-123", "456")
print(result)  # we expect to get -123+456=333

result = mySolution.addStrings("123.5", "456.1")
print(result)  # we expect to get 123.5+456.1 =579.6

result = mySolution.addStrings("123a", "456b")
print(result)  # we expect to get 123a + 456b= 579ab
'''
# Lets build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]
#write a loop to try all the test cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else: 
        print("test Failed. Change professions.")
        print("expected result", expectedResult[i], " actual result", result)    