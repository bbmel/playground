#python3

def fib(n):
    fibList = []
    fibList.append(0)
    fibList.append(1)
    for i in range(2, n + 1):
        n = (fibList[i - 1] + fibList[i - 2]) % 10
        fibList.append(n)
    return(fibList[len(fibList) - 1])

n = int(input())
print(fib(n))


