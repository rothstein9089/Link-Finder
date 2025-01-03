import sys
import requests
import BeautifulSoup


def loop():
    for word in sys.stdin:
        res = requests.get(f" /{word}")
        if res.status_code == 404:
            loop()

        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)

loop()


def get_page_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    links = soup.find_all("a")

    for t in links:
        link2 = t.get("href")
        print(link2)




get_page_links('https://www.jackborisov.com')
