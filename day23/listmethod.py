l  =[11,23,25,16,78]
print(l)
l.append(7)
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(25))
print(l.count(16))
#copy method
m = l.copy()
m[0] = 0
print(m)
print(l)
#insert method
l.insert(1,"green")
print(l)
#extend
p = [4,5,6,8,9]
# l.extend(p)
k = l + p
# print(l)
print(k)

