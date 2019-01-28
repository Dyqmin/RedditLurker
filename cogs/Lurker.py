import discord
from discord.ext import commands
import praw
import json
from .utils.convert import t_ago

class Lurker:
    def __init__(self, bot):
        with open('config.json') as config:
            self.config_data = json.load(config)
        self.bot = bot
        # Creating read-only reddit instance
        self.reddit = praw.Reddit(client_id=self.config_data['reddit_client_id'],
                                  client_secret=self.config_data['reddit_client_secret'],
                                  user_agent=self.config_data['reddit_user_agent'])
        self.URL = 'https://www.reddit.com'

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
                # Create a sorting attribute with a selected option
                sub_request = getattr(self.reddit.subreddit(subreddit_name), sorting)
                response = discord.Embed(title="Found threads",
                                         description="r/{} sorted by {}".format(subreddit_name, sorting),
                                         color=0xff7011)
                for sub in sub_request(limit=10):
                    value = "[Link]({}) Posted by u/{} {}\n\u200B".format(self.URL+sub.permalink, sub.author,
                                                                          t_ago(sub.created_utc))
                    if len(sub.title) > 250:
                        name = sub.title[:250]
                    else:
                        name = sub.title
                    response.add_field(name=name,
                                       value=value,
                                       inline=False)
                await ctx.send(embed=response)
            except Exception as e:
                return await ctx.send("Got `{}` error.".format(e))
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