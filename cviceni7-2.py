class chyba(Exception):
    pass

class Banka:
    def __init__(self, jmeno, urok):
        self.jmeno = jmeno
        self.urok = urok
        self.zustatek = 0

    def __str__(self):
        return f"Na ucte {self.jmeno} je {self.zustatek}"


    def vloz(self, castka):
        if castka < 0:
            #return "nelze vlozit"
            raise chyba("nemuzete vlozit zapornou castku")
        self.zustatek += castka
        #return f"vlozil jste {castka} vas ucetni zustatek je {self.zustatek}"

    def vyber(self, castka):
        try:
            self.zustatek -= castka
            #return f"vybral jste {castka} vas ucetni zustatek je {self.zustatek}"
        except:
            pass

    def pricti_urok(self):
        xx = self.zustatek / 100
        yy = xx * self.urok
        self.zustatek += yy
        #return f"Urok vaseho {self.jmeno} je {self.urok} procent, vas novy zustatek na ucte je {self.zustatek}"


if __name__ == "__main__":

    ucet = Banka("Sporici", 3)
    print(ucet)
    ucet.vloz(200)
    print(ucet)
    ucet.vyber(100)
    print(ucet)
    ucet.pricti_urok()
    print(ucet)
