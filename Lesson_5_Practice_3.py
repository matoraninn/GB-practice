with open("practice_1.txt") as textfile:
 members ={}
 q = 0
 x = 0
 for i in textfile:
     q += 1
     name, income  = i.split()
     members[name] = income
     x = x + int(income)
     if int(income) < 20000:
        print (f'{name}')
 result = x / q
 print(result)