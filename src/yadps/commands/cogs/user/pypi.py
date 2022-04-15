import disnake
import requests
from disnake.ext import commands
from yadps.config.data import Data


class PyPi(commands.Cog):
    data = Data()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.slash_command(
        description="Get information on a pypi package.",
    )
    @commands.has_any_role(
        data.memberRoleId
    )
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def pypi(self, inter: disnake.ApplicationCommandInteraction, package):
        url = "https://pypi.org/pypi"
        r = requests.get(f"{url}/{package}/json")
        if r.status_code == 200:
            r_json = r.json()['info']
            embed = disnake.Embed(
                title=f"{package} v{r_json.get('version')}",
                description=f"{r_json.get('summary')}"
            )
            fields = {
                'Author': 'author',
                'Author Email': 'author_email',
                'Discontinued': 'yanked',
                'Keywords': 'keywords',
                'Bugs': 'bugtrack_url',
                'Project URL': 'project_url',
            }
            for name, value in fields.items():
                if r_json.get(value):
                    embed.add_field(name, r_json.get(value))
            await inter.send(embed=embed)
        else:
            await inter.send(f"{url}/{package}/json returned {r.status_code} reason: {r.reason}")


def setup(bot):
    bot.add_cog(PyPi(bot))
