import discord
from discord.utils import get
from discord.ext import commands
from datetime import datetime, timedelta
import itertools
from song import songAPI





# wrapper / decorator

message_lastseen = datetime.now()
message2_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!',help_command=None)


songInstance = songAPI()



@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("WTF {0}".format(par))


@bot.command()
async def help(ctx):
    # help
    # test
    # send
    emBed = discord.Embed(title="Tutorial Bot help", description="All available bot commands", color=0x42f5a7)
    emBed.add_field(name="help", value="Get help command", inline=False)
    emBed.add_field(name="test", value="Respond messaeg that you've send", inline=False)
    emBed.add_field(name="help", value="Send Hello message to user", inline=False)
    emBed.set_thumbnail(url='https://play-lh.googleusercontent.com/0oO5sAneb9lJP6l8c6DH4aj6f85qNpplQVHmPmbbBxAukDnlO7DarDW0b-kEIHa8SQ')
    emBed.set_footer(text='WTF', icon_url='https://play-lh.googleusercontent.com/0oO5sAneb9lJP6l8c6DH4aj6f85qNpplQVHmPmbbBxAukDnlO7DarDW0b-kEIHa8SQ')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def send(ctx):
    print(ctx.channel.send)
    await ctx.channel.send('Hello')


@bot.event #async/await
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content == '!joy':
        await message.channel.send(str(message.author.name)+ 'Hello')
        #loging
        print('{0} เรียกนาย ชื่อ ตอน {1} และเรียกได้อีกที่ {2}'.format(message.author.name,datetime.now(),message_lastseen))
    elif message.content == '!Joy':
        await message.channel.send(str(message.author.name)+ 'Hello')
        #loging
        print('{0} เรียกนาย ชื่อ ตอน {1} และเรียกได้อีกที่ {2}'.format(message.author.name,datetime.now(),message_lastseen))
    elif message.content == 'นายชื่ออะไร' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds=10)
        await message.channel.send('เสือกจาก' + str(bot.user.name))
        #loging
        print('{0} เรียกนาย ชื่อ ตอน {1} และเรียกได้อีกที่ {2}'.format(message.author.name,datetime.now(),message_lastseen))
    elif message.content == 'ผมชื่ออะไร' and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds=10)
        await message.channel.send('ควยไรสัส ' + str(message.author.name))
    elif message.content == '!Logout':
        await bot.logout()  
    await bot.process_commands(message)

@bot.command()
async def play(ctx,* ,search):
   await songInstance.play(ctx, search)

@bot.command()
async def stop(ctx):
    await songInstance.stop(ctx)

@bot.command()
async def pause(ctx):
    await songInstance.pause(ctx)

@bot.command()
async def resume(ctx):
    await songInstance.resume(ctx)

@bot.command()
async def leave(ctx):
    await songInstance.leave(ctx)

@bot.command()
async def queueList(ctx):
    await songInstance.queueList(ctx)

@bot.command()
async def skip(ctx):
    await songInstance.skip(ctx)







bot.run('OTMwNDY5NjY4NTkyOTQ3MjMw.Yd2VaA.ePefyCpMRqJl-SMr3dWVz8k9crs') 
    
