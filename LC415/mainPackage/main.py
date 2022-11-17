#main py
from solutionPackage.Solution import *

#test the Solution made by prof nicholson
#leetcode problem 415
#instantiate the class and all that
mySolution = Solution()

'''
result = mySolution.addStrings("123", "456")
print(result)#expect 579
#test 1 worked, lets do one that fails.
result = mySolution.addStrings("abc", "def")
print(result) #expect idk
result = mySolution.addStrings("-123", "456")
print(result) #expect 333
result = mySolution.addStrings("1d23.5", "45h6.1")
print(result) #probably gonna be random digits again
result = mySolution.addStrings("9v%!oa7", "1129y56#@!!")
print(result) #probably more digits
'''
#lets make a list of test cases and expected results

num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expectedresult = [579, 1110, 3000]
#could also put quotes around each entry in the expected results list.

for i in range(0,3):
    result = mySolution.addStrings(num1[i],num2[i])
    if result == str(expectedresult[i]): #make it a string
        print("test passed")
    else:
        print("test failed...")
        print("expected result",expectedresult[i], " actual results...", result)



