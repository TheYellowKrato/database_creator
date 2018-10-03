import time
import types

import fut


class Server(object):
    def __init__(self):
        self.session = None

    def __getattribute__(self, attr):
        no_need_to_delay = ["__init__", "__module__", "__dict__", "__weakref__", "__doc__",
                            "connexion"]
        method = object.__getattribute__(self, attr)
        if type(method) == types.MethodType:
            if attr not in no_need_to_delay:
                time.sleep(5)
        return method

    def connexion(self, login, password, pass_phrase, platform):
        try:
            print("Trying to log in %s" % login)
            self.session = fut.Core(login, password, pass_phrase, platform)
            print("Connected")
            return True
        except Exception as e:
            print(e.reason)
            return False

    def sbs_sets(self):
        return self.session.sbsSets()

    def sbs_set_challenges(self, set_id):
        return self.session.sbsSetChallenges(set_id)

    def sbs_squads(self, challenge_id):
        return self.session.sbsSquad(challenge_id)

    def sbs_start(self, challenge_id):
        return self.session.sbsStart(challenge_id)
