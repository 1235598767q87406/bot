class Animal:
    def __init__(self, size, color, name):
        self.size = size
        self.color = color
        self.name = name

    def move(self):
        print("животное двигается")


class Tiger(Animal):
    def rev(self):
        print("тигр рычит")


tiger = Tiger("средний", "рыжий", "пушок")
print(tiger.color)
