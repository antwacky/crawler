# Crawler

Simple web crawler for extracting links recursively from a given domain.

## Pre-reqs

Install the required Python packages as follows:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

The usage is as follows:

```
usage: crawler [-h] --domain DOMAIN --starturl STARTURL [--exclusive]
               [--processes PROCESSES] [--quiet]

Crawl URL for links

optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN, -d DOMAIN
                        domain to crawl
  --starturl STARTURL, -u STARTURL
                        url to start with
  --exclusive, -e       only crawl links on the provided domain
  --processes PROCESSES, -p PROCESSES
                        processes to use
  --quiet, -q           hide progress
```

For example:

```
python crawler --domain https://monzo.com --starturl / --exclusive --processes 2 --quiet
```
Use as a package as below:

```
>>> import crawler
>>> s = crawler.Spider(exclusive_domain=True)
>>> results = s.crawl()
>>> print(results)
{'https://www.example.com/': []}
```

## Unit Test

To run the unit tests run the tests.py file:
```
source venv/bin/activate
python tests.py
```
Example output:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.592s

OK
```

## Docker

Build the image:

```
docker build -t crawler:latest .
```

Run the container with args:

```
docker run crawler:latest --domain https://monzo.com --starturl / --exclusive --processes 2 --quiet
```
