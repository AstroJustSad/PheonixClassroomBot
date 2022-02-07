#important v8.91 is set for 19 of Eb 2022
from cProfile import label
from tabnanny import check
import discord
import distutils
import random
import os 
import re
import datetime
from discord.ext import commands
from discord.ext import tasks
from distutils import command
from turtle import color, title
from unicodedata import name 
from asyncio import sleep as s
from discord.utils import get




#get data
import datafile
from datafile import Imagedata
from datafile import Imagedata2
from datafile import Gifdata
from datafile import rating
from datafile import ballresponses
from datafile import banembed
from datafile import description
from datafile import botimage
from datafile import bs
from datafile import botver
from datafile import color1
from datafile import lyrics
from datafile import url

#get commands 
import commands1
from commands1 import h,hv,w,wv,g,gv,m,mv,r,rv,p,pv,E,Ev


#bot code
#Version 8.90
cilent = commands.Bot (command_prefix=commands.when_mentioned_or('-'))
cilent.remove_command('help')

#help command for the bot 
@cilent.command('help')
async def help (ctx):
    random_color=random.choice(color1)
    embed=discord.Embed (tilte='Pheonix classroom',description=description,color=random_color)
    embed.add_field(name=h,value=hv,inline=True)
    embed.add_field(name=w,value=wv,inline=True)
    embed.add_field(name=m,value=mv,inline=True)
    embed.add_field(name=g,value=gv,inline=True)
    embed.add_field(name=p,value=pv,inline=True)
    embed.add_field(name=E,value=Ev,inline=True)
    embed.add_field(name=r,value=rv,inline=True)
    embed.set_thumbnail(url=botimage)
    embed.set_footer(text=f'Developed by TechSupport.Org. Version {botver}')
    await ctx.send(embed=embed)

#ready
@cilent.event
async def on_ready():
    botstatus=random.choice(bs)
    await cilent.change_presence(status=discord.Status.dnd,activity=discord.Game(botstatus))
    print('Client online')
 


#join
@cilent.event 
async def on_member_join(member:discord.Member):
    print(f'{member}has joined the server.')
   
#leave
@cilent.event 
async def on_member_remove(member):
    print(f'{member}has left the server.')

#kick ban v1.1
#need to fix embed gif that shows up in next update v8.99
@cilent.command(aliases=['B'])
async def ban(ctx,member:discord.Member, * ,reason='was struck by the ban Hammer'):
    random_color=random.choice(color1)
    embed=discord.Embed(title='User Ban',description=member.mention,color=random_color())
    embed.add_field(name='Member',value=reason,inline=True)
    embed.set_image(url=banembed)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)
    await member.ban(reason=reason)
    
@cilent.command()
async def hello(ctx):
    helloEmbed = discord.Embed(title="Hello :wave:", description=f"Hi there {ctx.author.mention}", color = ctx.author.color)
    helloEmbed.set_thumbnail(url=f"{ctx.author.avatar_url}")
    helloEmbed.set_footer(icon_url=f"https://lh3.googleusercontent.com/xuwBaIy4dCq95kX2cEMq_6GnB6Ed2B3imfZW4UQvUlo2MGMy2QiCAfm7r6BNj2jAeA=h200", text="By Pheonix Bot @ 2022")

    await ctx.send(embed=helloEmbed)
    

@cilent.command(description="Give direct access links for students.")
async def dlink(ctx):
    dlinkEmbed = discord.Embed(title="Direct Links", description=f"Give direct links for students to easily navigate", color = ctx.author.color)
    dlinkEmbed.add_field(name="Pheonix Classroom - ", value="https://bit.ly/3uLryiT")
    dlinkEmbed.add_field(name="Mindspark - ", value="https://bit.ly/3HzS6qy")
    dlinkEmbed.set_footer(icon_url=f"https://lh3.googleusercontent.com/xuwBaIy4dCq95kX2cEMq_6GnB6Ed2B3imfZW4UQvUlo2MGMy2QiCAfm7r6BNj2jAeA=h200", text="By Pheonix Bot @ 2022")

    await ctx.send(embed=dlinkEmbed)
    
    
@cilent.command(alieases=['K'])
async def kick(ctx,member:discord.Member, *,reason='was removed from the server'):
    random_color=random.choice(color1)
    embed=discord.Embed(title='User kick',description=member.mention,color=random_color)
    embed.add_field(name='Member',value=reason,inline=True)
    embed.set_image(url=banembed)
    embed.set_thumbnail(url=member.avatar_url)
    await member.kick(reason=reason)
    await ctx.send(embed=embed)


#whois v1.3
@cilent.command(aliases=['user','info'])
async def whois(ctx,*,member:discord.Member):
    random_color=random.choice(color1)
    
    embed=discord.Embed (title=member.display_name,description=member.mention,color=random_color)
    embed.add_field(name='House',value= member.top_role,inline=True)
    embed.add_field(name='Joined at',value=member.joined_at,inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url,text=f'Requested by {ctx.author.display_name} ')
    await ctx.send(embed=embed)



#meme command (do not touch, there are rick rolls ) v1.7
@cilent.command()
async def meme(ctx):
    random_color=random.choice(color1)
    embed=discord.Embed(color=random_color)
    random_link2=random.choice(Imagedata2)
    random_link1=random.choice(Imagedata)
    images=[random_link1,
            random_link2]

    random_link=random.choice(images)
    embed.set_image(url=random_link)
    await ctx.send(embed=embed)


@cilent.command()
async def gif(ctx):
    random_color=random.choice(color1)
    embed=discord.Embed(color=random_color)

    
    randomgif_link=random.choice(Gifdata)
    images=[randomgif_link]

    random_link=random.choice(images)
    embed.set_image(url=random_link)
    await ctx.send(embed=embed)

 
#ping
@cilent.command()
async def ping(ctx):
    await ctx.send (f'Pong Your ping is {round(cilent.latency *1000)}ms.'
    '\n If your ping is above 600 your definitly on airtel')


#announce 
@cilent.command()
async def announce(ctx, channel: discord.TextChannel, * ,message):
    await ctx.send('Loading')
    await channel.send(f'{message}')
    await ctx.send('Sent!')


#8ball v1.01
@cilent.command(aliases=['8ball','8b',])
async def eightball(ctx, * ,question):   
    
    await ctx.send(f':8ball: Question:{question}\n:8ball: Answer: {random.choice(ballresponses)}')

#member rater 
@cilent.command()
async def rate(ctx):
    random_color=random.choice(color1)
    embed=discord.Embed(title='Your rating:',description=f'{random.choice(rating)}',color=random_color)
    embed.set_footer(icon_url= ctx.author.avatar_url,text=f'Requested by {ctx.author.display_name} ')
    await ctx.send(embed=embed)


#rick roll 
@cilent.command(aliases=['dm','Secret'])
async def r8ck(ctx):
    random_color=random.choice(color1)
    random_url=random.choice(url)
    random_line=random.choice(lyrics)
    embed=discord.Embed(tile='Your secret message:',description=random_line,color=(random_color))
    embed.set_image(url=random_url)
    embed.set_footer(icon_url=ctx.author.avatar_url,text='You Got Rick Rolled')
    await ctx.send(embed=embed)




cilent.run('')