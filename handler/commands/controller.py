from handler.config.data import Data
from handler.logging.log import Log
import os


class CommandController:
    data = Data().read()
    command_log = Log().create(__name__, data.command_log)
    total_loaded = 0

    def __init__(self, bot):
        self.bot = bot

    def init(self):
        self.command_log.info("Initing commands")
        self.load()

    def load(self):
        if self.data.dev_commands:
            self.set_command_state(self.data.dev_cog, 'load')
        if self.data.admin_commands:
            self.set_command_state(self.data.admin_cog, 'load')
        if self.data.mod_commands:
            self.set_command_state(self.data.mod_cog, 'load')
        if self.data.user_commands:
            self.set_command_state(self.data.user_cog, 'load')
        self.command_log.info(f"Total commands loaded: {self.total_loaded}")

    def set_command_state(self, module, state, command=None):
        path_string = self.data.cog_path + '.' + module
        if command and isinstance(command, str):
            arg = {path_string + '.' + command}
            getattr(self.bot, "%s_extension" % state)(*arg)
        else:
            for cmd in os.listdir(self.data.cog_path.replace('.', '/') + '/' + module):
                if cmd.endswith('.py'):
                    arg = {path_string + '.' + cmd[:-3]}
                    getattr(self.bot, "%s_extension" % state)(*arg)
                    self.total_loaded += 1

    def get_command_ranks(self) -> list:
        path = self.data.cog_path.replace(".", "/")
        ranks = []
        for dir in os.listdir(path):
            ranks.append(dir)
        return ranks

    def get_command_list(self, rank=None) -> list:
        path = self.data.cog_path.replace(".", "/")
        commands = []
        if rank:
            for file in os.listdir(path + "/" + rank):
                if file.endswith(".py"):
                    commands.append(file.replace(".py", ""))
            return commands
        if rank is None:
            for dir in os.listdir(path):
                for file in os.listdir(path + "/" + dir):
                    if file.endswith(".py"):
                        commands.append(file.replace(".py", ""))
            return commands
