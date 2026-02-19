import sys

N = int(sys.stdin.readline().rstrip())
lst1 = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
lst2 = list(map(int, sys.stdin.readline().rstrip().split()))


dict_lst1 = {}

for _ in range(len(lst1)):
    if len(lst1) >= 0:
        if lst1[-1] in dict_lst1.keys():
            dict_lst1[lst1.pop()] += 1
        else:
            dict_lst1[lst1.pop()] = 1

for i in lst2:
    if i in dict_lst1.keys():
        print(dict_lst1[i], end=' ')
    else:
        print(0, end=' ')