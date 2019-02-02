import discord
from discord.ext import commands
from .utils.convert import t_ago


class Lurker:
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.bot.reddit
        self.URL = 'https://www.reddit.com'

    @commands.command(name='posts', aliases=['threads'])
    async def show_posts(self, ctx, subreddit_name: str, sorting: str = "new", posts_limit: int = 10):
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
                response = discord.Embed(title='Found threads',
                                         description='r/{} sorted by {}'.format(subreddit_name, sorting),
                                         color=0xff7011)

                if posts_limit > 25:
                    posts_limit = 25
                    response.title += ' [ Posts limit reduced to maximum (25) ]'

                for sub in sub_request(limit=posts_limit):
                    post_url = self.URL + sub.permalink
                    post_author = sub.author
                    post_time = t_ago(sub.created_utc)

                    # Create description of post with link, author and time
                    value = "[Link]({}) Posted by u/{} {}\n\u200B".format(post_url, post_author, post_time)

                    # Embed allows max 256 characters in name parameter
                    if len(sub.title) > 250:
                        name = sub.title[:250] + "..."
                    else:
                        name = sub.title
                    response.add_field(name=name, value=value, inline=False)

                await ctx.send(embed=response)
            except Exception as e:
                print("Got ({}) error from  {}".format(e, ctx.invoked_with))
                return await ctx.send("I could not find `{}`".format(subreddit_name))
        else:
            return await ctx.send("I could not find **{}** sorting option".format(sorting))

    @show_posts.error
    async def posts_handler(self, ctx, error):
        """Error Handler for <posts> command"""
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'subreddit_name':
                await ctx.send("You need to define  a subreddit!")


def setup(bot):
    bot.add_cog(Lurker(bot))