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

        queries = ["a", "e", "i", "o", "u"]
        for query in queries:

            search_xpath = '//*[@id="inputSearchCard"]'
            self.crawler.send_input(search_xpath, query)

            xpath = '//*[@id="search_display_div"]/a'
            elements = self.crawler.get_elements(xpath)

            for element in elements:
                name = element.get_attribute("title")
                url = element.get_attribute("href")
                teams_dict[name] = {"url": url}

        return teams_dict

    def get_team_metrics_and_players(self, url):
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

        players_urls = list()
        for players_element in players_elements:
            players_url = players_element.get_attribute("href")
            players_urls.append(players_url)

        if len(metrics) == 7:
            wins = metrics[3]
            losses = metrics[4]
            win_rate = self.win_rate(wins, losses)
            metrics.append(win_rate)

        return metrics, players_urls

    def get_player_metrics(self, url):
        metrics = list()

        self.crawler.get_url(url)

        user_xpath = '/html/body/div[4]/div/div/div[2]/div[1]/p[2]'
        username_title = self.crawler.get_element_text(user_xpath)
        username_parts = username_title.split(": ")
        if len(username_parts) == 2:
            username = username_parts[1]
        else:
            username = ""
        metrics.append(username)

        metrics_xpath = '//*[@class="div_league_player_data"][1]/div/div[2]/*'
        metrics_elements = self.crawler.get_elements(metrics_xpath)

        for metrics_element in metrics_elements[1:]:
            metric_str = metrics_element.text
            metric_str = metric_str.replace(".0", "")
            if metric_str != "":
                metric = int(metric_str)
            else:
                metric = 0
            metrics.append(metric)

        if len(metrics) == 7:
            wins = metrics[3]
            losses = metrics[4]
            win_rate = self.win_rate(wins, losses)
            metrics.append(win_rate)

        return metrics

    @staticmethod
    def win_rate(wins, losses):
        win_rate = 0
        if losses > 0:
            win_rate = wins / (wins + losses)
            win_rate = round(win_rate * 100)
        return win_rate
