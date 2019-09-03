import discord
import os
from keep_alive import keep_alive
import wikipedia
import wikia 

###########################################################################

client = discord.Client()

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event


async def on_message(message):
      
  if message.author == client.user:
    return

  if "hey noba" in message.content.lower():
    await message.channel.send("What do you want?")

  if "Hello there." in message.content:
    await message.channel.send('General Kenobi. You are a bold one!')

  if "Capitalism" in message.content:
     await message.channel.send("Seize the means of production!")

  if "bye noba" in message.content.lower():
    await message.channel.send("See You Space Cowboy...")
    
  if "Trump" in message.content:
    await message.channel.send('#notmypresident')

  if "data dog" in message.content.lower():
    await message.channel.send('Seems that way')
  
  if "!wiki" in message.content.lower():
    words = message.content.split()
    searchCrit = words[1:]
    await message.channel.send(wiki_summary(searchCrit))

  if "!lotr" in message.content.lower():
    searchCrit = message.content[5:]
    await message.channel.send(LOTR_search(searchCrit))

  if message.content.startswith("!help"):
    await message.channel.send(help_info())


########################################################################

def wiki_summary(arg):
    definition = wikipedia.summary(arg, sentences=1, chars=100, 
    auto_suggest=True, redirect=True)
    return definition

#def anime_search(arg):
  
#  info = wikia.summary("anime", arg)

#  return info

def LOTR_search(arg):
  
  info = wikia.summary("lotr", arg)

  return info

def help_info():
  
  info = "( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°) \n hey noba: returns 'What do you want?' \n Hello there.: returns 'General Kenobi. You are a bold one!' \n Capitalism: returns 'Seize the means of production!' \n bye noba: returns 'See You Space Cowboy...' \n Trump: returns '#notmypresident' \n data dog: returns 'Seems that way' \n !wiki: searches wikipedia and returns summary \n !lotr: searches lotr fandom and returns summary \n !help: returns this mess \n ( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°)( ͡° ͜ʖ ͡°) "

  return info

##########################################################################

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
