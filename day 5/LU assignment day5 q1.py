array = [0, 1, 2, 3, 4, 5, 56.0, 54, 0]

array.sort()
count = array.count(0)
for i in range(count):
    array.remove(0)
for i in range(count):
    array.append(0)

print(array)
