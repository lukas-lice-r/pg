class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"Osoba {self.jmeno} ma {self.vek} let"

    def pridat_rok1(self):
        self.vek += 1

class student(Osoba):

    def __init__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik
        if self.rocnik > 5:
            self.rocnik = "odstudoval"

    def __str__(self):
        return f"Student {self.jmeno} ma {self.vek} Status studenta {self.rocnik}"

    def pridat_rok(self):
        self.vek += 1
        try:
            self.rocnik += 1
        except Exception:
            return "student odstudoval"
        if self.rocnik > 5:
            self.rocnik = "vystudoval"



class Ucitel(Osoba):

    def __init__(self, jmeno, vek, roky_praxe):
        super().__init__(jmeno, vek)
        self.roky_praxe = roky_praxe

    def __str__(self):
        return f"Ucitel {self.jmeno} ma {self.vek} roky praxe {self.roky_praxe}"

    def pridat_rok(self):
        self.vek += 1
        self.roky_praxe += 1
        

class Udrzba(Osoba):

    def __init__(self, jmeno, vek):
        super().__init__(jmeno, vek)

    def __str__(self):
        return f"Udrzba {self.jmeno} ma {self.vek}"

    def pridat_rok():
        super().pridat_rok1


if __name__ == "__main__":
    osoba = Osoba("Franta", 15)
    print(osoba)
    osoba.pridat_rok1()
    print(osoba)

    print("/////////////")

    studentik = student("Ferda", 25, 5)
    print(studentik)
    studentik.pridat_rok()
    print(studentik)

    print("/////////////")

    ucitel = Ucitel("Vladimir", 6, 20)
    print(ucitel)
    ucitel.pridat_rok()
    print(ucitel)

    print("/////////////")

    udrzitel = Udrzba("Karel", 60)
    print(udrzitel)
    udrzitel.pridat_rok1()
    print(udrzitel)


    