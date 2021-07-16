import json
import argparse

from spider import Spider

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Crawl URL for links')

    parser.add_argument('--domain', '-d', dest='domain', help='domain to crawl', required=True)
    parser.add_argument('--starturl', '-u', dest='starturl', help='url to start with', required=True)
    parser.add_argument('--exclusive', '-e', action='store_true', dest='exclusive', help='only crawl links on the provided domain', required=False)
    parser.add_argument('--processes', '-p', type=int, dest='processes', help='processes to use', required=False)
    parser.add_argument('--quiet', '-q', action='store_true', dest='quiet', help='hide progress', required=False)

    args = parser.parse_args()

    spider = Spider(domain=args.domain, start_url=args.starturl, exclusive=args.exclusive, processes=args.processes, quiet=args.quiet)
    result = spider.crawl()
    print(json.dumps(result, indent=4))
