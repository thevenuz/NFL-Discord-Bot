# NFL-Discord-Bot

A Discord bot that can fetch livescores of any ongoing NFL games.

### How to use the bot?
The bot has a single command `/livescore`. If there are any live games occuring when this command is used, the bot will give the live score results of all the ongoing games. If there are no live games happening when this command is used, the bot will give the score results of the three recent games.

### About the code
The bot uses ESPN's API to fetch the live score details. The code does nothing much other than filtering out the results from ESPN API.

### Built using Hikari and Hikari-Lightbulb libraries
