
import math
import os
import random
import re
import sys
def recursion(total):
    conversion = int(total)
    print(type(conversion))
    if (int(total)) < 10:
        return int(total)
    for element in total:
        addition += int(element)
    
    recursion(str(addition))
    
def superDigit(n, k):
    # Write your code here
    p = k * (n)
    total = 0
    for element in p:
        total += int(element)
    
    if total < 10:
        return total
    
    result = recursion(str(total))
    
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
