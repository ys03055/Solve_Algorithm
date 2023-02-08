a = list(input())
dict = {}
for i in a :
    i1 = i.lower()
    if i1 not in dict :
        dict[i1] = 1
    else :
        dict[i1] +=1
result = [k for k,v in dict.items() if max(dict.values())==v]
if len(result) > 1:
    print("?")
else :
    print(result[0].upper())
