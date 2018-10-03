import json
import urllib


class PlayersParser(object):

    base_url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page="

    def __init__(self):
        pass

    def get_players(self):

        players = []

        players_data = urllib.request.urlopen(self.base_url).read()
        players_json = json.loads(players_data.decode("utf-8"))

        total_pages = players_json["totalPages"]

        for page in range(1, total_pages + 1):
            players_data = urllib.request.urlopen(self.base_url + str(page)).read()
            players_json = json.loads(players_data.decode("utf-8"))
            players = players + players_json["items"]

        return players
