import sys
import unittest
import dotenv
import yaml
from schema import Schema, SchemaError
from handler.logging.log import Log
from handler.config.data import Data


class TestActions(unittest.TestCase):
    data = Data()
    log = Log().create(__name__, data.config["botLog"])

    def test_assertPythonVersion(self):
        self.assertTrue(sys.version_info[0:2] == (3, 10))

    def assertTokenExists(self):
        def token_exists() -> bool:
            settings_file = "settings/.env"
            env = dotenv.dotenv_values(settings_file)
            if "TOKEN" not in env:
                self.log.error(f"Key: TOKEN not found in {settings_file}")
                return False
            if len(env.get("TOKEN")) == 0:
                self.log.error("Empty value for key TOKEN")
                return False
            if len(env.get("TOKEN")) != 59:
                self.log.error(f"Token has incorrect length. Expected: 59. Got: {len(env.get('TOKEN'))}")
                return False
            return True
        self.assertTrue(token_exists())

    def test_assertValidConfig(self):
        def valid_yaml() -> bool:
            yadps_schema = Schema({
                "yadps": {
                    "version": str,
                    "databaseEnabled": bool,
                    "mode": str,
                    "envFile": str,
                },
                "logData": {
                    "enableLogging": bool,
                    "botLog": str,
                    "databaseLog": str,
                    "commandLog": str,
                    "systemLog": str,
                },
                "commandData": {
                    "cogPath": str,
                    "userCog": str,
                    "modCog": str,
                    "adminCog": str,
                    "devCog": str,
                    "enableUserCommands": bool,
                    "enableModCommands": bool,
                    "enableAdminCommands": bool,
                    "enableDevCommands": bool,
                    "enableCommandWarnings": bool,
                    "enableCommandDebug": bool,
                },
                "roleData": {
                    "guildId": int,
                    "memberRoleId": int,
                    "modRoleId": int,
                    "adminRoleId": int,
                    "devRoleId": int,
                }
            })
            with open("settings/yadps.yaml", 'r') as stream:
                y = yaml.safe_load(stream)
            try:
                yadps_schema.validate(y)
                return True
            except SchemaError as err:
                self.log.error(err)
                return False
        self.assertTrue(valid_yaml())
