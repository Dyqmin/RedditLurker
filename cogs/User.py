import discord
from discord.ext import commands



class UserInfo:
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.bot.reddit
        self.URL = 'https://www.reddit.com'

    @commands.command()
    async def user(self, ctx, user_name: str):
        """Sends user details"""
        await ctx.send("Foo")


def setup(bot):
    bot.add_cog(UserInfo(bot))