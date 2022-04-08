from typing import Any
import disnake
from handler.logging.log import Log
from handler.config.data import Data
from handler.database.sql import Sql
from handler.commands.controller import CommandController
from disnake.ext import commands


class Yadps(commands.Bot):
    data = Data()
    bot_log = Log().create(__name__, data.config["botLog"])

    def __init__(self, **options: Any):
        super().__init__(**options)
        self.bot_log.info("Initing yadps-chan")
        self.command_controller = CommandController
        if self.data.config["sql_enabled"]:
            self.sql = Sql()
        if self.data.config["token"] == "":
            self.bot_log.error("Token not found!")
            exit(1)
        self.bot_log.info("Valid .env configuration detected")

    async def on_ready(self):
        self.bot_log.info("yadps-chan is connected")

    async def on_message(self, interaction: disnake.ApplicationCommandInteraction):
        if interaction.author == self.user:
            return

    async def on_slash_command(self, inter):
        self.bot_log.info(f"Slash command: {inter.data.name} invoked by {inter.author}")

    async def on_slash_command_completion(self, inter):
        self.bot_log.info(f"Slash command: {inter.data.name} invoked by {inter.author} successful")

    async def on_slash_command_error(self, interaction: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingAnyRole):
            if self.data.config["enableCommandWarnings"]:
                self.bot_log.warning(f"{interaction.author} is missing roles for command: {interaction.data.name}")
            if self.data.config["enableCommandDebug"] or self.data.config["mode"] == "development":
                self.bot_log.debug(
                    f"Command -> {interaction.data.name} | Invoked from -> {interaction.channel_id} | By user"
                    f"-> {interaction.author} | Error -> {interaction.author} missing roles")
            await interaction.send(
                f"{interaction.author.mention}, you don't have the required permissions for this command.")

