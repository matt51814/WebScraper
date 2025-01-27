from scraper import Scraper
import json
from tqdm import tqdm
from loguru import logger

logger.remove()
logger.add(lambda msg: tqdm.write(msg, end=""))


class FixturesScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.result_dict = {"fixtures": []}
        logger.success("Fixtures Scraper successfully loaded")

    @staticmethod
    def generate_path(page_num: int) -> str:
        return f"/football/fixtures?comps=1&teams=1,2,127,130,131,4,6,7,34,8,26,10,11,12,23,15,20,21,25,38&compSeasons=719&page={page_num}&pageSize=10&statuses=U,L&altIds=true&fast=false"

    def get_data(self, key) -> None:
        page_num = 0
        results = []
        while True:
            response = self.get_page_data(page_num)
            content_dict = json.loads(response.content.decode("utf-8"))
            if self.check_for_no_content(content_dict, "content"):
                break
            results.extend(content_dict["content"])
            page_num += 1
        self.result_dict[key] = results
        return

    def get_all_data(self) -> None:
        logger.info("Getting data...")
        for key in tqdm(self.result_dict.keys()):
            logger.info(f"Getting {key} data...")
            self.get_data(key)
        logger.success("Data retrieved")
        return


if __name__ == "__main__":
    fs = FixturesScraper()
    fs.get_all_data()
    fs.write_all_data()
