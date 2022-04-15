#!/usr/bin/env python

from typing import Any
import disnake
from yadps.logging.log import Log
from yadps.config.data import Data
from yadps.database.sql import Sql
from yadps.commands.controller import CommandController
from test.test_actions import TestActions
from disnake.ext import commands


class Yadps(commands.Bot):
    test = TestActions()
    test.assertTokenValidity()
    test.assertValidConfig()
    data = Data()
    log = Log().create(__name__, data.botLog)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.log.info("YADPS-Chan is starting")
        self.command_controller = CommandController(self).load()
        if self.data.databaseEnabled:
            self.sql = Sql()
        else:
            self.log.warn("SQL IS DISABLED")

    async def on_ready(self):
        self.log.info("yadps-chan is connected")

    async def on_message(self, interaction: disnake.ApplicationCommandInteraction):
        if interaction.author == self.user:
            return

    async def on_slash_command(self, inter):
        if self.data.enableCommandDebug:
            self.log.debug(f"Slash command {inter.data.name} invoked by {inter.author} result -> {inter.data}")
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author}")

    async def on_slash_command_completion(self, inter):
        self.log.info(f"Slash command: {inter.data.name} invoked by {inter.author} successful")

    async def on_slash_command_error(self, interaction: disnake.ApplicationCommandInteraction, error):
        if isinstance(error, commands.MissingAnyRole):
            if self.data.enablecommandWarnings:
                self.log.warning(f"{interaction.author} is missing roles for command: {interaction.data.name}")
            if self.data.enableCommandDebug or self.data.mode == "development":
                self.log.debug(
                    f"Command -> {interaction.data.name} | Invoked from -> {interaction.channel_id} | By user"
                    f"-> {interaction.author} | Error -> {interaction.author} missing roles")
            await interaction.send(
                f"{interaction.author.mention}, you don't have the required permissions for this command.")
        self.log.error(error)

