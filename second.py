def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    dict = {0 : "nula",
            1 : "jedna",
            2 :"dva",
            3 : "tri",
            4 : "ctyri",
            5 : "pet",
            6 : "sest",
            7 : "sedm",
            8 :"osm",
            9 : "devet"
    }
    desitky = {10 : "seset",
            11 : "jedenact",
            12 : "dvanact",
            13 : "trinact",
            14 : "ctrnact",
            15 : "patnact",
            16 : "sestnact",
            17 : "sedmnact",
            18 : "osmnact",
            19 : "devatenact",
            20 : "dvacet",
            30 : "tricet",
            40 : "ctyricet",
            50 : "padesat",
            60 : "sedesat",
            70 : "sedmdesat",
            80 : "osmdesat",
            90 : "devadesat"
            }
    if int(cislo) < 10:
        return()




    return cislo

if __name__ == "__main__":
    cislo = int(input("Zadej číslo (0-100): "))
    text = cislo_text(cislo)
    print(text)