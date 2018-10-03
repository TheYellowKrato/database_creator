from Database import Database
from PlayersParser import PlayersParser
from SbcParser import SbcParser

if __name__ == "__main__":

    database = Database()
    sbc_parser = SbcParser()
    players_parser = PlayersParser()

    database.remove_challenges()
    database.remove_players()

    sbc_data = sbc_parser.get_sbcs()
    database.insert_challenge(sbc_data)

    print(database.count_challenges())
    print(database.get_challenges())

    players_data = players_parser.get_players()
    database.insert_player(players_data)

    print(database.count_players())
    print(database.get_players())
