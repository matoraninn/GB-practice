
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = int(input("Введите год рождения: "))
city = input("Введите город: ")
email = input("Введите email: ")
telephone = input("Введите номер: ")

def second_func(name, surname, year, city, email, telephone):
    return name, surname, year, city, email, telephone
print(f"(Имя - {name}; Фамилия - {surname}; Год рождения - {year}; Город - {city}; Email - {email}; Телефон - {telephone}")


