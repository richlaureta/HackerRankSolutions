grid = ['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']
total = []
for i in range(0, len(grid)):
    sum = 0
    for element in grid[i]:
        sum += ord(element)
    total.append(sum)

for i in range(0, len(total)):
    if i == len(total) - 1:
        print('YES')
        break

    if total[i] > total[i + 1]:
        print('NO')
    elif total[i] >= total[i + 1]:
        continue