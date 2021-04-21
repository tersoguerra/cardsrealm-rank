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

        metrics_xpath = '//*[@class="mainpage"]/div'
        metrics_elements = self.crawler.get_elements(metrics_xpath)

        for metrics_element in metrics_elements:
            metric_str = metrics_element.text

            metric_str = metric_str.replace("\n", " ").replace(".0", "")
            number_pattern = r'\d'
            if not match(metric_str, number_pattern):
                metric = 0
            else:
                metric = int(metric_str.split(" ")[0])

            metrics.append(metric)

        players_xpath = '//*[@class="mainpage"]/a'
        players_elements = self.crawler.get_elements(players_xpath)
        players_count = len(players_elements)
        metrics.append(players_count)

        if len(metrics) == 7:
            wins = metrics[3]
            loses = metrics[4]
            win_rate = 0
            if loses > 0:
                win_rate = wins/(wins+loses)
                win_rate = round(win_rate*100)
            metrics.append(win_rate)

        return metrics

    def get_player(self):
        pass
