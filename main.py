from Database import Database
from SbcParser import SbcParser

if __name__ == "__main__":

    database = Database()
    sbc_parser = SbcParser()

    database.remove_challenges()

    data = sbc_parser.get_sbcs()
    database.insert_challenge(data)

    print(database.count_challenges())
    print(database.get_challenges())
