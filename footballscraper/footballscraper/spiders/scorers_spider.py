import scrapy
from footballscraper.items import ScorersItem


class ScorersSpider(scrapy.Spider):
    name = "scorers"

    start_urls = ["https://native-stats.org/competition/PL/"]

    def parse(self, response):
        table = response.xpath("//*/table")[3]
        rows = table.xpath("tbody/tr")
        for row in rows:
            yield ScorersItem(
                player=row.xpath('td[2]/div/span/text()').get(),
                scorer_points=int(row.xpath('td[3]/text()').get().strip()),
                goals=int(row.xpath('td[4]/text()').get().strip()),
                assists=int(row.xpath('td[5]/text()').get().strip()),
                soccer_points_per_match=float(row.xpath('td[6]/text()').get().strip()),
                goals_per_match=float(row.xpath('td[7]/text()').get().strip()),
                avg_minutes_to_score=float(row.xpath('td[8]/text()').get().strip()),
                avg_minutes_to_score_or_assist=float(row.xpath('td[9]/text()').get().strip())
            )
