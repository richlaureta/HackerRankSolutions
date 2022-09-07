
grid = ['abc', 'ade', 'efg']

lists = []


for i in range(0, len(grid)):
    comparisons = sorted(grid[i])
    lists.append(comparisons)

lists0 = []
for i in range(0, len(lists)):
    lists1 = []
    for j in range(0, len(lists)):
        lists1.append(lists[j][i])
    lists0.append(lists1)

lists1 = []
for i in range(0, len(lists0)):
    compare = sorted(lists0[i])
    lists1.append(compare)

if lists0 != lists1:
    print('NO')
elif lists0 == lists1:
    print('YES')