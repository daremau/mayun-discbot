import discord
from discord.client import Client
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print(f"{client.user.name} is ready.")

@client.command()
async def check_user_in_channel(ctx):
    voice_state = ctx.author.voice

    if voice_state is None:
        return await ctx.send('Conectate al canal')

@client.command()
async def play(ctx, url):
    check_user_in_channel(ctx)    
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
    print(f"{ctx.author.name} esta escuchando {info['title']}")
    
@client.command()
async def leave(ctx):
    check_user_in_channel(ctx)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send('<:memperra:784921504478527508>')
    else:
        await ctx.send('???????')

@client.command()
async def pause(ctx):
    check_user_in_channel(ctx)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('????????')

@client.command()
async def resume(ctx):
    check_user_in_channel(ctx)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('???????')

@client.command()
async def stop(ctx):
    check_user_in_channel(ctx)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send('<:TAVYRON:821417147435712573>')

@client.command(name="pilin")
async def pilin(ctx):
    await ctx.send("pilin")

client.run('OTAxOTgzNDg0MDI4MDAyMzM1.YXXzlA.PoYr8cwWqAjoNYemG2wAGktjjf0')
