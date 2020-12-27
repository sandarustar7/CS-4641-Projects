from basketball_reference_web_scraper import client

from basketball_reference_web_scraper.data import Location
from basketball_reference_web_scraper.data import Team
from basketball_reference_web_scraper.data import OutputType

client.standings(season_end_year=2019, output_type=OutputType.CSV, output_file_path="./test.csv")
output = client.players_season_totals(season_end_year = 2017)
print(output)

