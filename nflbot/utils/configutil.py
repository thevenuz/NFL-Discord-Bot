import json
import os
import aiofiles
from pathlib import Path
from nflbot.logger.baselogger import BaseLogger
from nflbot.models.config import Config
from nflbot.models.settings import Settings 

class ConfigUtil:
    def __init__(self) -> None:
        self.filePrefix="nflbot.utils.configutil"
        self.logger=BaseLogger().loggger_init()

    def load_config(self) -> Config:
        try:
            self.logger.info("%s.load_config method invoked", self.filePrefix)

            rootDirectory=os.path.dirname(__file__)
            configDirectory=Path(rootDirectory).parents[1]

            filePath = os.path.join(configDirectory, "config", "botconfig.json")

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
        
    async def load_settings(self) -> Settings:
        try:
            self.logger.info("%s.load_settings method invoked", self.filePrefix)

            rootDirectory=os.path.dirname(__file__)
            configDirectory=Path(rootDirectory).parents[1]

            filePath = os.path.join(configDirectory, "config", "settings.json")

            async with aiofiles.open(filePath, mode="r") as f:
                result = json.loads(await f.read())

            settings = Settings(ApiEndpoint=result["ApiEnpoint"])

            return settings
        
        except Exception as e:
            self.logger.fatal("Exception occured in %s.load_settings method", self.filePrefix, exc_info=1)
            raise e
        
    
    async def get_log_channels(self) -> tuple[str, str]:
        try:
            self.logger.info("%s.get_log_channels method invoked", self.filePrefix)

            config = self.load_config()

            return config.PublicLogChannel, config.PrivateLogChannel
        
        except Exception as e:
            self.logger.fatal("Exception occured in %s.get_log_channels method", self.filePrefix, exc_info=1)
            raise e
        