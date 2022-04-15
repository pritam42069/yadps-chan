import disnake
from disnake.ext import commands
from yadps.config.data import Data
import yaml


class Tag(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Show a tag.",
    )
    @commands.has_any_role(
        data.memberRoleId
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def tag(self, inter: disnake.ApplicationCommandInteraction, tag: str=None):
        with open('settings/tags.yaml') as file:
            tags = yaml.load(file, Loader=yaml.loader.Loader)
        if not tag:
            embed = disnake.Embed(
                title="All tags",
                description="\n".join([i for i in tags['tags']])
            )
            await inter.send(embed=embed)
            return
        try:
            embed = disnake.Embed(
                title=tags['tags'][tag]['title'],
                description=tags['tags'][tag]['description']
            )
            await inter.send(embed=embed)
        except KeyError:
            embed = disnake.Embed(
                title="That tag doesn't exist"
            )
            await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Tag(bot))
