from collections import Iterable

import scrapy
from temperatures import AverageTemperatures


def _calculate_average_week_temperature(temps: Iterable[str]) -> float:
    total_temperature = 0
    for temp in temps:
        total_temperature += int(temp)
    average = total_temperature / 7
    return average


class TiempoSpider(scrapy.spiders.XMLFeedSpider):
    name = "tiempo.com"
    allowed_domains = ["api.tiempo.com"]
    start_urls = [
        "http://api.tiempo.com/index.php?api_lang=es&division=102&affiliate_id=zdo2c683olan"
    ]
    itertag = "report"
    target_city = None

    def parse_node(self, response, node):
        all_data = node.xpath("//location/data")
        for data_node in all_data:
            city_name = data_node.xpath("name/text()").get()
            if city_name == self.target_city:
                url = data_node.xpath("url/text()").get()
                self.logger.info(url)
                yield scrapy.Request(
                    url + "&affiliate_id=zdo2c683olan",
                    callback=self.parse_city,
                )
                return
        yield AverageTemperatures()
        return

    def parse_city(self, node):
        TEMP_MIN = "Temperatura Mínima"
        TEMP_MAX = "Temperatura Máxima"
        result = AverageTemperatures()
        all_var = node.xpath("//var")
        for var_node in all_var:
            name = var_node.xpath("name/text()").get()
            if name == TEMP_MIN or name == TEMP_MAX:
                all_forecast = var_node.xpath("data/forecast/@value").getall()
                if name == TEMP_MIN:
                    result.min = _calculate_average_week_temperature(all_forecast)
                elif name == TEMP_MAX:
                    result.max = _calculate_average_week_temperature(all_forecast)
                if result.min is not None and result.max is not None:
                    break
        yield result
