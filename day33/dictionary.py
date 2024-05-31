dic = {
    1: "raj",
    2: "ram",
    3: "goyal",
    4: "suraj"
}
# print(dic[4])
# print(dic['1'])
# print(dic.get('1')) #get will throw any error

for key in dic.keys():
    print(f"the value of corresponding to the key {key} is {dic[key]}")