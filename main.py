from email import message
from urllib import response
from aiohttp import request
import discord
import requests
import os
from discord.ext import commands
import json
import random
import sys
import traceback
import asyncio
from distutils import extension

bot = discord.Client()


with open("./config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["DISCORD_TOKEN"]

with open("./mood.json", "r") as moodjsonFile:
    moodData = json.load(moodjsonFile)
    sedi = moodData["sad_words"]
    anger = moodData["angry_words"]
    sedi_en = moodData["starter_encounrge"]
    anger_en = moodData["anger_cool"]


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
    if any(word in msg for word in sedi):
        await message.channel.send(random.choice(sedi_en))

    if any(word in msg for word in anger):
        await message.channel.send(random.choice(anger_en))

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
