import configparser
from config.VarConfig import pageElementLocatorPath


class ParseConfigFile(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(pageElementLocatorPath, encoding="utf-8-sig")

    def getItemSection(self, sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        value = self.cf.get(sectionName, optionName)
        return value


if __name__ == '__main__':
    pc = ParseConfigFile()
    print(pc.getItemSection("Mol_login"))
    print(pc.getOptionValue("Mol_login", "loginPage.username"))