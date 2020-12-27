russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
newfile = []
with open('practice_1.txt', 'r') as textfile:
    for i in textfile:
        i = i.split(' ', 1)
        newfile.append(russian[i[0]] + '  ' + i[1])
with open('practice_2.txt', 'w') as newtextfile:
    newtextfile.writelines(newfile)