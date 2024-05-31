name = ["raj" , "singh" , "guman"  , "rame" , "shi" , "rohit" , "amit"]

if "raj" in name:
    print("yes")
else:
    print("No")
    
print(name[len(name)-3])#convert to positive indexing
print(name[:])
print(name[:5:2])#start , stop , step

#lst compre
lst = [i*i for i in range(4) if i%2==0] #[expresion1] "for i in range" if i%2==0 (this condition should be true then only keep element in the list)
print(lst)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)