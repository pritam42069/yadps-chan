import asyncpg, asyncio
from handler.config.data import Data
from handler.logging.log import Log


class Sql:

    def __init__(self):
        self.data = Data()
        self.log = Log().create(__name__, self.data.config["databaseLog"])
        self.sql_data = {
            "database": self.data.config["sql_user"],
            "host": self.data.config["sql_host"],
            "port": self.data.config["sql_port"],
            "user": self.data.config["sql_user"],
            "pass": self.data.config["sql_pass"]
        }
        self.pool = None
        global signal
        for k, v in self.sql_data.items():
            if len(v) == 0:
                self.log.error(f"Config error: value for {k} is empty")
                signal = "empty"
            else:
                signal = "valid"
        asyncio.run(self.start(signal))

    async def start(self, signal=None):
        if signal == "valid" or signal is None:
            self.log.info("Starting PostgreSQL Pool")
            self.pool = await self.create_pool()

    async def create_pool(self):
        return await asyncpg.create_pool(
            f'postgresql://{self.sql_data["user"]}'
            f':{self.sql_data["pass"]}'
            f'@{self.sql_data["host"]}/'
            f'{self.sql_data["database"]}',
            min_size=0,
            max_size=5,
            max_queries=30,
            timeout=5,
            command_timeout=7,
            max_inactive_connection_lifetime=60
        )

    async def example_query(self, query):
        if self.pool is None:
            self.pool = await self.create_pool()
        async with self.pool.acquire() as connection:
            return await connection.fetch(query)
