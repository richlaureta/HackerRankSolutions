lastIndex = len(s) - 1
    
def palindromeIndex:
    for i in range((lastIndex + 1)//2):
        if s[i] != s[lastIndex - i]:
            if s[i: lastIndex - i] == s[i: lastIndex - i][::-1]:
                return lastIndex - i
            elif s[i + 1: lastIndex + 1  - i] == s[i+ 1: lastIndex + 1 - i][::-1]:
                return i
    return -1