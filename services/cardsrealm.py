from services.crawler import Crawler
from services.regex import *


class CardsRealm(object):

    def __init__(self):
        self.crawler = Crawler()
        self.domain = "https://mtg.cardsrealm.com/"

    def get_teams(self):
        teams_dict = dict()

        url = f"{self.domain}teams/"
        self.crawler.get_url(url)

        xpath = '//*[@id="search_display_div"]/a'
        elements = self.crawler.get_elements(xpath)

        for element in elements:
            name = element.get_attribute("title")
            url = element.get_attribute("href")
            teams_dict[name] = {"url": url}

        return teams_dict

    def get_team_metrics(self, url):
        metrics = list()

        self.crawler.get_url(url)

        xpath = '//*[@class="mainpage"]/div'
        elements = self.crawler.get_elements(xpath)

        for element in elements:
            metric = element.text

            metric = metric.replace("\n", " ").replace(".0", "")
            number_pattern = r'\d'
            if not match(metric, number_pattern):
                metric = f'0 {metric}'

            metrics.append(metric)

        return metrics

    def get_player(self):
        pass
