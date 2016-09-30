"""Problem 2"""
s = 'azcbobobegghakl'
present = 0
n = 0
while n < (len(s) - 2):
    if s[n:n + 3] == 'bob':
        present += 1
        n += 1
    else:
        n += 1
print('Number of times bob occurs is: ' + str(present))
