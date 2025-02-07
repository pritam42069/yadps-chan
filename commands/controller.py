import os
from config.neoconfig import NeoConfig
from logger.log import Log

class CommandController:
    data = NeoConfig()
    command_log = Log().create(__name__, data.commandLog)
    total_loaded = 0

    _state_load = "load"
    _state_reload = "reload"
    _state_unload = "unload"

    def __init__(self, bot):
        self.bot = bot

    def load_cmds(self):
        if self.data.enableDevCommands:
            self.set_cog_state(self.data.devCog, self._state_load)
            if self.data.enableCommandDebug:
                self.command_log.info("Developer commands loaded")
        if self.data.enableAdminCommands:
            self.set_cog_state(self.data.adminCog, self._state_load)
            if self.data.enableCommandDebug:
                self.command_log.info("Admin commands loaded")
        if self.data.enableModCommands:
            self.set_cog_state(self.data.modCog, self._state_load)
            if self.data.enableCommandDebug:
                self.command_log.info("Moderator commands loaded")
        if self.data.enableUserCommands:
            self.set_cog_state(self.data.userCog, self._state_load)
            if self.data.enableCommandDebug:
                self.command_log.info("User commands loaded")
        self.command_log.info(f"Total commands loaded: {self.total_loaded}")

    def set_cog_state(self, module, state):
        path_string = self.data.cogPath + '.' + module
        for cmd in os.listdir(path_string.replace('.', os.path.sep)):
            if cmd.endswith('.py') and cmd != "__init__.py":
                getattr(self.bot, "%s_extension" % state)(*{path_string + f".{cmd[:-3]}"})
                self.total_loaded += 1

    def set_command_state(self, cog, state, command: str):
        cog = self.data.cogPath + '.' + cog
        for cmd in os.listdir(cog.replace('.', os.path.sep)):
            if cmd != "__init__.py" and cmd == command:
                getattr(self.bot, "%s_extension" % state)(*{cog + f".{command[:-3]}"})
