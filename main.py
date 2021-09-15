import discord
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print(f"{client.user.name} is ready.")

'''@client.event
async def on_voice_state_update(self, member, before, after):
    
    if not member.id == self.bot.user.id:
        return

    elif before.channel is None:
        voice = after.channel.guild.voice_client
        time = 0
        while True:
            await asyncio.sleep(1)
            time = time + 1
            if voice.is_playing() and not voice.is_paused():
                time = 0
            if time == 600:
                await voice.disconnect()
            if not voice.is_connected():
                break'''

@client.command()
async def play(ctx, url):
    try:
        voice_channel = ctx.author.voice.channel
        
        if ctx.voice_client is None:
            await voice_channel.connect()
       
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        
        await ctx.send('<:Buenardo:784888763343306762>')
        
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'] [0] ['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)
    except:
        print('no se encuentra ffmpeg')


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send('<:memperra:784921504478527508>')
    else:
        await ctx.send('???????')


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('????????')


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('???????')


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send('<:TAVYRON:821417147435712573>')

client.run('ODg3NDU5MTU5MDUyNzgzNjY3.YUEcvw.n4Li5ppg16uU6DVLfSGjN4jOmEM')