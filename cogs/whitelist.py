import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
from tinydb import TinyDB, Query
from discord.errors import NotFound as not_found
from json import loads
import os

SUPERUSERS = loads(os.getenv("SUPERUSERS"))
print(SUPERUSERS)

db = TinyDB("servers.json")
server = Query()

class whitelist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_subcommand(base="whitelist", name="add", description="Add a server to the TNB whitelist", options=[create_option(name="invite_link", description="Server invite link to be whiteilisted.", option_type=3, required=True)])
    async def whitelist_add(self, ctx, invite_link):
        
        if ctx.author.id in SUPERUSERS:
            try:
                inv = await self.bot.fetch_invite(invite_link)
                if db.search(server.server_id == inv.guild.id):
                    await ctx.send("Already Whitelisted")
                else:
                    db.insert({'server_id': inv.guild.id, 'server_name': inv.guild.name.lower()})
                    await ctx.send("Server successfully whitelisted")
            except not_found:
                await ctx.send("Unknown Invite!")
        else:
            await ctx.send("You are not a superuser.", hidden=True)


    @cog_ext.cog_subcommand(base="whitelist", name="remove", description="Remove a server from the TNB whitelist", options=[create_option(name="server_id", description="Server ID to remove from the whitelist.", option_type=3, required=True)])
    async def whitelist_remove(self, ctx, server_id):

        if ctx.author.id in SUPERUSERS:
            if server_id.isnumeric():
                if db.search(server.server_id == int(server_id)):
                    db.remove(server.server_id == int(server_id))
                    await ctx.send("Server successfully removed from the whitelist")
                else:
                    await ctx.send("Server not present in the whitelist")
            else:
                await ctx.send("Invalid Server id")
        else:
            await ctx.send("You are not a superuser.", hidden=True)

    @cog_ext.cog_subcommand(base="whitelist", name="all", description="List of all Whitelisted servers")
    async def whitelist_all(self, ctx):

        if len(db.all()) > 0:
            embed = discord.Embed(title="List of Whitlisted Servers", description="List of Whitlisted Servers with server IDs", colour=discord.Color.blue())

            for i in db.all()[:8]:
                embed.add_field(name=i["server_name"].capitalize(), value=i["server_id"], inline=False)

        else:
            embed = discord.Embed(title="No Whitelisted servers!!", description="No whitelisted servers as of now, check back later", colour=discord.Color.blue())

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(whitelist(bot))