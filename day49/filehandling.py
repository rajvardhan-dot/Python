#READING
f = open('raj.txt' , 'r')
text = f.read()
print(text)
f.close()

# f = open('raj2.txt' , 'w'):to create new file
# text = f.read()
# print(text)
# f.close() 


# WRITING
f = open('raj2.txt' , 'w')
f.write('Hello world')
f.close()


#WITH KEYWORD
with open('raj.txt' , 'a') as f:
    f.write("hey i am inside with")