from scrapy.crawler import CrawlerProcess

from scraper.pipeline import TiempoPipeline
from scraper.spider import TiempoSpider
from temperatures import AverageTemperatures


def crawl(city) -> AverageTemperatures:
    ITEM_PIPELINES = {
        "scraper.pipeline.TiempoPipeline": 300,
    }
    crawler = CrawlerProcess(settings={"ITEM_PIPELINES": ITEM_PIPELINES})
    TiempoSpider.target_city = city
    crawler.crawl(TiempoSpider)
    crawler.start()
    return TiempoPipeline.get_result()
