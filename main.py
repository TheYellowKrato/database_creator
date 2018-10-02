from Database import Database
from SbcParser import SbcParser

if __name__ == "__main__":
    database = Database()
    sbc_parser = SbcParser()
    print(sbc_parser.get_sbcs())
