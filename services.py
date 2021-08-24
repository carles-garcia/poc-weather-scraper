from typing import Optional

from scraper.crawler import crawl


class WeatherForecast:
    def get_average_min(self, city) -> Optional[float]:
        result = crawl(city)
        return result.min

    def get_average_max(self, city) -> Optional[float]:
        result = crawl(city)
        return result.max
