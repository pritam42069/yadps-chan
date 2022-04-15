from disnake.ext import commands
from yadps.config.data import Data
import disnake


class Ping(commands.Cog):

    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(description="Ping bot")
    @commands.has_any_role(
        data.memberRoleId
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.send("Pong!")


def setup(bot):
    bot.add_cog(Ping(bot))
