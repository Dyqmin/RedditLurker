## Reddit Lurker
A discord bot for Reddit use from your discord server.


## Using cogs
If you just want to use any of cogs, remember to create reddit instance with [praw](https://praw.readthedocs.io/en/latest/) 
as an attribute of your bot class.
```py
import discord
from discord.ext import commands
import praw


bot = commands.Bot(command_prefix='!',
                   description='Bot name')
                   
# Creating read-only reddit instance
bot.reddit = praw.Reddit(client_id='Reddit API client ID',
                          client_secret='Reddit API secret',
                          user_agent='Reddit API app name')
```

Here is a short list of cogs:
- **Lurker** -  list of posts from provided subreddit
- **RandomImage** - images/memes. You can create new short commands by editing 
subreddits.json  
- **User** - User info