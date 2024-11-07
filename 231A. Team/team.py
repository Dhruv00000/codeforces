n: int = int(input())
solutions: int = 0

for _ in range(n):

    views: str = input()
    views: list[str] = views.split()

    if views.count("1") > 1: solutions += 1

print(solutions)