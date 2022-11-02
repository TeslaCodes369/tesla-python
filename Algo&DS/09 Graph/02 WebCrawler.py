import requests
import re


class WebCrawler:
    def __init__(self) -> None:
        self.checked_sites = []

    def getLinks(self, raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html)

    def read_url(self, url):
        raw = ''

        try:
            raw = requests.get(url).text
        except Exception as e:
            pass

        return raw

    def crawl(self, url):
        queue = [url]

        self.checked_sites.append(url)

        while queue:
            ur = queue.pop(0)
            print(ur)

            ur_html = self.read_url(ur)

            for url in self.getLinks(ur_html):
                if url not in self.checked_sites:
                    self.checked_sites.append(url)
                    queue.append(url)


if __name__ == '__main__':
    wc = WebCrawler()
    wc.crawl('https://www.hp.com')
