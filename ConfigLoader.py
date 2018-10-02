import json


class ConfigLoader(object):
    config = []

    def __init__(self, path="config.json"):
        self.load_conf_from_file(path)

    def load_conf_from_file(self, path):
        try:
            file = open(path, 'r')
            self.config = json.load(file)
            file.close()
        except IOError:
            print("File config.json not found")
            exit(-1)

    def get_property(self, property_name, account_number):
        if len(self.config) > account_number:
            if property_name in self.config[account_number]:
                return self.config[account_number][property_name]
            else:
                print("Can't find %d in config.json" % property_name)
                exit(-1)
        else:
            print("Account number invalid : %d/%d" % (account_number, len(self.config)))

    def get_number_of_accounts(self):
        return len(self.config)
