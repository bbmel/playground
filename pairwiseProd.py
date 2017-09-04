#python3

numOfNums = input()
nums = input().split()
newNums = []
for elem in nums:
    elem = int(elem)
    newNums.append(elem)
sortedNums = sorted(newNums)
arrLength = len(sortedNums)
maxProduct = sortedNums[arrLength - 1] * sortedNums[arrLength - 2]
print(maxProduct)



