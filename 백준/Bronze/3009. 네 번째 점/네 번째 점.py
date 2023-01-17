x_loc = []
y_loc = []

for _ in range(3):
    x, y = map(int, input().split())
    x_loc.append(x)
    y_loc.append(y)
for i in range(3):
    if x_loc.count(x_loc[i]) == 1:
        x4 = x_loc[i]
    if y_loc.count(y_loc[i]) == 1:
        y4 = y_loc[i]
print(x4, y4)