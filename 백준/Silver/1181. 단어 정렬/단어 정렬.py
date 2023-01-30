import sys
import operator
n = int(sys.stdin.readline())
dict= {}
for i in range(n) :
    a = sys.stdin.readline()
    if a not in dict :
        dict[a] = len(a)
dict1 = sorted(dict.items(), key=operator.itemgetter(1))
dict1.sort(key=lambda x: (x[1], x[0]))
for key, vaule in dict1:
    print(key,end="")
