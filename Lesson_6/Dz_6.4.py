class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Our speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Our speed for town car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'{self.name}speed is high please slow down'
        else:
            return f'Normal speed for {self.name} '


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Our speed for town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'{self.name}speed is high please slow down'
        else:
            return f'Normal speed for {self.name} '


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Our speed for town car {self.name} is {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Our speed for town car {self.name} is {self.speed}')


l = SportCar(150, 'Yelow', 'Lamborginy', False)
f = TownCar(75, 'White', 'Ford', False)
r = WorkCar(38, 'Grey', 'Reno', True)
a = PoliceCar(110, 'None', 'Audi', True)
print(r.turn_left())
print(f'When {f.turn_right()}, {a.stop()} for inspection')
print(f'{f.go()} with speed exactly {f.show_speed()}')
