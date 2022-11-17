import json
import os
from pathlib import Path
from nflbot.logger.baselogger import BaseLogger
from nflbot.models.config import Config

class ConfigUtil:
    def __init__(self) -> None:
        self.filePrefix="nflbot.utils.configutil"
        self.logger=BaseLogger().loggger_init()

    def load_config(self):
        try:
            self.logger.info("%s.load_config method invoked", self.filePrefix)

            rootDirectory=os.path.dirname(__file__)
            configDirectory=Path(rootDirectory).parents[1]

            filePath = os.path.join(configDirectory, "config", "config.json")

            with open(filePath) as f:
                result = json.load(f)

            config = Config(
                Token = result["Token"],
                PublicLogChannel = result["PublicLogChannel"],
                PrivateLogChannel = result["PrivateLogChannel"]
            )

            return config
        
        except Exception as e:
            self.logger.fatal("Exception occured in %s.load_config method", self.filePrefix, exc_info=1)
            raise e
        
# https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?limit=1000&dates=20221114-20221115