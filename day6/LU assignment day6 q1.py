l1 = [1,2,3,4]
l2 = ['a','b','c','d']
d = dict([(l2[i],l1[i]) for i in range(len(l1))])
print(d)