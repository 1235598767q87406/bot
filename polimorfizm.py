class Chelovek:
    def __init__(self, size, name, xar):
        self.size = size
        self.name = name
        self.xar = xar

    def naz_sebya(self):
        print(f"называет себя {self.name}")


class Boy(Chelovek):
    def naz_sebya(self):
        print(f"называет себя мужским именем {self.name}")


class Girl(Chelovek):
    def naz_sebya(self):
        print(f"называет себя женским именем {self.name}")


boy = Boy("большой", "Даня", "добрый")
boy.naz_sebya()
girl = Girl("маленький", "Ася", "весёлый")
girl.naz_sebya()
