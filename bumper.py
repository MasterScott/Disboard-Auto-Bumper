import os
import discord

TOKEN = "ODQ3Nzc5OTU5MzU1NDczOTIz.YLDCnQ.eh7bmOZKh2fYVEUnFq6omizHFHU"
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
