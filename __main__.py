import sys

import disnake

from handler.bot.yadps import Yadps

if __name__ == "__main__":
    if sys.version_info[0:2] != (3, 10):
        print(
            f"Python version must be minimum 3.10. Currently detected version: "
            f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)
    yadps = Yadps(test_guilds=[956780366063095808], intents=disnake.Intents.default())
    yadps.run(yadps.data.config["token"])