import discord
from discord.ext import commands

# Creating a read-only instance

# r = praw.Reddit(client_id='kfWixU70Pze-8A',
#                 client_secret='r5m3jgdLn1PwhhiTWoxnid_HRuI',
#                 user_agent='DircordBot Lurker')


TOKEN = 'NTM2Njc0ODAzMjYwODUwMjA2.Dyt9_A.gjShOwoHSHkvtZSFddUyz-Bj-h4'

bot = commands.Bot(command_prefix='?', description="description")



@bot.event
async def on_ready():
    print('Bot rd')


bot.run(TOKEN)
