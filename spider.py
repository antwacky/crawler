import requests
import queue
import threading
import sys
from bs4 import BeautifulSoup

class Spider:

    def __init__(self, domain='https://www.example.com', start_url='/', exclusive_domain=False):

        self.domain = domain
        self.start_url = start_url
        self.exclusive_domain = exclusive_domain

    def get_links(self, link):

        try:
            html = requests.get(link).text
        except:
            print('failed to connect to {}'.format(self.domain))
            sys.exit(1)

        s = BeautifulSoup(html, 'html.parser')
        links = [ a.get('href') for a in s.find_all('a') ]
        links = [ link for link in links if link != None ]

        if self.exclusive_domain == True:
            # exclude any links not relative to given domain
            links = [ link for link in links if 'http' not in link ]

        return links

    def _worker(self, q, results):

        while q.qsize() > 0:
            link = q.get()

            if self.start_url not in link:
                continue

            if link in results:
                continue

            # complete relative links
            if 'http' not in link:
                link = self.domain + link

            links = self.get_links(link)
            results[link] = links

            for link in links:
                q.put(link)

        return

    def crawl(self):

        start_url = self.domain + self.start_url
        results = {}

        q = queue.Queue()
        q.put(start_url)

        t = threading.Thread(target=self._worker, args=(q, results, ))
        t.start()
        t.join()

        return results
