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

    """# conntent to LOCAL DB
    bot.connection = Connection(CONFIG['host'],CONFIG['port'])
    if bot.connection.isOnline():
        print('\t\t`Connected to local DB`')
    else:
        print('\t\t`Could not connect to local DB`')"""

    #TODO LATER


@bot.slash_command(name='showavatar',description='Show your avatar')
@commands.cooldown(1,3,commands.BucketType.user)
async def show_avatar(ctx, *, user: Option(discord.User, default=None,required=False)):
    if user is None:
        user = ctx.author

    color = discord.Color(value=randint(0, 0xffffff))

    embed = discord.Embed(title=f'{user.name}\'s Avatar', color=color)
    embed.set_image(url=user.avatar)
    await ctx.respond(embed=embed)


@bot.slash_command(name='setvc',description='Sets [create Voice channel]')
async def set_vc(ctx,*,vc: Option(discord.VoiceChannel, default=None, required=True)):
    if vc is None:
        await ctx.respond('`No Voice Channel provided`')
        return
    await ctx.respond(f'`Setting {vc.name} as Create Voice Channel`')
    #TODO LATER set VC in local DB
    await ctx.respond(f'`{vc.name} is now [the Create Voice Channel]`')


@bot.slash_command(name='setcategory',description='Sets [voice channel category]')
async def set_category(ctx,*,category: Option(discord.CategoryChannel, default=None, required=False)):
    if category is None:
        #TODO LATER set category from local DB if set_vc is set
        await ctx.respond('`No Category provided`')
        return

    await ctx.respond(f'`Setting {category.name} as Voice Channel Category`')
    #TODO LATER set category in local DB

@bot.slash_command(name='limitactivevc',description='Sets [active voice channel per user limit]')
async def limit_active_vc(ctx,*,amount: Option(int, default=None, required=True,choices=list(range(1,6)))):
    if amount is None:
        await ctx.respond('`No amount provided`')
        return

    await ctx.respond(f'`Setting {amount} as Active Voice Channel per User Limit`')
    #TODO LATER set amount in local DB
    await ctx.respond(f'`{amount} is now the Active Voice Channel per User Limit`')


@bot.event
async def on_application_command_error(ctx, error):
    if (error, commands.CommandOnCooldown):
        await ctx.respond(f'You are on cooldown for {round(error.retry_after)} seconds')
    else:
        raise error



"""
Load all modules
"""
for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'modules.{filename[:-3]}')
        print(f'[INFO] Loaded Module: {filename[:-3]}')

if len(os.listdir('./modules')) < 1:
    print('[INFO] No modules found')

bot.run(CONFIG['token'])