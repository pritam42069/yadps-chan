import disnake
from disnake.ext import commands
from yadps.config.data import Data


class Lore(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Add lore to the mighty guild.",
    )
    @commands.has_any_role(
        data.adminRoleId
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def lore(self, inter: disnake.ApplicationCommandInteraction, title, desc, image_url):
        lore_embed = disnake.Embed(
            title=title,
            description=desc,
        )
        if len(image_url) != 0:
            lore_embed.set_image(url=image_url)
        await inter.send(embed=lore_embed)


def setup(bot):
    bot.add_cog(Lore(bot))