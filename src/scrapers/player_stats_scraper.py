import json
from tqdm import tqdm
from scraper import Scraper


class PlayerStatsScraper(Scraper):
    def __init__(self):
        super().__init__()
        self.stats = self.config["stats"]
        self.output_dir = self.config["player_stats_output_dir"]
        self.result_dict = {s: [] for s in self.stats}

    @staticmethod
    def generate_path(stat: str, page_num: int) -> str:
        return f"/football/stats/ranked/players/{stat}?page={page_num}&compSeasons=719&comps=1&compCodeForActivePlayer=EN_PR&altIds=true"

    @staticmethod
    def check_for_no_content(content_dict: dict) -> bool:
        if content_dict["stats"]["content"] == []:
            return True
        return False

    def get_data(self, key) -> None:
        page_num = 0
        results = []
        while True:
            response = self.get_page_data(key, page_num)
            content_dict = json.loads(response.content.decode("utf-8"))
            if self.check_for_no_content(content_dict):
                break
            results.append(content_dict)
            page_num += 1
        self.result_dict[key] = results
        return

    def get_all_data(self) -> None:
        for key in tqdm(self.result_dict.keys()):
            self.get_data(key)
        return


if __name__ == "__main__":
    pss = PlayerStatsScraper()
    print(pss)
    pss.get_all_data()
    pss.write_all_data()
