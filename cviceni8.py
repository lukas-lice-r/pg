import json

class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

#    def __str__(self):
#        return f"Osoba {self.jmeno} s telefonem {self.telefon} a mailem {self.email}"
#    def jmeno(self, jmeno):
#        hasdigit = False
#        for char in jmeno:
#            if char.isdigit():
#                hasdigit = True
#                return "jmeno nesmi obsahovat cislice"
#    def telefon(self, telefon):
#        try:
#            o = int(telefon)
#        except Exception:
#            return "Telefon nesmi obsahovat pismena"
#    def email(self, email):
#        pass

    @property
    def jmeno(self):
        return self.__jmeno

    @jmeno.setter
    def jmeno(self, hodnota):
        if hodnota.replace(" ", "").isalpha():
            self.__jmeno = hodnota
        else:
            raise InvalidData("jmeno muze obsahovat pouze pismena")

    def __str__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"

    @classmethod
    def load_json_data(cls, data):
        if "jmeno" not in data or "telefon" not in data or "email" not in data:
            return None
        return cls(data["jmeno"], data["telefon"], data["email"])
#    def load_json_data(cls, data):
#        with open(data, "r") as file:
#            return cls.file


if __name__ == "__main__":
    o = Osoba("Jan Novak", "004225877845", "jan@novak,cz")
    print(o)
#    o.jmeno = "4894654879"
#    print(o)
#    o.telefon = "Ferda"
#    print(o)

    osoby = []
    with open("osoby.json", "r") as f:
        data = json.loads(f.read())
        for record in data:
            osoby.append(Osoba.load_json_data(record))
    print(osoby)