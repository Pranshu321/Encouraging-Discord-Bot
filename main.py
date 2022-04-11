from email import message
from urllib import response
from aiohttp import request
import discord
import requests
import os
from discord.ext import commands
import json
import random

bot = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "cry", "die", "sed", "WTF"]
angry_words = ["anger", "boiling", "fire", "💢", "😡", "🤬"]

starter_encounrge = [
    "Cheer up Buddy!",
    "Hang in there",
    "You are great person!",
    "Be Ready Tackle Problems!",
    "Be Calm and happy",
    "Be Cool Buddy",
    "The bad news is time flies",
    "Nothing is impossible",
]

anger_cool = [
    "Anger is the path to the dark side , so cool down and play with me!",
    "Anger makes you smaller",
    "Your mind is like this water my friend",
    "You're only hurting yourself Cool down!!",
]

with open("./config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["DISCORD_TOKEN"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + "   - " + json_data[0]["a"]
    return quote


@bot.event
async def on_ready():
    print("I am ready to use")


@bot.event
async def on_message(message):
    msg = message.content
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encounrge))

    if any(word in msg for word in angry_words):
        await message.channel.send(random.choice(anger_cool))

    if message.content.startswith("!hi"):
        await message.channel.send("Hello , This QuoMoto Bot")

    if message.content.startswith("!inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("!AddAngerMood"):

        await message.channel.send("New Anger Mood Added :) ")

    if message.content.startswith("!AddSedMood"):

        await message.channel.send("New Sed Mood Added :) ")

    if message.content.startswith("!AddAngerCool"):

        await message.channel.send("New Anger Cool Method Added :) ")

    if message.content.startswith("!AddSedBooster"):

        await message.channel.send("New Sed Enhancer Method Added :) ")


bot.run(TOKEN)
