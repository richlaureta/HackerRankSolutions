petrolpumps = [[1, 5], [10, 3], [3, 4]]
petrol = 0
index = -1
for i in range(len(petrolpumps)):
    petrol += petrolpumps[i][0] - petrolpumps[i][1] 
    if petrol < 0:
        index = i + 1
        petrol = 0

print(index)