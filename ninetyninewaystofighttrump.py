from unicodedata import normalize

from bs4 import BeautifulSoup
from requests import get


def main():
    url = "https://99waystofighttrump.com/"

    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.select('ol li')

    results = []
    for item in items:
        link = item.select('a')[0]['href'] if item.select('a') else None
        action = normalize('NFKD', item.text)

        results.append({
            "action": action,
            "link": link
        })

    return results


if __name__ == "__main__":
    main()
