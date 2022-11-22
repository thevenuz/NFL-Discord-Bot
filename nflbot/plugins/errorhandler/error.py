import hikari
import lightbulb
from nflbot.logger.baselogger import BaseLogger

filePrefix = "nflbot.plugins.errorhandler.error"
logger = BaseLogger().loggger_init()

async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    try:
        logger.info("%s.on_error method invoked for guild: %s for command: %s", filePrefix, event.context.guild_id, event.context.command.name)

        embed= hikari.Embed(title=f"🛑 An error occurred with the `{event.context.command.name}` command.", color=0xFF0000)

        if isinstance(event.exception,lightbulb.BotMissingRequiredPermission):
            logger.error("Error due to bot missing permissions in server: %s", event.context.guild_id)

            embed.add_field(name="Error:", value="Bot's missing permissions. Please check if the bot has SEND MESSAGES and SEND EMBEDS permission.")

        elif isinstance(event.exception,lightbulb.CommandNotFound):
            logger.error("Error due to invalid command in server: %s", event.context.guild_id)

            embed.add_field(name="Error:", value=f"Invalid command.")

        else:
            logger.fatal("Some unknown exception has occured for command %s in server: %s", event.context.command.name, event.context.guild_id, exc_info=1)

            embed.add_field(name="Error:", value=f"Unknown error. Please try the command again or contact the Dev if the error persists.")
           
        await event.context.respond(embed=embed)

    except Exception as e:
        logger.fatal("Exception occured in %s.on_error method for guild: %s for command: %s", filePrefix, event.context.guild_id, event.context.command.name, exc_info=1)
        raise e
    


def load(bot):
    bot.subscribe(lightbulb.CommandErrorEvent,on_error)

def unload(bot):
    bot.unsubscribe(lightbulb.CommandErrorEvent,on_error)