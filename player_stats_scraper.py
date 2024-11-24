import requests
import json
import yaml
from tqdm import tqdm


class PlayerStatsScraper:
    def __init__(self):
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)
        self.headers = config["headers"]
        self.base_url = config["base_url"]
        self.stats = config["stats"]
        self.result_dict = {s: [] for s in self.stats}

    @staticmethod
    def generate_path(stat: str, page_num: int) -> str:
        return f"/football/stats/ranked/players/{stat}?page={page_num}&compSeasons=719&comps=1&compCodeForActivePlayer=EN_PR&altIds=true"

    def generate_url(self, stat: str, page_num: int) -> str:
        return self.base_url + self.generate_path(stat, page_num)

    @staticmethod
    def check_for_no_content(content_dict: dict) -> bool:
        if content_dict["stats"]["content"] == []:
            return True
        return False

    @staticmethod
    def write_data(results: list[dict], filename: str) -> None:
        with open(f"{filename}.json", "w") as file:
            json.dump(results, file)
        return

    def write_all_data(self) -> None:
        for key in self.result_dict.keys():
            self.write_data(results=self.result_dict[key], filename=key)
        return

    def get_page_data(self, key: str, page_num: int) -> requests.models.Response:
        self.headers["Path"] = self.generate_path(key, page_num)
        response = requests.get(
            url=self.generate_url(key, page_num), headers=self.headers
        )
        try:
            response.raise_for_status()  # Raises an exception for non-2xx status codes
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
        return response

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
    pss.get_all_data()
    print(pss.result_dict)
