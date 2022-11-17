# Main.py

from solutionPackage.Solution import Solution


mySolution = Solution()
'''
result = mySolution.addStrings('132', '140')
print(result)


result2 = mySolution.addStrings('aaa','bbb')
print(result2)


result3 = mySolution.addStrings('-123','456')
print(result3)

x = mySolution.addStrings('a','b')
print(x)
'''

num1 = ['123','999','1000']
num2 = ['456','111','2000']
expectedResult = [579,1110,3000]

for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == str(expectedResult[i]):
        print('Test Passed')
    else:
        print('Test Failed')
        print('expected', expectedResult[i], 'actual', result[i])



