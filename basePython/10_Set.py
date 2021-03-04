#不允许重复元素，并且可以 交集、并集、差集

set={1,2,3,4,5}
set.add(6)
set.pop()
set.remove(2)
set.discard(3)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1 & set2)
print(set1.intersection(set2))

print(set1 | set2)
print(set1.union(set2))

print(set1 - set2)
print(set1.difference(set2))

