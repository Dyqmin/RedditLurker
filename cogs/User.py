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

        redditor = self.reddit.redditor(user_name)
        try:
            karma = redditor.link_karma + redditor.comment_karma
            profile_link = f"https://www.reddit.com/user/{redditor.name}"

            response = discord.Embed(title=f"u/{redditor.name}",
                                     description=f"[Check]({profile_link})",
                                     color=0xff7011)
            response.set_thumbnail(url=redditor.icon_img)

            response.add_field(name="Karma", value=karma, inline=False)
            await ctx.send(embed=response)
        except Exception as e:
            await ctx.send("User not found")


def setup(bot):
    bot.add_cog(UserInfo(bot))