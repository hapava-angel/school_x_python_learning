not_sequence = 0
# N: int = int(input('Enter the number: '))
a = [int(i) for i in input()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
