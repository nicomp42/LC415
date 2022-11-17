'''
Name: Roger Poduska
email: poduskrd@mail.uc.edu
Assignment: LC415
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: In class work 11/17/22
Citations: N/a
Anything else that's relevant: N/a
'''

from solutionPackage.Solution import *

#Entry point to test code
#Testing solution class for LeetCode problem 415

#Instantiate object of type Solution
mySolution = Solution()
'''
result = mySolution.addStrings("123", "456")
print(result) #Expected answer 579

#Expected to fail or is a restraint of LC problem
result = mySolution.addStrings("aaa", "bbb")
print(result)

result = mySolution.addStrings("-123", "456")
print(result) 

result = mySolution.addStrings("123.5", "456.1")
print(result) #Expected answer 579.6

result = mySolution.addStrings("123a", "456b")
print(result)

result = mySolution.addStrings("123!", "456@")
print(result) 
'''

#Building list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]
#Loop through test cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if(expectedResult[i] == result):
        print("test passed ", result)
    else:
        print("Test failed.")
        print("expected ", type(expectedResult[i]), " actual ", type(result))

