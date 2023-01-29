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
            embed= hikari.Embed(color=0Xb3ffff)
            if status == GameStatus.Ongoing:
                title= "LIVESCORE"
            
            else:
                title= "RECENT GAMES"

            msg = ""
            for game in result:
                
                msg= f'{msg}\n\n**{game["home"].Team.DisplayName} ({game["home"].Score})** - **({game["away"].Score}) {game["away"].Team.DisplayName}**'

            embed.add_field(name=f"{title}", value=f"{msg}", inline=False)

            await ctx.respond(embed=embed)

        else:
            await ctx.respond(embed=hikari.Embed(title=f"Error!", description=f"Bot could not find any live games or recent scores!", color=0xFF0000))

    except Exception as e:
        logger.fatal("Exception occured in %s.live_score method for guild: %s", filePrefix, ctx.guild_id, exc_info=1)
        raise e



def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)  