n: int = int(input('N: '))
array: list = range(n)
print(array)

i = 0

while True:
    if array[i] % 123 == 0:
        print(array[i], 'делится')
        break 
    i += 1