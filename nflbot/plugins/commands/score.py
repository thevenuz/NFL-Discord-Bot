import hikari
import lightbulb
from nflbot.models.score import GameStatus
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

        status, result = await ScoreImpl().get_live_score()

        if result:
            if status == GameStatus.Ongoing:
                embed= hikari.Embed(title=f"LIVE SCORE:", color=0Xff500a)
            
            else:
                embed= hikari.Embed(title=f"RECENT GAMES:", color=0Xff500a)
            msg = ""
            for game in result:
                
                msg= f'{msg}{game["home"].Team.Name} (**{game["home"].Score}**) - (**{game["away"].Score}** {game["away"].Team.Name})\n'

        embed.add_field(name=f"**RESULTS**", value=f"{msg}", inline=False)

        await ctx.respond(embed=embed)

    except Exception as e:
        logger.fatal("Exception occured in %s.live_score method for guild: %s", filePrefix, ctx.guild_id, exc_info=1)
        raise e



def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)  