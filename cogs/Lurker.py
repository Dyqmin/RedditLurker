import discord
from discord.ext import commands
import praw
import json


class Lurker:
    def __init__(self, bot):
        with open('config.json') as config:
            self.config_data = json.load(config)
        self.bot = bot
        # Creating read-only reddit instance
        self.reddit = praw.Reddit(client_id=self.config_data['reddit_client_id'],
                                  client_secret=self.config_data['reddit_client_secret'],
                                  user_agent=self.config_data['reddit_user_agent'])

    @commands.command()
    async def meme(self, ctx):
        """Sends a random meme."""
        await ctx.send(self.reddit.subreddit('edgymemes').random().url)

    @commands.command()
    async def posts(self, ctx, subreddit_name: str, sorting: str = "new"):
        """Sends list of threads on subreddit"""
        # TODO multiple subreddits
        sorting_options = (
                            "hot",
                            "new",
                            "random",
                            "rising",
                            "top"
                          )
        # Check if sorting option exists
        if sorting in sorting_options:
            try:
                # Create a sorting attribute with provided option
                sub_request = getattr(self.reddit.subreddit(subreddit_name), sorting)
                response = ''
                for submission in sub_request(limit=10):
                    response += "[{}]({})\n".format(submission.title, submission.url)
                embed = discord.Embed(description='Found threads:\n{}'.format(response))
                await ctx.send(embed=embed)
            except Exception as e:
                return await ctx.send("Got `{}` error. Subreddit doesn't exist or is private".format(e))
        else:
            return await ctx.send("I could not find **{}** sorting option".format(sorting))

    @posts.error
    async def posts_handler(self, ctx, error):
        """Error Handler for <posts> command"""
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'subreddit_name':
                await ctx.send("You need to provide a subreddit!")

    @commands.command()
    async def ele(self, ctx):
        """ Secret function. Sends a random gif of a baby elephant.
        Because everyone loves baby elephants"""
        await ctx.send(self.reddit.subreddit('babyelephantgifs').random().url)


def setup(bot):
    bot.add_cog(Lurker(bot))