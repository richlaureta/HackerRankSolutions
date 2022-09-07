
k = 2
s = 'middle-Outz'

mod_effort = k % 26

l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
C = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lnew = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Cnew = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

dictl = {'a': 0,'b': 1,'c': 2, 'd': 3,'e': 4,'f': 5,'g': 6,'h': 7, 'i': 8,'j': 9,'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,'u':20,'v':21,'w':22,'x':23,'y': 24,'z': 25}

dictC = {'A': 0,'B': 1,'C': 2, 'D': 3,'E': 4,'F': 5,'G': 6,'H': 7, 'I': 8,'J': 9,'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
'P': 15,'Q': 16,'R': 17,'S': 18,'T': 19,'U':20,'V':21,'W':22,'X':23,'Y': 24,'Z': 25}

endIndex =  mod_effort - 1 
startIndex = 25 - mod_effort
start = 0

for i in range(startIndex + 1, 26):
    lnew[i] = l[start]
    Cnew[i] = C[start]
    start += 1

start1 = mod_effort

for i in range(0, startIndex + 1):
    lnew[i] = l[start1]
    Cnew[i] = C[start1]
    start1 += 1
together = []
for element in s:
    if element.isalpha():
        if element.islower():
            
            together.append(lnew[dictl[element]])
        elif element.isupper():
            together.append(Cnew[dictC[element]])
    else:
        together.append(element)

togetherness = ''

for element in together:
    togetherness += element

print(togetherness)