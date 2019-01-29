import discord
from discord.ext import commands
from .utils.convert import t_ago


class Lurker:
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.bot.reddit
        self.URL = 'https://www.reddit.com'

    @commands.command()
    async def meme(self, ctx, type: str = "random"):
        """Sends a random meme."""
        """
        TODO memes on wholesomememes shittyadviceanimals MemeEconomy AdviceAnimals
        TODO parameter for new memes
        """
        meme_types = ("edgy", "dank", "random")
        await ctx.send(self.reddit.subreddit('edgymemes').random().url)

    @commands.command()
    async def posts(self, ctx, subreddit_name: str, sorting: str = "new"):
        """Sends list of threads on subreddit"""
        # TODO multiple subreddits
        # TODO limit parameter
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
                    post_url = self.URL + sub.permalink
                    post_author = sub.author
                    post_time = t_ago(sub.created_utc)
                    value = "[Link]({}) Posted by u/{} {}\n\u200B".format(post_url, post_author, post_time)

                    # Embed allows max 256 characters in name parameter
                    if len(sub.title) > 250:
                        name = sub.title[:250] + "..."
                    else:
                        name = sub.title
                    response.add_field(name=name, value=value, inline=False)

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