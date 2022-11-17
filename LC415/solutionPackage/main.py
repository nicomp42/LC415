from Solution import *

mySolution = Solution ()

'''
result = mySolution.addStrings("123", "456")
print(results)

#let's make one that fails 
result = mySolution.addStrings("aaa", "bbb")
print(results)

result = mySolution.addStrings("-123", "456")
print(results)

result = mySolution.addStrings("123.5", "456.1")
print(results)

result = mySolution.addStrings("123a", "456b")
print(results)

result = mySolution.addStrings("123!", "456@")
print(results)
'''

#let's build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111" , "2000"]
expectedResult = ["579", "1110", "3000"]
#Write a loop to try all the test cases
for i in range(0, 3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else:
        print("test FAILED. Change professions")
        print("expected result", expectedResult[i], "actual result", result)
    
    
    
    
    
