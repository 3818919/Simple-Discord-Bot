import discord
from discord.ext import commands

class Support_Cog(commands.Cog, name='Support'):

  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def support(self, ctx):
    #Donate to Game
    title = 'Support the Server' #Post Title
    subtitle = 'Help us keep the game going.' #Post Sub-title
    donatelink = 'url' #Donation page URL for players to follow
    thumbnail = 'url' #Thumbnail image URL
    description = 'All funds go towards our server hosting & maintenance, internet connection and the website/forum domain.' #Post Description

    #Start of Embed
    Donate=discord.Embed(title=title, url=donatelink, description=subtitle, color=0xfac400)
    Donate.set_thumbnail(url=thumbnail)
    Donate.set_footer(text=description)
    await ctx.send(embed=Donate)
    #End of Donate Link
  


  @commands.command()
  async def wiki(self, ctx):
    gamename = 'Game Name Wiki' #Name of your game's wiki
    wikiurl = 'URL' #URL of your game's wiki
    description = 'All information about our game can be found here.' #Post description
    thumbnail = 'URL' #Post thumbnail URL

    ##Embed Start
    wiki = discord.Embed(title = gamename,url = wikiurl, description = description, colour = discord.Colour.blue())
    wiki.set_thumbnail(url=thumbnail)
    await ctx.send(embed=wiki)
    ##Embed End
  


  @commands.command()
  async def play(self, ctx):
    gamename = 'Game Name' #Name of the game
    description = 'Click here to download the game' #Post description
    client_download = 'URL' #Game download link
    thumbnail = 'URL' #Thumbnail image URL

    #Embed Start
    Play=discord.Embed(title = gamename, url=client_download, description = description, color=0xfac400)
    Play.set_thumbnail(url = thumbnail)
    await ctx.send(embed=Play)
    #Embed End

#Define terminal text colours
class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'

#Define Support Cog
def setup(bot):
  bot.add_cog(Support_Cog(bot))
  print (bcolours.YELLOW + 'Support Addon Loaded')
