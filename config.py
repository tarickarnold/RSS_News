from dataclasses import dataclass
import logging
import logging.config
import logging.handlers
import os
import toml

@dataclass
class RSSList:
    websites: list

@dataclass
class Bot:
    name: str
    environment: str
    email: str

class Config:

    def __init__(self, config_file) -> None:
        self.logger = logging.getLogger(__name__)
        self.file: any = config_file
        self.rsslist: list[str] = []
        self.loadTomlConfigs()

    def loadTomlConfigs(self) -> None:
        if not os.path.exists(self.file):
            self.logger.critical(f"Could not find {self.file}. Please locate or create file.")
            raise Exception(f"Could not find {self.file}. Please locate or create file.")
        else:
            with open(file= self.file, mode= 'r') as file:
                self.config: dict[str, any] = toml.load(f= file)
                self.logger.info(f"{self.file} found!")
    
    def parseConfigs(self) -> None:
        self.name: str = self.config['bot']['name']
        self.env: str = self.config['bot']['environment']
        self.rsslist: list[str] = self.config['bot']['urls']['websites']
        self.logger.info("Parsing complete")

    def __getitem__(self, item) -> any:
        return self.config[item]

def main() -> None:
    dir_name: str = os.path.dirname(p=__file__)
    config_file: str = os.path.join(dir_name, "config.toml")
    Config(config_file= config_file)

if __name__=="__main__":
    main()