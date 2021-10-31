from discord.ext import commands
from discord.errors import NotFound as not_found
from tinydb import TinyDB, Query
import os
from discord_slash import SlashCommand
from re import findall
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TNB_DISCORD_TOKEN")
BOT_MANAGER_ID =os.getenv("BOT_MANAGER_ID")

url_define = 'discord(?:\.com|app\.com|\.gg)[\/invite\/]?(?:[a-zA-Z0-9\-]{2,32})'


bot = commands.Bot(command_prefix=">")
slash = SlashCommand(bot, sync_commands=True)

db = TinyDB("servers.json")
server = Query()

@bot.event
async def on_message(message):
    if findall(url_define, message.content):
        raw = findall(url_define, message.content)
        for i in raw:
            try:
                inv = await bot.fetch_invite(i)
                if db.search(server.server_id == inv.guild.id):
                    pass
                else:
                    await message.delete()
                    break
            except not_found:
                await message.delete()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@slash.slash(name="kill", description="Kill TNB Ecosystem Bot")
async def kill(ctx):
    if ctx.author.id == BOT_MANAGER_ID:
        await bot.close()
    else:
        await ctx.send("You are not the bot manager.")

bot.run(BOT_TOKEN)