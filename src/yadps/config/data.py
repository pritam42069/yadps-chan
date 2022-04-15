import yaml
import dotenv

class Data:

    env_keys = ['TOKEN', 'SQL_HOST', 'SQL_PORT',
                     'SQL_USER', 'SQL_PASS', 'SQL_DB']
    yaml_file = 'settings/yadps.yaml'

    def __init__(self):
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

