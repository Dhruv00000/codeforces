n: int = int(input())

x: int = 0
for _ in range(n):

    statement: str = input()
    operation: str = statement.split("X")

    if "++" in [operation[0], operation[1]]: x += 1
    else: x -= 1

print(x)