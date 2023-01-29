import hikari
import lightbulb
from nflbot.logger.baselogger import BaseLogger

plugin = lightbulb.Plugin("HelpPlugin")

filePrefix = "nflbot.plugins.commands.help"

logger = BaseLogger().loggger_init()

@plugin.command
@lightbulb.command("help","help command", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx: lightbulb.SlashContext):
    try:
        logger.info("%s.help method invoked", filePrefix)

        embed = hikari.Embed(title="Help", color=0Xb3ffff)

        embed.add_field(name="ABOUT", value="A simple bot that can fetch livescore/recent games score of NFL league with a single command.", inline= False)
        embed.add_field(name="Commands:", value="`/livescore` : only command of the bot which is used for getting live score/ score of recently completed games", inline=False)
        embed.add_field(name="Support server:", value="")

        await ctx.respond(embed=embed)
    
    except Exception as e:
        logger.fatal("Exception occured in %s.help method", exc_info=1)
        raise e
    

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin) 