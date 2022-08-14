from email.policy import default
from optparse import Option
import discord
from discord.ext import commands
from discord import SlashCommandGroup,slash_command
global cc

voice = SlashCommandGroup("voice","voice related commands")

class VoiceManager(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot

    """
    VoiceManager

    This cog is responsible for managing voice channels.
    """
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after) -> None:
        print(f'\n\n MEMBER: {member} \n\n BEFORE: {before}\n\n AFTER: {after}')


    @discord.slash_command()
    async def hello(self,ctx):
        await ctx.respond('Hello World')
    

    @slash_command()
    async def bye(self,ctx):
        await ctx.respond('Bye World')

    @voice.command(name="join",description="Joins a voice channel")
    async def join(self,*,channel:discord.VoiceChannel=None):
        if channel is None:
            return
        await self.respond(f'Joined {channel.name}')

    @voice.command(name="leave",description="Leaves a voice channel")
    async def leave(
        self,
        *,
        channel:Option(discord.VoiceChannel,name="channel",required=True)
        ):
        if channel is None:
            return
        await self.respond(f'Left {channel.name}')

def setup(bot: discord.bot) -> None:
    bot.add_cog(VoiceManager(bot))
    bot.add_application_command(voice)