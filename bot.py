import hikari
import lightbulb
from nflbot.utils.configutil import ConfigUtil

config = ConfigUtil().load_config()

bot = lightbulb.BotApp(token=config.Token)


bot.load_extensions_from('./nflbot/plugins/commands', must_exist=True)

bot.run(activity=hikari.Activity(name="NFL games", type=hikari.ActivityType.WATCHING))
