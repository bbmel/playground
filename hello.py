def reverseArr():
    print('Enter the number of elements: ')
    N = input()
    print('Enter ' + N + ' elements: ')
    elems = input()
    arr = elems.split(' ')
    arr = list(map(int, arr))
    revArr = arr[::-1]
    for i in range(len(revArr)):
        print(revArr[i], end=" "),


reverseArr()