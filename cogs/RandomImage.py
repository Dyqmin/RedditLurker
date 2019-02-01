import discord
from discord.ext import commands
import json

class RandomImage:
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.bot.reddit
        self.URL = 'https://www.reddit.com'
        with open('utils/subreddits.json') as lst:
            self.subreddit_list = json.load(lst)

    # TODO import aliasow z pliku subreddit json
    @commands.command(name="m", aliases=)
    async def send_url(self, ctx):
        """
        Short command for random images. It is limited to hardcoded aliases
        """

        # Find subreddit based on provided command
        # Schema = {short_command: subreddit_name}
        request_target = {
            "m": "memes",
            "aww": "aww",
            "edgy": "edgymemes",
            "dank": "dankmemes",
            "e": "babyelephant gifs"}
        target_choice = request_target[ctx.invoked_with]
        await ctx.send(self.reddit.subreddit(target_choice).random().url)


def setup(bot):
    bot.add_cog(RandomImage(bot))