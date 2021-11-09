import discord   # import discord library
import os
os.system('cls||clear') # Clears the terminal on every run of the program

project_dir = os.path.dirname(__file__)   # Selecting the path to the folder from which we use picture (gif)
images_dir = os.path.join(project_dir, 'images')   # Selecting the folder from which we use picture (gif)
chewing_path = os.path.join(images_dir, 'chewing.gif')  # Selecting the picture (gif) from the folder

######## Replying to messages
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))  # On startup will display a message saying the bot has logged in the server

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):   # If the message starts with the word "hello", the bot will reply with "Hello"
    await message.channel.send('Hello!')

  if message.content.startswith('hi'): 
    await message.channel.send('Hi!')

  if message.content.startswith('sup'):
    await message.channel.send('Whats up!')

  if "ям" in message.content:   # If the message contains the word "ям (bulgarian for eat)" the bot will return a GIF
    await message.channel.send(file=discord.File(chewing_path))

  if "qm" in message.content:
    await message.channel.send(file=discord.File(chewing_path))

  if message.content.startswith('https://9gag.com/'):    # If the message starts with a link from the 9gag site the bot will return a message
    await message.channel.send('Awesome! Funny! HAHA!')

client.run('Here you put the token from discord app')