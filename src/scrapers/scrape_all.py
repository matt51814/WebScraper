from fixtures_scraper import FixturesScraper
from player_stats_scraper import PlayerStatsScraper
from results_scraper import ResultsScraper
from standings_scraper import StandingsScraper

if __name__ == "__main__":
    for scraper in [
        FixturesScraper,
        PlayerStatsScraper,
        ResultsScraper,
        StandingsScraper,
    ]:
        s = scraper()
        s.get_all_data()
        s.write_all_data()
