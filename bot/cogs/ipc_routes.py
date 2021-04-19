
from discord.ext import commands, ipc

from bot.data import Data

class Fun(commands.Cog):


    def __init__(self, bot):
      
        self.bot=bot

    
    @ipc.server.route()

    async def get_guild_ids(data):

        return [guild.id for guild in bot.guilds]

    @ipc.server.route()

    async def get_guild_info(data):

        guild = await bot.fetch_guild(data.guild_id)

        guild_info = {"name": guild.name, "icon_url": str(guild.icon_url)}

        return guild_info
