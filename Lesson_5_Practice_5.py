def summ():
    try:
        with open('practice_3.txt', 'w+') as textfile:
            line = input('Ввод: \n')
            textfile.writelines(line)
            number = line.split()

            print(sum(map(int, number)))
    except IOError:
        print("Ошибка")
    except ValueError:
        print("Ошибка")
summ()