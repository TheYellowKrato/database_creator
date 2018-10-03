from tqdm import tqdm

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

    def get_sbs(self):
        challenges_data = []
        if self.connexion():
            sets = self.server.sbs_sets()
            for category in tqdm(sets['categories'], desc='Categories'):
                for set_data in tqdm(category['sets'], desc='Sets'):
                    challenges = self.server.sbs_set_challenges(set_data['setId'])['challenges']
                    for challenge in tqdm(challenges, desc='Challenges'):
                        challenge_id = challenge["challengeId"]
                        status = challenge["status"]
                        if status == 'NOT_STARTED':
                            challenge_details = self.server.sbs_start(challenge_id)
                        elif status == 'IN_PROGRESS':
                            challenge_details = self.server.sbs_squads(challenge_id)
                        elif status == 'COMPLETED':
                            print("Challenge already completed")
                            print(challenge)
                        if 'playerRequirements' in challenge_details:
                            challenge["playerRequirements"] = challenge_details["playerRequirements"]
                        challenge["squad"] = challenge_details["squad"]
                        challenges_data.append(challenge)
        return challenges_data
