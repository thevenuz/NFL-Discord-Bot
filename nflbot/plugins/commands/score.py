import hikari
import lightbulb
from nflbot.logger.baselogger import BaseLogger
from nflbot.pluginsimpl.commands.scoreimpl import ScoreImpl

plugin= lightbulb.Plugin("ScorePlugin")

filePrefix="nflbot.plugins.commands.score"

logger=BaseLogger().loggger_init()


@plugin.command
@lightbulb.command("livescore","check live score of the ongoing games", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def live_score(ctx: lightbulb.SlashContext) -> None:
    try:
        logger.info("%s.live_score method invoked for guild: %s", filePrefix, ctx.guild_id)

        result = await ScoreImpl().get_live_score()

    except Exception as e:
        logger.fatal("Exception occured in %s.live_score method for guild: %s", filePrefix, ctx.guild_id, exc_info=1)
        raise e



def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)  