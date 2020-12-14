with open("practice_1.txt") as textfile:
 lines = 0
 for i in textfile:
        lines += 1
        words = 0
        space = 0
        for j in i:
            if j != " " and space == 0:
                words += 1
                space = 1
            elif j == " ":
                space = 0
        print("Слов:",words)
print("Строк:",lines)