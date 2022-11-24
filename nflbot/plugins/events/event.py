import hikari
import lightbulb
from nflbot.logger.baselogger import BaseLogger
from nflbot.utils.configutil import ConfigUtil

plugin= lightbulb.Plugin("EventPlugin")

filePrefix = "nflbot.plugins.events.event"

logger = BaseLogger().loggger_init()

@plugin.listener(hikari.GuildJoinEvent)
async def guild_join_event(event: hikari.GuildJoinEvent):
    try:
        logger.info("%s.guild_join_event method invoked for server: %s", filePrefix, event.guild_id)

        publicLogChannel, privateLogChannel = await ConfigUtil().get_log_channels()

        if publicLogChannel:
            joinMsg = f"Bot joined a new server: {event.guild.name}"
            await plugin.bot.rest.create_message(publicLogChannel, joinMsg)

        if privateLogChannel:
            joinMsg= f"Bot joined a new server: {event.guild.name}, Id: {event.guild_id}"
            await plugin.bot.rest.create_message(privateLogChannel, joinMsg)

        
    
    except Exception as e:
        logger.fatal("Exception occured in %s.guild_join_event method for server: %s", filePrefix, event.guild_id, exc_info=1)
        raise e
    
@plugin.listener(hikari.GuildLeaveEvent)
async def guild_leave_event(event: hikari.GuildLeaveEvent):
    try:
        logger.info("%s.guild_join_event method invoked for server: %s", filePrefix, event.guild_id)

        publicLogChannel, privateLogChannel = await ConfigUtil().get_log_channels()

        if publicLogChannel:
            leaveMsg = f"Bot left server: {event.old_guild.name}"
            await plugin.bot.rest.create_message(publicLogChannel, leaveMsg)

        if privateLogChannel:
            leaveMsg= f"Bot left server: {event.old_guild.name}, Id: {event.guild_id}"
            await plugin.bot.rest.create_message(privateLogChannel, leaveMsg)

        
    
    except Exception as e:
        logger.fatal("Exception occured in %s.guild_join_event method for server: %s", filePrefix, event.guild_id, exc_info=1)
        raise e


def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)