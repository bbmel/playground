#python3

def fib(n):
    fibList = []
    if n is 0 or n is 1:
        return(n)
    else:
        fibList.append(0)
        fibList.append(1)
        for i in range(2, n + 1):
            valAtIndex = fibList[i - 1] + fibList[i - 2]
            fibList.append(valAtIndex)
        return(fibList[n])

n = int(input())
print(fib(n))
