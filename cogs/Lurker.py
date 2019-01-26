import discord
from discord.ext import commands
import praw
import json

# Create read-only reddit instance


class Lurker:
    def __init__(self, bot):
        with open('config.json') as config:
            self.config_data = json.load(config)
        self.bot = bot
        self.reddit = praw.Reddit(client_id=self.config_data['reddit_client_id'],
                                  client_secret=self.config_data['reddit_client_secret'],
                                  user_agent=self.config_data['reddit_user_agent'])

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def meme(self, ctx):
        await ctx.send(self.reddit.subreddit('dankmemes').random().url)


def setup(bot):
    bot.add_cog(Lurker(bot))