import asyncio
import time

import disnake
from handler.config.data import Data
from disnake.ext import commands


class Reminders(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Send a message to a channel reminding to bump every 2 hours.",
        hidden=True
    )
    @commands.has_any_role(
        data.config["adminRoleId"]
    )
    async def bump(self, interaction: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel):
        start_time = time.time()
        if not isinstance(channel, disnake.TextChannel):
            await interaction.send("You must supply a text channel.")
            return
        await interaction.send(f"Enabling bump reminders on channel: {channel.mention}")
        embed = disnake.Embed(
            title="Bump us!",
            description="""
            Bumping helps the server grow. You can bump a server every 2 hours.
            To bump a server, type `/bump`. You can also go [here](https://disboard.org/server/956780366063095808) to bump us!
            Note that `/bump` is a slash command and not a text based command.
            """
        )
        while True:
            await channel.send(embed=embed, delete_after=2*60*60)
            await asyncio.sleep(2*60*60)



def setup(bot):
    bot.add_cog(Reminders(bot))
