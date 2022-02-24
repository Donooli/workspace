import configparser

class ConfigReader:

    def __init__(self,conf_file):
        self.config = configparser.ConfigParser()
        self.conf_file = conf_file
        self.section = []
        self.result = dict()

    def read_file(self):
        self.config.read(self.conf_file)
        self.section = self.config.sections()

    def extract(self):
        self.read_file()
        for i in self.section:
            self.result[i] = self.config[i]['interval']
        return self.result

'''if __name__ == '__main__':
    print(ConfigReader('conf.txt').extract())'''
