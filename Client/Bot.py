import datetime
import discord
from Settings import *
from discord.ext import commands
from discord import Option
from random import randint

intents = discord.Intents.all()

bot = commands.Bot(intents=intents,debug_guilds=CONFIG['debug_guilds'])

@bot.event
async def on_ready():
    print('----------------------------------------------------')
    print(f'\t\t`Logged in as {bot.user.name}`')
    print(f'\t\t`{bot.user.id}`')
    print('----------------------------------------------------')


@bot.slash_command(name='showavatar',description='Show your avatar')
@commands.cooldown(1,3,commands.BucketType.user)
async def show_avatar(ctx, *, user: Option(discord.User, default=None,required=False)):
    if user is None:
        user = ctx.author

    color = discord.Color(value=randint(0, 0xffffff))

    embed = discord.Embed(title=f'{user.name}\'s Avatar', color=color)
    embed.set_image(url=user.avatar)
    await ctx.respond(embed=embed)


@bot.event
async def on_application_command_error(ctx, error):
    if (error, commands.CommandOnCooldown):
        await ctx.respond(f'You are on cooldown for {round(error.retry_after)} seconds')
    else:
        raise error



"""
Load all modules
"""
for filename in os.listdir('./Modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'Modules.{filename[:-3]}')
        print(f'[INFO] Loaded Module: {filename[:-3]}')

else:
    print('[modules is empty]')

bot.run(CONFIG['token'])