import yaml
import requests
import os
import json


class Scraper:
    def __init__(self):
        with open("config.yaml", "r") as file:
            self.config = yaml.safe_load(file)
        self.headers = self.config["headers"]
        self.base_url = self.config["base_url"]
        self.result_dict = {}

    def __str__(self):
        return str(vars(self))

    @staticmethod
    def generate_path(*args) -> str:
        return str(*args)

    def generate_url(self, *args) -> str:
        return self.base_url + self.generate_path(*args)

    @staticmethod
    def check_for_no_content(content_dict: dict, key: str) -> bool:
        if content_dict[key] == []:
            return True
        return False

    def write_data(self, results: list[dict], filename: str) -> None:
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        with open(f"{self.output_dir}/{filename}.json", "w") as file:
            json.dump(results, file)
        return

    def write_all_data(self) -> None:
        for key in self.result_dict.keys():
            self.write_data(results=self.result_dict[key], filename=key)
        return

    def get_page_data(self, *args) -> requests.models.Response:
        self.headers["Path"] = self.generate_path(*args)
        response = requests.get(url=self.generate_url(*args), headers=self.headers)
        try:
            response.raise_for_status()  # Raises an exception for non-2xx status codes
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
        return response


if __name__ == "__main__":
    s = Scraper()
    print(s)
