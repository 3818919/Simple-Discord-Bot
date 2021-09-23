import discord
from discord.ext import commands
import youtube_dl

class music_cog(commands.Cog, name='Music Cog'):

  def __init__(self, bot):
    self.bot = bot

  #Music commands list
  @commands.command()
  async def music(self, ctx):
    music = discord.Embed(title = 'Bot Commands', description = 'Starting Commands for the Bot', colour = discord.Colour.blue())
    music.add_field(name="$listen `url`", value="Play's a youtube link as audio in the voice chat.", inline=False)
    music.add_field(name="$pause + $resume", value="Player controls", inline=False)
    music.add_field(name="$stop", value="Stops the music player", inline=False)
    music.add_field(name="$dc", value="Disconnects the bot from the voice channel", inline=False)

    await ctx.send(embed=music)
    print ('Help command check')

  #Stop music Command
  @commands.command()
  async def stop(self,ctx):
    author = ctx.author.mention
    vc = ctx.voice_client
    vc.stop()
    await ctx.send(f'Music stopped by **{author}**')
  
  #Disconnect bot function
  @commands.command()
  async def dc(self,ctx):
    vc = ctx.voice_client
    await vc.disconnect()

  #Play music command - Uses youtube URL as argument
  @commands.command()
  async def listen(self,ctx,url):
    if ctx.author.voice is None:
      await ctx.send("You're not in a voice channel!", delete_after = 10)
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
    vc = ctx.voice_client
    vc.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format' : 'bestaudio'}
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url,download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
  
  #Pause Music command
  @commands.command()
  async def pause(self,ctx):
    await ctx.voice_client.pause()
    await ctx.send("Music paused", delete_after = 10)

  @commands.command()
  async def resume(self,ctx):
    await ctx.voice_client.resume()
    await ctx.send("Music resumed", delete_after = 10)
  
  #Error Handeling
  @stop.error
  async def stop_error(self, ctx, error):
    print ('Error when trying to stop music.')
  
  @listen.error
  async def play_error(self, ctx, error):
    print ('Error when trying to play music.')
  
  @dc.error
  async def dc_error(self, ctx, error):
    print ('Error when trying to DC bot.')
  
  @pause.error
  async def pause_error(self, ctx, error):
    print ('Error when trying to pause music.')
  
  @resume.error
  async def status_error(self, ctx, error):
    print ('Error when trying to resume music.')

#Define terminal text colours
class bcolours:
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'

#Define music cog
def setup(bot):
  bot.add_cog(music_cog(bot))
  print (bcolours.GREEN + 'Music Addon Loaded')