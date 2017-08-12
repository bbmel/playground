def reverseArr():
    N = input('Enter the number of elements: ')
    elems = input('Enter ' + N + " elements: ")
    arr = elems.split(' ')
    arr = list(map(int, arr))
    revArr = arr[::-1]
    for i in range(len(revArr)):
        print(revArr[i], end=" "),


reverseArr()