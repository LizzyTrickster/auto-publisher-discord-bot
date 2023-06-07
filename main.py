#!usr/bin/env python3

import discord
import os
from discord import Client

intents = discord.Intents.default()

bot = Client(intents=intents, status="publishing your messages")

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.guild and message.channel.is_news():
        try:
            await message.publish()
        except:
            pass
bot.run( os.getenv("TOKEN") )
