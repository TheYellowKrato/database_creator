import pymongo


class Database:
    con = None
    table = None

    def __init__(self):
        self.con = pymongo.MongoClient("mongodb://localhost:27017/")
        self.table = self.con["fut19"]

    def get_database_list(self):
        return self.con.list_database_names()

    def insert_data(self, table_name, data):
        if len(data) is not 0:
            if isinstance(data, list):
                return self.table[table_name].insert_many(data)
            else:
                return self.table[table_name].insert_one(data)
        else:
            print("No data found")
            return False

    def get_data(self, table_name):
        results = []
        for result in self.table[table_name].find():
            results.append(result)
        return results

    def remove_data(self, table_name):
        return self.table[table_name].remove({})

    def insert_challenge(self, challenge_data):
        return self.insert_data("challenges", challenge_data)

    def insert_player(self, player_data):
        return self.insert_data("players", player_data)

    def count_data(self, table_name):
        return self.table[table_name].count()

    def get_challenges(self):
        return self.get_data("challenges")

    def get_players(self):
        return self.get_data("players")

    def remove_challenges(self):
        return self.remove_data("challenges")

    def remove_players(self):
        return self.remove_data("players")

    def count_challenges(self):
        return self.count_data("challenges")

    def count_players(self):
        return self.count_data("players")


if __name__ == "__main__":
    database = Database()
