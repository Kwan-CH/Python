import csv

import data

name = 'demo.txt'
write = 'w'
APPEND = 'a'
read = 'r'

'''file1 = open('python.csv', mode='w')'''
# csv file is Excel
# code = 'HS'
# quantity = '89'
# file = open(name, mode=write)
# file.write(code + quantity)
#
# file = open(name, read)
# print(file.read())

# when mode == write, when want TO WRITE something in the file, when mode = write, it will overwrite EVERYTHING
# file = open(name, APPEND)
# print(file.write('\nhello'))
# file = open(name, read)
# print(file.read())
# file = open(name, mode=write)
# file.write('Hello world')
# file.close()
# file = open(name, read)
# print(file.read())
# print the whole content in the file
# print(file.readline())  # give out the 1st line of the content
# print(file.readline())  # multiple readLine will print the next content

# with open(name, read) as file1:
#     replaced = 'Earth'
#     file = file1.read()
#     file = file.replace('world', replaced)
#
# with open(name, write) as updated:
#     updated.write(file)


with open('../Assignment/demo.txt', mode=read) as myCSVFile:
    # csv.reader same thing like generator, require list()
    data = list(csv.reader(myCSVFile))
    # it will return the content in a list form, a row for a list
    # comma split word into separate element
    print(data)
    for content in data:
        string = ' '.join(content)  # join function to eliminate []
        print(string.split(' '))

print('file updated successfully')