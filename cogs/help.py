import discord
from discord.ext import commands

#Start of Help Cog
class Help_Cog(commands.Cog, name='Help Command'):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def help(self, ctx):
    #Start of Main Commands List
    helpcommands = discord.Embed(title = 'Bot Commands', description = 'Starting Commands for the Bot', colour = discord.Colour.blue())
    helpcommands.add_field(name="$play", value="A quick link to download the game", inline=False)
    helpcommands.add_field(name="$status", value="Checks server status", inline=False)
    helpcommands.add_field(name="$wiki", value="Displays a link to the game wiki", inline=False)
    helpcommands.add_field(name="$music", value="List of options for playing music", inline=False)
   
    await ctx.send(embed=helpcommands)
    print ('Help command used - No errors')
    #End of Main Commands List
  
#Define terminal text colour
class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'

#Define cog
def setup(bot):
  bot.add_cog(Help_Cog(bot))
  print (bcolours.YELLOW + 'Help Menus Loaded')