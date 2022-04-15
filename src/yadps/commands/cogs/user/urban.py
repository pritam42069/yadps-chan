from disnake.ext import commands
from yadps.config.data import Data
import disnake
import requests
from urllib.parse import urlencode, urlparse, urlunparse


class Urban(commands.Cog):

    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(description="Find the definition of something from urban dictionary.")
    @commands.has_any_role(
        data.memberRoleId
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def urban(self, inter: disnake.ApplicationCommandInteraction, query: str):
        parsed_url = list(
            urlparse("https://api.urbandictionary.com/v0/define"))
        parsed_url[4] = urlencode({"term": query})
        r = requests.get(
            urlunparse(parsed_url))
        data = r.json().get("list")
        if r.status_code == 404 or not data:
            embed = disnake.Embed(
                title="404, Not Found",
                description="Your query was not found."
            )
            await inter.send(embed=embed)
            return
        elif r.status_code == 200:
            embed = disnake.Embed()
            data = data[0]
            if data.get("word"):
                embed.title = data.get("word")
            if data.get("definition"):
                embed.description = data.get(
                    "definition").replace("[", "").replace("]", "")
            if data.get("example"):
                embed.add_field("Example", data.get("example").replace("[", "").replace("]", ""))
            await inter.send(embed=embed)
            return
        embed = disnake.Embed(title=f"Something went wrong, {r.status_code}")
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Urban(bot))
