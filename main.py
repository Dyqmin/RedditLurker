import discord
from discord.ext import commands
import json
import praw


# Read config parameters
with open('config.json') as config:
    config_data = json.load(config)

bot = commands.Bot(command_prefix=config_data["prefix"],
                   description='Reddit Lurker')

# Creating read-only reddit instance
bot.reddit = praw.Reddit(client_id=config_data['reddit_client_id'],
                          client_secret=config_data['reddit_client_secret'],
                          user_agent=config_data['reddit_user_agent'])

# List of cogs
features = ['cogs.Lurker', 'cogs.RandomImage', 'cogs.User']


@bot.event
async def on_ready():
    print('Bot rd')
    for extension in features:
        try:
            bot.load_extension(extension)
            print(f"Extension {extension} loaded!")
        except Exception as e:
            exc = '{} cannot be loaded. [{}]'.format(extension, e)
            print(exc)

if __name__ == '__main__':
    bot.run(config_data["token"])
