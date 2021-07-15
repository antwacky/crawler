import unittest
from spider import Spider

class TestCrawler(unittest.TestCase):

    def test_empty_crawl(self):
        spider = Spider(exclusive_domain=True)
        results = spider.crawl()
        for link, links in results.items():
            self.assertTrue(len(links) == 0)

    def test_crawl(self):
        spider = Spider(domain='https://www.york.ac.uk/teaching/cws/wws/webpage1.html', exclusive_domain=True)
        results = spider.crawl()
        self.assertTrue(len(results)==1)
        results = next(iter(results.values()))
        self.assertTrue('#Main-Content' in results)
        self.assertTrue('#Mobile-Search' in results)
        self.assertTrue('#Main-Navigation' in results)

if __name__ == '__main__':
    unittest.main()
