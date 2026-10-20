def je_prvocislo(cislo):
    if cislo < 2:
        return False

    for i in range(2, cislo):
        if cislo % i == 0:
            return False

    return True

def vrat_prvocisla(maximum):
    list = []
    for cislo in range(maximum + 1):
        if je_prvocislo(cislo):
            list.append(cislo)

    return list

    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)

    