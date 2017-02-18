from unicodedata import normalize

from bs4 import BeautifulSoup
from requests import get


def main():
    url = "http://2hoursaweek.org/"

    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    sections = soup.select('section')

    results = []
    for section in sections:
        action = section.select('h3')[0].text
        action = normalize('NFKD', action)

        links = section.select('a.action-link')
        link = links[0]['href'] if links else None

        results.append({
            "action": action,
            "link": link
        })

    return results


if __name__ == "__main__":
    main()
