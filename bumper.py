import discord, os, time
from discord.ext import commands # https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html

# More improvements example: https://codeberg.org/SnowCode/auto-bump


# Uncomment the line below if you are wanting to host this on heroku and are using an environment variable to store the token.
token = os.getenv("USER_TOKEN")
# If you are using this on a server or your home pc uncomment the line below and put the discord token for the account you want it to auto bump on.
#token = "TOKEN"

botReceive = commands.Bot(command_prefix = "--", self_bot=True) # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=run#bot

@botReceive.event
async def on_ready():
   
    print("Discord.py library's Version: " + discord.__version__)
    print("Auto Bumper Is Online!") 
    print("USER_TOKEN: " + os.getenv("USER_TOKEN"))
   
    # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=run#discord.ext.commands.Bot.user
    print("Auto Bumper with Username: " + str(botReceive.user) + " | User ID: " + str(botReceive.user.id)) 
  
   # for server in botReceive.servers:
   #     member = server.get_member(botReceive.user.id)
   #     if member:
    print("The bot is available in these servers: ")
    for guild in botReceive.guilds:
        print(" Server Name: " + str(guild.name) + " Server ID: " + str(guild.id))

    
            #await botReceive.say(f"Server Name: {server.name}")
            #await botReceive.say(f"Server ID:   {server.id}")

    # Initializing channel where to send !d bump
    # Example: fetch_channel("855039765711552515")
    print ("DISCORD_SERVER_CHANNEL_ID: " + str(os.getenv("DISCORD_SERVER_CHANNEL_ID")))
    print ("DISCORD_SERVER_CHANNEL_NAME: #" + str(await botReceive.fetch_channel(os.getenv("DISCORD_SERVER_CHANNEL_ID"))))
    channel = await botReceive.fetch_channel(os.getenv("DISCORD_SERVER_CHANNEL_ID"));
   
    # Send --bla command automatically on the bot initialization.
    await channel.send("--bla")
   
    # Some Loop Testing
    while True:
        await channel.send("found channel")
        time.sleep(8125)
        
      
    print ("while loop is not running.")
        
        
    #server = bot.get_server(member.server)
    #channel = discord.utils.get(server.text_channels, name='general')
    
    #print(str(botReceive.user.fetch_channel))
    
    #https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20utils%20get#discord.utils.get
    # print(str(discord.utils.get(async botReceive.fetch_guild.text_channels, name="general")))
    #print(botReceive.get_channel('855039765711552515'))

@botReceive.command()
async def bla(ctx): # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context
    #while True:
    await ctx.send("!d bump")
    await ctx.send("Username: " + str(ctx.author))
    await ctx.send("Channel ID: " + str(ctx.channel.id))
    print("Auto Bumper Channel ID: " + str(ctx.channel.id))
    print("Auto Bumper bla command has been done in #" + str(ctx.channel) + " by " + str(ctx.author))
       #time.sleep(10) # 8125 seconds == 2 hours



botReceive.run(token, bot = False)
















@botReceive.event
async def on_connect():
    print("Auto Bumper successfully connected to Discord!")


    
@botReceive.event
async def on_disconnect():
    print("Auto Bumper: Discord.com is down or the Bot can not connect to the internet")
