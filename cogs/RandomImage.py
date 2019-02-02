import discord
from discord.ext import commands
import json

# Import short commands from json file
with open('subreddits.json') as config:
    subreddit_list = json.load(config)


class RandomImage:
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.bot.reddit
        self.subreddits_list = subreddit_list

    # Create command aliases from imported SUBREDDIT_LISTS
    aliases = list(subreddit_list.keys())

    @commands.command(name="", aliases=aliases)
    async def send_url(self, ctx):
        """
        Short command for random images.
        Bot sends URL of uploaded image in randomly selected post.
        It is limited to hardcoded aliases in subreddits.json
        """
        # TODO there is a chance for a blank response if the post has no link

        # Find subreddit based on provided command
        target_choice = self.subreddits_list[ctx.invoked_with]
        img_request = self.reddit.subreddit(target_choice).random().url

        response = discord.Embed()
        response.set_image(url=img_request)

        await ctx.send(embed=response)

    @commands.command()
    async def random(self, ctx, subreddit_name: str):
        """
        Sends URL of uploaded image in randomly selected post.
        """
        try:
            img_request = self.reddit.subreddit(subreddit_name).random().url

            response = discord.Embed()
            response.set_image(url=img_request)

            await ctx.send(embed=response)
        except Exception as e:
            print("Got ({}) error from  {}".format(e, ctx.invoked_with))
            await ctx.send("I could not find `{}`".format(subreddit_name))

    @commands.command()
    async def e(self, ctx):
        """
        Secret function. Sends a gif of baby elephant.
        Because everyone loves baby elephants.
        """
        elephant_gif = self.reddit.subreddit("babyelephantgifs").random().url
        await ctx.send(elephant_gif)


def setup(bot):
    bot.add_cog(RandomImage(bot))
