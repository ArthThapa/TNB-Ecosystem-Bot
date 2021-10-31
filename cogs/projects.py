import discord
from discord import colour
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option
import requests
from DiscordUtils.Pagination import AutoEmbedPaginator


class projects(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_subcommand(base="project", name="all", description="List of all TNB Projects")
    async def project_all(self, ctx):

        await ctx.defer(hidden=False)

        req = requests.get("https://api.thenewboston.com/projects")
        data = req.json()

        if data["results"]:

            n = 8
            raw = [data["results"][i * n:(i + 1) * n] for i in range((len(data["results"]) + n - 1) // n )]
            pagination_list = []

            for i in raw:
                embed = discord.Embed(name="TNB Projects", description="TNB Projects", colour=discord.Colour.blue())
                for j in i:
                    embed.add_field(name=f"{j['title']}", value=f"{j['project_lead_display_name']}", inline=False)

                pagination_list.append(embed)

            paginator = AutoEmbedPaginator(ctx)
            await paginator.run(pagination_list)    

    @cog_ext.cog_subcommand(base="project", name="show", description="Know more about a specifc TNB project", options=[create_option(name="project_name", option_type=3, required=True, description="Name of TNB project (Should be precise)")])
    async def project_show(self, ctx, project_name):

        await ctx.defer(hidden=False)

        req = requests.get("https://api.thenewboston.com/projects")
        data = req.json()

        if data["results"]:

            found = False

            for project in data["results"]:
                if project["title"] == project_name:

                    found = True
                    embed = discord.Embed(title=f"{project['title']}", description=f"{project['overview']}", colour=discord.Colour.blue())
                    embed.add_field(name="Problem", value=f"{project['problem']}")
                    embed.add_field(name="Benefits", value=f"{project['benefits']}")

                    embed.set_author(name=f"{project['project_lead_display_name']}", url=f"{project['github_url']}", icon_url=f"{project['logo']}")
                    break

            if found:
                await ctx.send(embed=embed)
            else:
                await ctx.send("Project Not Found!!")

        else:
            await ctx.send("Project Not Found!!")


def setup(bot):
    bot.add_cog(projects(bot))