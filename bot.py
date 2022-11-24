import hikari
import lightbulb
from nflbot.utils.configutil import ConfigUtil

config = ConfigUtil().load_config()

bot = lightbulb.BotApp(token=config.Token)


bot.load_extensions_from('./nflbot/plugins/commands', must_exist=True)
bot.load_extensions_from('./nflbot/plugins/events', must_exist=True)
bot.load_extensions_from('./nflbot/plugins/errorhandler', must_exist=True)


@bot.listen(hikari.StartedEvent)
async def msg(event):
    print("bot has started...")


bot.run(activity=hikari.Activity(name="NFL games", type=hikari.ActivityType.WATCHING))

