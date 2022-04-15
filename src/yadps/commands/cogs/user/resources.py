import disnake
from disnake.ext import commands
from yadps.config.data import Data
import yaml


class Resource(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Send a link in resources channel, will be verified by mods first.",
    )
    @commands.has_any_role(
        data.memberRoleId
    )
    @commands.cooldown(1, 15*30, commands.BucketType.guild)
    async def resource(self, inter: disnake.ApplicationCommandInteraction, link: str, subject: str):
        embed = disnake.Embed(
            title=inter.author,
            description=f"Link: {link}\nSubject: {subject}\nDate: {inter.created_at.strftime('%d-%m-%y')}\nTime: {inter.created_at.strftime('%H:%M %p')}"
        )
        channel = await self.bot.fetch_channel(956780367694659589)
        await channel.send(embed=embed)
        # await inter.send(embed=embed)
        embed = disnake.Embed(
            title="Submitted",
            description="Thanks for submitting a resource! It will be posted in the resources channel after being approved."
        )
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Resource(bot))
