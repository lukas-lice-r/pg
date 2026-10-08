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
    desitky1 = {10 : "deset",
            11 : "jedenact",
            12 : "dvanact",
            13 : "trinact",
            14 : "ctrnact",
            15 : "patnact",
            16 : "sestnact",
            17 : "sedmnact",
            18 : "osmnact",
            19 : "devatenact"
    }
    desitky = {
            2 : "dvacet",
            3 : "tricet",
            4 : "ctyricet",
            5 : "padesat",
            6 : "sedesat",
            7 : "sedmdesat",
            8 : "osmdesat",
            9 : "devadesat"
            }

    
    if -1 < int(cislo) < 10:
        return(dict[int(cislo)])
    
    elif 9 < int(cislo) < 20:
        return(desitky1[int(cislo)])
    
    elif int(cislo) == 100:
        cislo = "sto"

    elif 19 < int(cislo) < 100:
        f = int(cislo) // 10
        g = int(cislo) % 10
        l = dict[g]
        if l == "nula":
            l = ""
        return(desitky[f] + " " + l)
    elif int(cislo) < 0:
        return "zadal jste cislo v minusu"
    else:
        return "zadal jste cislo mimo 0-100"

    return cislo

if __name__ == "__main__":
    smg = True
    while smg:

        cislo = input("Zadej číslo (0-100): ")
        if cislo.lstrip("-").isdigit():
            smg = False
        else:
            print("nezadal jste cislici")
    text = cislo_text(cislo)
    print(text)