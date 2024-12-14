n = int(input())
arr = []

for _ in range(n):
    command = input().split()
    if command[0] == "print":
        print(arr)
    else:
        getattr(arr, command[0])(*(int(x) for x in command[1:]))
