import os
import discord
from discord.ext import commands, tasks
from keep_alive import keep_alive
from itertools import cycle

#Define terminal colours
class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'

#Define discord bot token
TOKEN = os.environ['TOKEN']

#Define bot prefix & remove default help function
bot = commands.Bot(command_prefix='$', case_insensitive=True)
bot.remove_command('help')

#Loads cogs
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

  else:
    print(bcolours.RED + f'Unable to load {filename[:-3]}')

#Define rotating status
status = cycle([
  'Game - $help to start', 
  'Game - $status for game info',
  'Game - $wiki for the wiki',
  'Game - $play to play game',
])

#Loops defined status
@tasks.loop(seconds=30)
async def status_swap():
  await bot.change_presence(activity=discord.Game (name=next(status)))

#Defines on ready function
@bot.event
async def on_ready():
  status_swap.start()
  print('We have logged in as {0.user}'.format(bot))

#Logs messages in discord to file
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.author.bot: return

  guild = message.guild
  if guild:
      path = "chatlogs/{}.txt".format(guild.name)  
      with open(path, 'a+') as f:
          print("{0.author.name} : {0.content}".format(message), file=f)
      await bot.process_commands(message)

#Keeps bot alive  
keep_alive()

#Runs bot
bot.run(TOKEN)
