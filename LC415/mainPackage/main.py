
from solutionPackage.Solution import *







mySolution = Solution()
result = mySolution.addStrings('123', '456')
print(result)

result = mySolution.addStrings('aaa','bbb')














# Let's build a list of test cases and expected results
num1 = ["123", "999", "1000"]
num2 = ["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]
# Write a loop
for i in range(0, 3):
    result = mySolution.addStrings(num1[i],num2[i])
    if result == expectedResult[i]:
        print('Test passed')
    else:
        print("test FAILED")
        print("expected result", expectedResult[i], "actual result", result)