import json
import argparse

from spider import Spider

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Crawl URL for links')

    parser.add_argument('--domain', dest='domain', help='domain to crawl', required=True)
    parser.add_argument('--starturl', dest='starturl', help='url to start with', required=True)
    parser.add_argument('--exclusive', action='store_true', dest='exclusive_domain', help='only crawl links on the provided domain', required=False)

    args = parser.parse_args()

    spider = Spider(domain=args.domain, start_url=args.starturl, exclusive_domain=args.exclusive_domain)
    result = spider.crawl()
    print(json.dumps(result, indent=4))
