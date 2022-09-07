a = [1,2,3,4,5,6,7]
a.sort()
n = len(a)
mid = int((n + 1)/2) - 1
a[mid], a[n-1] = a[n-1], a[mid]

st = mid + 1 #4
ed = n - 2 #5

while(st < ed):
    a[st], a[ed] = a[ed], a[st]
    st = st + 1
    ed = ed - 1

for i in range (n):
    print(a[i], end =' ')
 
