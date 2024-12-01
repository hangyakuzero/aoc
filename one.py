left = []
right = []
with open("day1.txt") as file1:
    lines = file1.readlines()
print(lines)
for line in lines:
    line = line.strip().split()

    left.append(int(line[0]))
    right.append(int(line[1]))

left = sorted(left)
right = sorted(right)
total = 0
print(left)
print(right)
for i in range(len(left)):
    total += abs(left[i] - right[i])
print("total =", +total)

new = 0

map = {}
numb = []
for i in right:
    map[i] = right.count(i)

print(map)
for j in left:
    if j in map:
        new += j * (map.get(j))
print(new)
