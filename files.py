import datetime


file_handler = open("C:/Users/jenya/Desktop/111.txt")#as a defult it opens as reading('r')
print(file_handler)
print(file_handler.tell()) #tell me where i amin the file

listOfLines = file_handler.readlines() #read all the lines into list
                                        #not recomendedon big file
print(listOfLines)
print('==============================')
print([word.replace('\n', '') for word in listOfLines]) #raplace /n for a blanc space, more aesthetic code

print(file_handler.tell()) #tell me where i amin the file
print('===============================')
print([len(word) for word in listOfLines])#the lengh of the file
print('================================')
print('sum', sum([len(word) for word in listOfLines]))#the sum of the words(withought the spase)
print('================================')

for line in listOfLines:
    print(line, end='')
print('====================================')
listOfLines = file_handler.readlines()
print(listOfLines) #gives us an empty list becouse its the end of the file
file_handler.seek(0) #returns to the begining of the file, we can move through the file with the seek command
listOfLines = file_handler.readlines()
print(listOfLines)

file_handler.close() #must close the file when we finish working with him

with open('C:\\Users\\jenya\\Desktop\\111.txt') as file_handler:
    for line in file_handler:
        print(line, end='')#becouse of the with it willbe closed(so we wont forget to close it)


with open('C:\\Users\\jenya\\Desktop\\new111.txt', 'w') as file_handler:#if the file dont exict, it creates one
    file_handler.write(f'hello new file{datetime.datetime.now()}') #datetime.datetime.now()-writes the time right now to the new file

with open('C:\\Users\\jenya\\Desktop\\new111.txt', 'a') as file_handler:# as append it adds it as well
    file_handler.seek(0)#append doesnt go back back to start
    file_handler.write('\n')
    file_handler.write(f'hello new file{datetime.datetime.now()}')
    print(file_handler.tell())#proof that append doesnt go back


with open('C:\\Users\\jenya\\Desktop\\new111.txt', 'w') as file_handler:#if the file dont exict, it creates one
   file_handler.seek(0)
   file_handler.write(f'good buy{datetime.datetime.now()}')# writing 'r' let us move through the file
   #cennot read, only write with 'w' or 'a'
   #file_handler.seek(0)
   #line = file_handler.readline()
   #print(f'line = {line}')


with open('C:\\Users\\jenya\\Desktop\\new111.txt', 'w+') as file_handler:#w+ gives us the option to write and to read as well
   file_handler.seek(0)
   file_handler.write(f'good buy')
   #cennot read, only writee
   file_handler.seek(0)
   line = file_handler.readline()
   print(f'line = {line}')


with open('C:\\Users\\jenya\\Desktop\\new1111.txt', 'r+') as file_handler:# r+ = you read line and then we do write, thats why wed did seek.
   file_handler.seek(0)
   line = file_handler.readline()
   print(f'line read in r+ = {line}')
   file_handler.write((f'first line in file {datetime.datetime.now()}'))

# we have 'a+' we will use it only when we dont want to spoil what we write on the document, it's starts in the end of the opened file.

