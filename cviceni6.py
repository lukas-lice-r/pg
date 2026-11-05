import sys
import requests
import json


url = 'https://www.jcu.cz/cz/'
url1 = 'https://data.carnewschina.com/suggest?q=' ###
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'


def get_model_names(prefix):
    r = requests.get(url1 + (prefix))
    if r.status_code == 200:
        #print("request recieved")
        #l = url1 + prefix
        #print(l)
        pass
    else:
        print(f"error {r}")

    g = json.loads(r.content)
    models = []

    for model in g["models"]:
        models.append(model["name"])

    return [models]

'''def kurzy():
    r = requests.get(url2)
    if r.status_code != 200:
        return {}
    g = r.text

    value = g.splitlines()[2:]
    data = {}
    values = value.split("|")
    print(values)
    


    return '''


if __name__ == "__main__":
    # responce = requests.get(url)
    # if responce.status_code == 200:
    #     print(responce.content)

    '''    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} prefix")
        sys.exit()'''

    '''prefix = "ni"                    #sys.argv[1]
    models = get_model_names(prefix)
    for model in models:
        print(model)'''
    print("ahoj")
    kurzy()