from Database import Database
from PlayersParser import PlayersParser
from SbcParser import SbcParser


def load_players():
    players_parser = PlayersParser()

    database.remove_players()

    players_data = players_parser.get_players()
    database.insert_player(players_data)

    print(database.count_players())
    print(database.get_players())

def load_challenges():
    sbc_parser = SbcParser()
    database.remove_challenges()

    sbc_data = sbc_parser.get_sbs()
    database.insert_challenge(sbc_data)

    print(database.count_challenges())
    print(database.get_challenges())


if __name__ == "__main__":

    database = Database()

    print("Type 1 to load players")
    print("Type 2 to load challenges")
    print("Type 3 to load both")
    choice = input()
    if choice.isdigit():
        choice = int(choice)
    else:
        choice = -1
    if choice == 1:
        load_players()
    elif choice == 2:
        load_challenges()
    elif choice == 3:
        load_players()
        load_challenges()
    else:
        print("Didn't understand your choice")








