import copy

x = [[1,2,3], [4,5,6]]
y = copy.copy(x)


print(x)
x = [[1,2,3], [4,6,6]]
print(y)

print(id(x))
print(id(y))

y = copy.deepcopy(x)
print(id(y))