import discord
from discord.ext import commands
import json

# Read config parameters
with open('config.json') as config:
    config_data = json.load(config)

bot = commands.Bot(command_prefix=config_data["prefix"],
                   description="Reddit Lurker")

features = ['cogs.Lurker']

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
