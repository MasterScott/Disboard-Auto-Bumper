# bot.py
import os
import discord

TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
