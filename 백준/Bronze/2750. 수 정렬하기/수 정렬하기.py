t = int(input())
num_list = []
for i in range(t):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])