import scrapy
from footballscraper.items import StandingItem


class StandingsSpider(scrapy.Spider):
    name = "standings"

    start_urls = ["https://native-stats.org/competition/PL/"]

    def parse(self, response):
        table = response.xpath("//*/table")[2]
        rows = table.xpath("tbody/tr")
        for row in rows:
            yield StandingItem(
                pos=row.xpath("td[1]/text()").get(),
                team=row.xpath("td[2]/div/span/span[1]/text()").get(),
                matches=int(row.xpath("td[3]/text()").get()),
                points=int(row.xpath("td[4]/text()").get()),
                plus_and_minus=int(row.xpath("td[5]/text()").get()),
                goals=row.xpath("td[6]/text()").get().strip(),
            )
