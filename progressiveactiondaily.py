from unicodedata import normalize

from bs4 import BeautifulSoup
from requests import get


def main():
    url = "https://progressiveactiondaily.com/category/action/page/%s/"

    results = []
    for page in range(1, 8):
        response = get(url % page)
        soup = BeautifulSoup(response.text, 'html.parser')

        articles = soup.select('article')

        for article in articles:
            headline = article.select('h2 a')[0].text
            headline = headline.replace("Action of the day: ", "")
            headline = normalize('NFKD', headline)
            headline = headline.capitalize()

            link = article.select('p a')[0]

            results.append({
                "action": headline,
                "link": link['href']
            })

    return results


if __name__ == "__main__":
    main()
