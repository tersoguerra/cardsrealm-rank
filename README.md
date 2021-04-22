# CardsRealm Rank

Script in Python to rank teams and players from mtg.cardsrealm.com

## Installation

Use the package manager pip to install this dependencies:

- Pandas
```bash
pip install pandas
```
- Selenium
```bash
pip install selenium
```

Download Selenium ChromeDriver at your python binary's path, with the same version as your Google Chrome Browser: 
https://chromedriver.chromium.org/getting-started

Clone this script at: https://github.com/tersoguerra/cardsrealm-rank

## Usage

Execute main.py, input Y to execute team's players ranking, other inputs execute team ranking.
```bash
python3 main.py
```

Output data is exported at CSV file at main.py path, named "cardsrealm_teams OR players_rank_date.csv"

