#update
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# #clear
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.clear()
# print(info)

#pop : remove item whose key is passed as parameter
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#del
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
