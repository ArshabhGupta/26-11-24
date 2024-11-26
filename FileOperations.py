#file = open('file.txt', 'r')
#print(file.read())
#print("File in the Read mode")
#print(file.read())
#file.close()

#file_write = open('file.txt', 'w')
#file_write.write("File in the write mode.....")
#file_write.write("Hello I am Arshabh!")
#file.close()

#file_append = open('file.txt', 'a')
#file_append.write("File in the append mode.....")
#file_append.write("Hello again!")
#file_append.close()

file = open('file.txt', 'r')
counter = 0
content = file.read()
colelist = content.split("\n")
for i in colelist:
    if i:
        counter += 1
print("This is the number of lines in file: ")
print(counter)

