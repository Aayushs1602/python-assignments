list1 = [10, 20, 30, 40, 50, 60, 70, 80]  # sorted list one
list2 = [10, 15, 20, 25, 30, 35, 40, 50, 60]  # sorted list two

# using one loop merge both of them into one

list_merged = []

index1 = 0
index2 = 0

while True:
    print(index1, index2)
    if index1 < len(list1) and index2 < len(list2):
        a = list1[index1]
        b = list2[index2]
        if a < b:
            list_merged.append(a)
            index1 += 1

        else:
            list_merged.append(b)
            index2 += 1
    else:
        if index1 < len(list1):
            a = list1[index1]
            list_merged.append(a)
            index1 += 1

        if index2 < len(list2):
            b = list1[index2]
            list_merged.append(b)
            index2 += 1

        elif index2 == len(list2) and index1 == len(list1):
            break

print(list_merged)
