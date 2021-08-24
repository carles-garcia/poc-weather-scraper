from scraper.crawler import crawl

def test_crawl():
    result = crawl("Gavà")
    max = round(result.max, 1)
    min = round(result.min, 1)
    assert max == 27.3
    assert min == 20.4
