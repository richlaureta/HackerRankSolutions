numbers = [4,5,6,7]

for i in range(len(numbers)):
    
    arrays = []
    for j in range(len(numbers)):
        if j == len(numbers) - 1:
            break

        sum_mod = (numbers[j] + numbers[j+1]) % 10
        arrays.append(sum_mod)
        
    numbers = arrays
    print
    
    if(len(numbers) == 2):
        encrypted = str(numbers[0]) + str(numbers[1])
        break

print(encrypted)