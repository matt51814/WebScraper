from scraper import Scraper
import json
from tqdm import tqdm
from loguru import logger

logger.remove()
logger.add(lambda msg: tqdm.write(msg, end=""))


class StandingsScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.result_dict = {"standings": []}
        logger.success("Standings Scraper successfully loaded")

    @staticmethod
    def generate_path() -> str:
        return "/football/standings?compSeasons=719&altIds=true&detail=2&FOOTBALL_COMPETITION=1&live=true"

    def get_data(self, key) -> None:
        response = self.get_page_data()
        content_dict = json.loads(response.content.decode("utf-8"))
        self.result_dict[key] = content_dict["tables"][0]["entries"]
        return

    def get_all_data(self) -> None:
        logger.info("Getting data...")
        for key in tqdm(self.result_dict.keys()):
            logger.info(f"Getting {key} data...")
            self.get_data(key)
        logger.success("Data retrieved")
        return


if __name__ == "__main__":
    ss = StandingsScraper()
    print(ss)
    ss.get_all_data()
    ss.write_all_data()
