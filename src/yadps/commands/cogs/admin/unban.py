from yadps.logging.log import Log
from yadps.config.data import Data
from disnake.ext import commands


class Unban(commands.Cog):

    data = Data()
    yadps_log = Log().create(__name__, data.botLog)


    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Unban a given user.",
        hidden=True
    )
    @commands.has_any_role(
        data.adminRoleId
    )
    async def unban(self, ctx, userid):
        user = await self.bot.fetch_user(userid)
        await ctx.guild.unban(user)
        self.yadps_log.warning(f"{user} has been unbanned!")
        await ctx.send(f"{user} is now unbanned.")


def setup(bot):
    bot.add_cog(Unban(bot))
