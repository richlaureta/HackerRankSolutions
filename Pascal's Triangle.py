n = 10
initial = [[1], [1, 1]] # 121, 1331
initial1 = [[1]]
if n == 1: 
    print(initial1)
elif n == 2:
    print(initial)
elif n > 2:
    startIndex = 1
    for i in range(n-2):
        triangle = []
        triangle.append(1)
        for j in range(0, len(initial[startIndex]) - 1):
            
            sum = initial[startIndex][j] + initial[startIndex][j + 1]
            triangle.append(sum)
        
        startIndex += 1 
        
        triangle.append(1)
        initial.append(triangle)
    
    print(initial)
