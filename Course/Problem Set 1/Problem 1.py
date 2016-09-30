"""Problem 1"""
s = 'azcbobobegghakl'
vowel = 0
for letter in s:
    if letter == 'a':
        vowel += 1
    elif letter == 'e':
        vowel += 1
    elif letter == 'i':
        vowel += 1
    elif letter == 'o':
        vowel += 1
    elif letter == 'u':
        vowel += 1
print('Number of vowels: ' + str(vowel))
