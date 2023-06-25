import discord
#from discord.ext import commands
import os
import requests
import json
import random
from books import generate_books
from quotes import generate_quotes
from gita import generate_gita
from rizz import generate_rizz
from replit import db
from keepalive import keep_alive


client = discord.Client(intents=discord.Intents.all())

books = generate_books()

quotes = generate_quotes()

gita = generate_gita()

rizz = generate_rizz()

@client.event
async def on_ready():
  print('We have Logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(': u.hey'))
  print('Connected to bot: {}'.format(client.user.name))
  print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('u.hey'):
    await message.channel.send(
      "I am Übermensch. The protector of humanity. For more information: `u.info` "
    )

  if msg.startswith('u.info'):
    await message.channel.send(
      "**Übermensch** is a discord bot developed by Pratik and Harshith. The main aim for this bot is to send people positive messages on discord, and acknowledge them with various important philosophical concepts.\n\n **What is Übermensch?**\n It is the ideal superior man of the future who could rise above conventional morality to create and impose his own values, originally described by Friedrich Nietzsche in Thus Spoke Zarathustra (1883–5). \n For list of commands: `u.comm`"
    )

  if msg.startswith('u.comm'):
    await message.channel.send("The list of commands for this bot are:")
    await message.channel.send("`u.hey  -->  Greeting message` \n" +
      "`u.info  -->  Display the information about the bot` \n" +
      "`u.comm  -->  Display the list of commands` \n" +
      "`u.quotes  -->  Generate a random philosophical quote for the user` \n" +
      "`u.gita  -->  Generate a quote form The Gita` \n" +                      "`u.phil  -->  Explain a Philosophical concept to the user` \n" +
      "`u.books  -->  Suggest a book to the user` \n" +
      "`u.rizz  -->  Tell a love quote`")
  
  if msg.startswith('u.books'):
    await message.channel.send("Here's a book suggestion for you:")
    await message.channel.send("`"+books+"`")

  if msg.startswith('u.quotes'):
    await message.channel.send("Here's a beautiful quote for you:")
    await message.channel.send("`"+quotes+"`")

  if msg.startswith('u.gita'):
    await message.channel.send("Here's a quote from The Gita:")
    await message.channel.send("`"+gita+"`")

  if msg.startswith('u.mika'):
    await message.channel.send("`Mika is an ancient prehistoric 1 million years old worm.`")

  if msg.startswith('u.rizz'):
    await message.channel.send("`"+rizz+"`")

keep_alive()
client.run("TOKEN")
