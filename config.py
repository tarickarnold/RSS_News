from dataclasses import dataclass
import os
import toml
import sys

@dataclass
class RSSList:
    websites: list

@dataclass
class Bot:
    name: str
    environment: str
    email: str

class Config:

    def __init__(self, target_file) -> None:
        self.file: any = target_file
        self.rsslist: list[str] = []
        self.loadTomlConfigs()
        
    def loadTomlConfigs(self) -> None:
        if not os.path.exists(path= self.file):
            raise Exception(f"Could not find {self.file}. Please locate or create file.")
        else:
            with open(file= self.file, mode= 'r') as file:
                self.config: dict[str, any] = toml.load(f= file)
            print(self.config)
    
    def parseConfigs(self) -> None:
        self.name: str = self.config['bot']['name']
        self.env: str = self.config['bot']['environment']
        self.rsslist: list[str] = self.config['bot']['urls']['websites']

def main() -> None:
    dir_name: str = os.path.dirname(p=__file__)
    target_file: str = os.path.join(dir_name, "config.toml")
    config = Config(target_file= target_file)
    config.parseConfigs()

if __name__=="__main__":
    main()