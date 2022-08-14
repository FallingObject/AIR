# imports

import os
import json
from pathlib import Path
from typing import Optional
from pydantic import BaseModel
import requests


# Path to the settings file && CONFIG FILE
path = Path(__file__).parent.parent.absolute()
CONFIG = json.load(open(os.path.join(path,'config.json')))

class VoiceChannel(BaseModel):
    vc_id: int
    vc_name: Optional[str] = "{$member.name}'s Voice Channel"

class Member(BaseModel):
    member_id: int
    voiceChannels: Optional[list] = [] # list of VoiceChannel


class VoiceManager(BaseModel):
    voiceChannels: Optional[list] = [] # list active of VoiceChannel
    join_create_voice_channel_id: int = None
    voice_channel_log_id: int = None
    voice_channel_category_id: int = None # default if going to be autmatically adjusted to same Category as [join_create_voice_channel_id]
    active_voice_channel_per_user_limit: int = 2 # to prevent spamming

class GreatingManager(BaseModel):
    join_channel_id: int = None
    join_message: str = "Welcome {$member.name} to {$member.guild.name}"

    leave_channel_id: int = None
    leave_message: str = "Goodbye {$member.name} from {$member.guild.name}"
    
    greating_log_channel_id: int = None


class Guild:
    guild_id: int
    voice_manager: VoiceManager
    greating_manager: GreatingManager
    members: Optional[list] = [] # list of Member

class Connection:
    def __init__(self,host,port) -> None:
        self.host = host
        self.port = port

    def isOnline(self) -> bool:
        r = requests.get(f'http://{self.host}:{self.port}')
        if r.status_code != 200:
            return False
        return r.json()['data']

    def getGuilds(self) -> list:
        r = requests.get(f'http://{self.host}:{self.port}/guilds')
        return r.json()['data']

    def getGuild(self,guild_id) -> Guild:
        r = requests.get(f'http://{self.host}:{self.port}/guilds/{guild_id}')
        return r.json()['data']

    def getVoiceManager(self,guild_id) -> VoiceManager:
        r = requests.get(f'http://{self.host}:{self.port}/guilds/{guild_id}/voice_manager')
        return r.json()['data']

    def getGreatingManager(self,guild_id) -> GreatingManager:
        r = requests.get(f'http://{self.host}:{self.port}/guilds/{guild_id}/greating_manager')
        return r.json()['data']

    def setVoiceManager(self,guild_id,voice_manager) -> dict:
        r = requests.put(f'http://{self.host}:{self.port}/guilds/{guild_id}/voice_manager',json=voice_manager)
        return r.json()['data']

    def setGreatingManager(self,guild_id,greating_manager) -> dict:
        r = requests.put(f'http://{self.host}:{self.port}/guilds/{guild_id}/greating_manager',json=greating_manager)
        return r.json()['data']

    def getMembers(self,guild_id) -> list:
        r = requests.get(f'http://{self.host}:{self.port}/guilds/{guild_id}/members')
        return r.json()['data']

    def getMember(self,guild_id,member_id) -> Member:
        r = requests.get(f'http://{self.host}:{self.port}/guilds/{guild_id}/members/{member_id}')
        return r.json()['data']

    def setMember(self,guild_id,member_id,member) -> dict:
        r = requests.put(f'http://{self.host}:{self.port}/guilds/{guild_id}/members/{member_id}',json=member)
        return r.json()['data']

    def getVoiceChannels(self,guild_id) -> list:
        r = requests.get(f'http://{self.host}:{self.port}/guilds/{guild_id}/voice_channels')
        return r.json()['data']

    def getVoiceChannel(self,guild_id,voice_channel_id) -> VoiceChannel:
        r = requests.get(f'http://{self.host}:{self.port}/guilds/{guild_id}/voice_channels/{voice_channel_id}')
        return r.json()['data']

    def setVoiceChannel(self,guild_id,voice_channel_id,voice_channel) -> dict:
        r = requests.put(f'http://{self.host}:{self.port}/guilds/{guild_id}/voice_channels/{voice_channel_id}',json=voice_channel)
        return r.json()['data']
