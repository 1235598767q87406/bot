class Ruchka:
    def __init__(self, color, mat):
        self.color = color
        self.mat = mat

    def pisat(self):
        print("ручка пишет")


ru = Ruchka("чёрный", "пластик")
print(ru.color)
ru.pisat()
