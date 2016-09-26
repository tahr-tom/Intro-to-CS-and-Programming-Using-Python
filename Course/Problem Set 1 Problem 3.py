""""Problem 3"""
s = 'azcbobobegghakl'
ansStr = ''
currentStr = ''
for i in range(len(s)):
    currentStr += s[i]
    if (i == len(s) - 1) or (s[i] > s[i + 1]):
        if len(currentStr) > len(ansStr):
            ansStr = currentStr
        currentStr = ''
print('Longest substring in alphabetical order is: ' + ansStr)
