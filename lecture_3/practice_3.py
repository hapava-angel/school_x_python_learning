n: int = int(input('Enter a number: ')) 
def guess(n: int) -> int | str:
    for i in range (1,n+1):
        if n / i == i:
            return i
    return('трудно, не могу')
answer = (guess(n))
print(answer)