import sys
from cviceni6 import download_rates


def convert(amount, currency):
    
    result = download_rates()
    smeg = result.get(currency)

    cislo = amount / result

    return cislo


if __name__ == "__main__":


    amount = float(input("zadejte mnozstvi: "))
    currency = input("zadejte menu: ").capitalize

    print(convert(amount,currency))