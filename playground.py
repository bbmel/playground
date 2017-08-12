def double_char(str):
  for i in str:
      print(i * 2, end = "")


def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i] + str[i + 1] == 'hi':
            count += 1
    print(count)


