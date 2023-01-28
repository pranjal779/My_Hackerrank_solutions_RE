n = int(input())
res = []
grade = []
for i in range(n):
    name = input()
    mark = float(input())
    res.append([name, mark])
    grade.append(mark)
print(res)
print(grade)
grade = sorted(set(grade))
print(grade)
m = grade[1]
print(m)
name = []
for val in res:
    if m == val[1]:
        name.append(val[0])

print(name)
name.sort()
print(name)
for nm in name:
    print(nm)
