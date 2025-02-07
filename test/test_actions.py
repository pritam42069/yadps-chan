import sys
import unittest
import dotenv
import yaml
from schema import Schema, SchemaError
from logger.log import Log
from config.neoconfig import NeoConfig


class TestActions(unittest.TestCase):
    data = NeoConfig()
    log = Log().create(__name__, "logs/test.logs")

    def test_assertPythonVersion(self):
        self.assertTrue(sys.version_info[0:2] == (3, 10))

    def assertTokenValidity(self):
        global token
        settings_file = "settings/.env"
        env = dotenv.dotenv_values(settings_file)
        if len(env) != 0:
            if not env["TOKEN"]:
                self.log.error("Key: TOKEN not found or is empty")
                self.fail()
            else:
                token = env["TOKEN"]
            #if len(token) != 59:
            #    self.log.error(f"Incorrect TOKEN length. Characters found: {len(token)} expected: 59")
            #    self.fail()
            # Token length seems to be changing between 59 -> 70, can't assert this test
        else:
            self.log.error("Invalid env file!")
            self.fail()

    def assertValidConfig(self):
        neo_schema = Schema({
            "neo": {
                "version": str,
                "databaseEnabled": bool,
                "mode": str,
                "envFile": str,
                "serverInfoFile": str,
            },
            "logData": {
                "enableLogging": bool,
                "botLog": str,
                "databaseLog": str,
                "commandLog": str,
                "systemLog": str,
                "testLog": str,
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
        with open("settings/neo.yaml", 'r') as stream:
            y = yaml.safe_load(stream)
        try:
            neo_schema.validate(y)
        except SchemaError as err:
            self.log.error(err)
            self.fail()
