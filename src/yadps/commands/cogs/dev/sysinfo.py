import csv
import psutil
import cpuinfo
import disnake
import os
from disnake.ext import commands
from yadps.config.data import Data


class SysInfo(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Get the server information YADPS is hosted on. Support only for Linux at the moment.",
        aliases=['si']
    )
    @commands.has_any_role(
        data.devRoleId
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def sysinfo(self, interaction: disnake.ApplicationCommandInteraction):
        info = {}
        file = self.data.serverInfoFile
        mem_v = psutil.virtual_memory()
        mem_s = psutil.swap_memory()
        cpu = cpuinfo.get_cpu_info()
        if not os.path.isfile(file):
            await interaction.send(f"{file} doesn't exist inside settings.")
            return
        with open("settings/server.info", "r") as release_file:
            r = csv.reader(release_file, delimiter='=')
            for k, v in r:
                info.update({k: v})
        embed = disnake.Embed(title="System information", description="YADPS-Chan likes beef!")
        embed.add_field(name="Name", value=f"{info['PRETTY_NAME']}", inline=True)
        embed.add_field(name="Architecture / ID", value=info['ID'], inline=True)
        embed.add_field(name="Build Type", value=info['BUILD_ID'], inline=True)
        embed.add_field(name="CPU", value=cpu['brand_raw'], inline=True)
        embed.add_field(name="CPU Architecture", value=cpu['arch'], inline=True)
        embed.add_field(name="CPU Hz", value=f"{cpu['hz_actual_friendly']}", inline=True)
        embed.add_field(name="Max Memory", value=f"{self.scale_bytes_to_gb(mem_v.total):.1f}GB", inline=True)
        embed.add_field(name="Used Memory", value=f"{self.scale_bytes_to_gb(mem_v.used):.1f}GB", inline=True)
        embed.add_field(name="Max Swap", value=f"{self.scale_bytes_to_gb(mem_s.total):.1f}GB", inline=True)
        embed.add_field(name="Used Swap", value=f"{self.scale_bytes_to_gb(mem_s.used):.1f}GB", inline=True)
        await interaction.send(embed=embed)

    def scale_bytes_to_gb(self, bytes):
        return bytes / 1024 / 1024 / 1024

def setup(bot):
    bot.add_cog(SysInfo(bot))
