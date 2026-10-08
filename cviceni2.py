def vykraceni(seznam):
    print(seznam)
    z = input("zadejte cislo v seznamu od 0-4: ")
    q = seznam.pop(int(z))
    q *= 10
    return seznam.append(q)


    





if __name__ == "__main__":
    '''
    vek = int(input("Enter your age: "))
    vek += 1
    print(f"you'll be {vek} next year")
    if vek >= 18:
        print("you're an adult")
    else:
        print("you're too young")
    '''
    seznam = []
    print("zadejte 5 cisel")

    for i in range(5):
        cislo = int(input("zadejte cislo: "))
        seznam.append(cislo)
        print(seznam)
    vykraceni(seznam)
    print(seznam)

