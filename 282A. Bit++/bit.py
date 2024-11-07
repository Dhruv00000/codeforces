n: int = int(input())

x: int = 0
for _ in range(n):

    statement: str = input()

    if "++" in statement: x += 1
    else: x -= 1

print(x)