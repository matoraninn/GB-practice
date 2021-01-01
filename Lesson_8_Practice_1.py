class Date:
    def __init__(self, dmy):
        # self.day = day
        # self.month = month
        # self.year = year
        self.dmy = str(dmy)

    @classmethod
    def extract(cls, dmy):
        my_date = []
        for i in dmy.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f"Все верно"
                else:
                    return f"Год не соответсвует"
            else:
                return f"Месяц не соответсвует"
        else:
            return f"День не соответсвует"

    def __str__(self):
        return f" {Date.extract(self.dmy)}"


today = Date("1 - 1 - 2021")
print(today)
print(Date.valid(3, 3, 2033))
print(today.valid(4, 4, 2004))
print(Date.valid(1, 11, 2000))