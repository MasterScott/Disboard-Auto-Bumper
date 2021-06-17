import discord, os, time
from discord.ext import commands


# Uncomment the line below if you are wanting to host this on heroku and are using an environment variable to store the token.
token = os.getenv("USER_TOKEN")
# If you are using this on a server or your home pc uncomment the line below and put the discord token for the account you want it to auto bump on.
#token = "TOKEN"

bot = commands.Bot(command_prefix = "--", self_bot=True)

@bot.event
async def on_ready():
    print("Auto Bumper Is Online!")
    print(await bot.fetch_user(token))
    
@bot.event
async def on_connect():
    print("Auto Bumper successfully connected to Discord!")


    
@bot.event
async def on_disconnect():
    print("Auto Bumper: Discord.com is down or the Bot can not connect to the internet")


@bot.command()
async def bla(ctx):
    while True:
        await ctx.send("!d bump")
        await ctx.send(ctx.author)
        time.sleep(8125)



bot.run(token, bot = False)
