def jaccardova_mnozina():



    A = {"hokej", "fotbal"}
    B = {"tenis", "basketbal"}
    C = {"tenis", "fotbal"}


    prunik = A.intersection(C)
    sjednoceni = A.union(C)

    ji = len(prunik) / len(sjednoceni)

    jid = 1 - ji

    return jid


if __name__ == "__main__":
    print(jaccardova_mnozina())