with open("practice_1.txt", 'w') as textfile:
  while True:
    text_x = input()
    if text_x == "": break
    textfile.write(text_x + "\n")