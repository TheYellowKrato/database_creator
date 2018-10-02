from ConfigLoader import ConfigLoader
from Server import Server


class SbcParser:
    config_loader = ConfigLoader()
    server = Server()

    def __init__(self):
        pass

    def connexion(self):
        if self.config_loader.get_number_of_accounts() > 0:
            login = self.config_loader.get_property("login", 0)
            password = self.config_loader.get_property("password", 0)
            pass_phrase = self.config_loader.get_property("passPhrase", 0)
            platform = self.config_loader.get_property("platform", 0)

            return self.server.connexion(login, password, pass_phrase, platform)
        else:
            print("No account found into config.json please follow config_example")
            exit()

    def get_sbcs(self):
        challenges = []
        if self.connexion():
            sets = self.server.sbs_sets()
            for category in sets['categories']:
                for set_data in category['sets']:
                    challenge = self.server.sbs_set_challenges(set_data['setId'])['challenges']
                    print("New sbs found")
                    challenges.append(challenge)
        return challenges
