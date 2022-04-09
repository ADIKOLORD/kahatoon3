# Problem 1
"""
# l = [1, 2, 4, 5, 6]
l = [-1, -2, -6]
for i in range(1, max(l)):
    if i not in l:
        print(i)
        break
else:
    print(1)
"""

# Problem 2
"""
user = input('Enter your text: ')
upper, lower = 0, 0
for i in user:
    if i == i.upper():
        upper += 1
    else:
        lower += 1
one_per = 100 / (upper + lower)
print(f'Upper - {one_per * upper}\nLower - {one_per * lower}')
"""

# Problem 3

l = [5, 7, 9, -1, 2]

# [1, 2, 3]
# [3, 1, 2] # 1
# [2, 3, 1] # 2
# [2, 3, 1] # 3

for i in range(len(l)):
    if l[i] > 0:
        f = l[-1]
        l.pop(-1)
        l.insert(0, f)
    else:
        s = l[0]
        l.pop(0)
        l.append(s)
print(l)

# Problem ?
