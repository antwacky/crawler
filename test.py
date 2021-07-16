import unittest
from spider import Spider

class TestCrawler(unittest.TestCase):

    def test_empty_crawl(self):
        spider = Spider(exclusive=True)
        results = spider.crawl()
        results = results[0]
        self.assertTrue(len(results)==1)
        for link, links in results.items():
            self.assertTrue(len(links) == 0)

    def test_error_response(self):
        spider = Spider(domain='https://www.york.ac.uk/teaching/cws/wws/webpage1.html', exclusive=True)
        results = spider.crawl()
        self.assertTrue(len(results)==1)
        results = results[0]
        for link, links in results.items():
            self.assertTrue(links == 'got http error response 404')

if __name__ == '__main__':
    unittest.main()
