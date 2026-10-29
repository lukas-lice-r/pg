import sys

def inkrementuj_cisla(data):
    with open("data.txt", "r") as file:
        data1 = file.read().split(",")

        result = []

        for item in data1:
            try:
                result.append(str(int(item) +1))
            except ValueError:
                result.append(item)
    print(result)

    
# rozdelit data carkou a pridat +1 k cislum


def nacti_radky(file_name):
    radky = []
    with open(file_name, "r") as file:
        for line in file:
            radky.append(line.strip())
    return radky

    

def zapis_radky(file_name, data):

    #with open(data, "w") as file:
    #    file.write("zapis")
    sw = file_name
    sm = data
    with open("data.txt", "w") as file:
        file.write("ferda, ")
        file.write("5")
    print(file)



if __name__ == "__main__":

#    if len(sys.argv) <= 1:
#        print(f'Pouziti: python {sys.argv[0]} jmeno_souboru')
#        sys.exit()

    file_name = "data.txt"          #sys.argv[1]   data.txt

    try:
        data = nacti_radky(file_name)
        print(data)
    except FileNotFoundError:
        print(f'Soubor {file_name} neexistuje')
        
    data = inkrementuj_cisla(data)

    name = file_name.split('.')  #  name = ['data', 'csv']

    file_name2 = name[0] + '2.' + name[1]  #  'data2.txt'
    zapis_radky(file_name2, data)