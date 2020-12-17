class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} went'
    def stop(self):
        return f'\n{self.name} has stopped'
    def turn(self, direction):
        return f'\n{self.name} turned {direction}'
    def show_speed(self):
        return f'\nSpeed is {self.speed}'
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nSpeed is {self.speed}.The speed limit is exceeded'
        else:
            return f'\nSpeed is {self.speed}'
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nSpeed is {self.speed}.The speed limit is exceeded'
        else:
            return f'\nSpeed is {self.speed}'
class PoliceCar(Car):
    pass
class SportCar(Car):
    pass


town = TownCar(90,'black','Toyota', False)
print('Tcar:\n' + town.go(), town.show_speed(), town.turn('right'), town.turn('around'), town.stop())
work = WorkCar(20,'yellow','Caterpillar', False)
print('Wcar:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())
police = PoliceCar(120,'white','Ford', True)
print('Pcar:\n' + police.go(), police.show_speed(), police.turn('left'), police.stop())
sport = SportCar(180,'black','Porsche', False)
print('Scar:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

