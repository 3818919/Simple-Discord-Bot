import discord
from discord.ext import commands
import socket
import pandas as pd

class Server_Status(commands.Cog, name='Server_Status'):

  def __init__(self, bot):
    self.bot = bot

  #Server Status Check
  @commands.command()
  async def status(self, ctx):
    gameowner = '<@188605352223309824>' #Discord ID of game owner
    game = 'Game Name' #Game Name
    onlineplayersurl = 'URL' #Web Table of Online Players
    ip = "192.168.0.1" #Game IP
    port = 8078 #Game Port
    retry = 5
    timeout = 3
    def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

    def checkHost(ip, port):
        ipup = False
        for i in range(retry):
          if isOpen(ip, port):
                        ipup = True
                        break
          else:

                        return
        return ipup

    if checkHost(ip, port):
      try:
        #Scrapes online players from website - Table format
        url = onlineplayersurl
        PlayersOnline = pd.read_html(url)[0]
        PlayersOnline.index += 1
        Lists = PlayersOnline.head(100) #Only shows up to 100 items
        People = Lists.Name
        Names = People.values
        PeopleList = '\n'.join(Names)
        playerson = len(Names)
        
        #Status Embed start
        serveron = discord.Embed(title = 'Server Online',description = f'I have just checked and {game} is online', colour = discord.Colour.green())
        serveron.add_field(name='%s Players Online' % playerson, value=PeopleList, inline=False)
        #Embed End

        await ctx.send(embed=serveron)

        #Prints server check & results to terminal
        print (bcolours.GREEN + f'Server check - {game} is online with {playerson} players online') 
        return
        
      
      except:
        #Zero Players Embed start
        ZeroPlayers = discord.Embed(title = 'Server Online',description = f'I have just checked and {game} is online', colour = discord.Colour.green())
        ZeroPlayers.add_field(name="0 Players Online", value="There are no players online.", inline=False)
        await ctx.send(embed=ZeroPlayers)  
        #Embed end

        #Prints server check & result to terminal
        print (f'Server check - Server Online with 0 players.')
      return
    
      
    else:
      #Embed Start - Server offline message, bot @'s owner
      serverdown = discord.Embed(title = 'Server Offline', colour = discord.Colour.red())
      serverdown.add_field(name=f'The server is Down! OMG everyone {gameowner}, we are all gonna die!', value=gameowner, inline=False)
      await ctx.send(embed=serverdown)
      #Embed end

      #prints server check & result to terminal
      print (f'Server Check - Server Offline')
      return
    return  

#Defines terminal text colours   
class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'

#Defines status cog
def setup(bot):
  bot.add_cog(Server_Status(bot))
  print (bcolours.YELLOW + 'Server Status Addon Loaded')