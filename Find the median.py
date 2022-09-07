
def findMedian(arr):
    arr.sort()
    if len(arr) == 1:
        return arr[0]
    elif len(arr) % 2 == 0:
        med = (int((len(arr)/2)))
        median = int((int(arr[med-1] + arr[med]))/2)
        return median
    elif len(arr) % 2 != 0:
        median = int((len(arr)/2) + 0.5)
        return arr[median -1]

if __name__ == '__main__':
    arr = [9,6,8,7,5]

    print(findMedian(arr))