import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """

    hrefs = []


    r = requests.get(url)
    if r.status_code == 200:
        pass
    else:
        return "error" + r

    data = r.text
    lines = data.split('<a href="')
    for line in lines[1:]:
        urls = line.split('"')[0]
        if urls.startswith("https://"):
            hrefs.append(urls)

    return hrefs


if __name__ == "__main__":
    try:
        url = 'https://www.jcu.cz/cz/' #sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
