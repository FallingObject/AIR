import discord
from discord.ext import commands


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