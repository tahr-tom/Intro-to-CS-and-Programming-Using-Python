# Check how many tries required to generated the target number,
# If the number is beyond the range, program stop and ask for another target number
import random
lower = int(input('Please enter the lower limit(inclusive): '))
upper = int(input('Please enter the upper limit(inclusive): '))
numb = random.randint(lower, upper)
target = int(input('Please enter the your target number: '))
trial = 0
if target > upper or target < lower:
    print('Error! You have input a number which is not inside the lower and upper limit!')
    target = int(input('Please enter the your target number: '))
while numb != target:
    trial += 1
    numb = random.randint(1, 99)
if numb == target:
    print('Success! Generated', numb, 'with', trial, 'tries')
