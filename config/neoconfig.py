import yaml
import dotenv
from mypy.typeops import false_only


class NeoConfig:
    env_keys = ['TOKEN', 'SQL_HOST', 'SQL_PORT', 'SQL_USER', 'SQL_PASS', 'SQL_DB']
    yaml_file = 'settings/neo.yaml'

    def __init__(self):
        # Neo config vars read() will attach to
        # This isn't actually necessary but makes it resolvable in the source
        # So if you don't care about unresolved syntax errors remove all the definitions

        # neo:
        self.version = 0
        self.databaseEnabled = False
        self.mode = ""
        self.envFile = ""
        self.serverInfoFile = ""
        # neo

        # logData
        self.enableLogging = False
        self.botLog = ""
        self.databaseLog = ""
        self.commandLog = ""
        self.systemLog = ""
        self.testLog = ""
        # logData

        # commandData
        self.cogPath = ""
        self.userCog = ""
        self.modCog = ""
        self.adminCog = ""
        self.devCog = ""
        self.enableUserCommands = False
        self.enableModCommands = False
        self.enableAdminCommands = False
        self.enableDevCommands = False
        self.enableCommandWarnings = False
        self.enableCommandDebug = False
        # commandData

        # roleData
        self.guildId = 0
        self.memberRoleId = 0
        self.modRoleId = 0
        self.adminRoleId = 0
        self.devRoleId = 0
        # roleData

        self.read()

    def read(self):
        with open(self.yaml_file) as stream:
            y_dict = yaml.safe_load(stream)
            for block in y_dict.values():
                for key, value in block.items():
                    setattr(self, key, value)
            env = dotenv.dotenv_values(self.envFile)
            for v in self.env_keys:
                setattr(self, v.lower(), env.get(v.upper()))
