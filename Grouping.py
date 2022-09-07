array = [1, 2, 4, 5, 6, 9] 

sorted1 = sorted(array)

indexPosition = 0
count = 1
for i in range(len(sorted1)):
    if sorted1[i] - sorted1[indexPosition] > 3:
        difference = sorted1[i] - sorted1[indexPosition] 
        
        count += 1
        indexPosition = i
        i = indexPosition

print(count)