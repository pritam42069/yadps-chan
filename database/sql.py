import asyncpg
from config.neoconfig import NeoConfig
from logger.log import Log

class Sql:
    def __init__(self):
        self.data = NeoConfig()
        self.log = Log().create(__name__, self.data.databaseLog)
        self.loaded = False

    async def start(self, signal=None):
        if signal == "valid" or signal is None:
            self.log.info("Starting PostgreSQL Pool")
            self.pool = await self.create_pool()
            self.loaded = True

    async def create_pool(self):
        return await asyncpg.create_pool(
            f'postgresql://{self.data.sql_user}'
            f':{self.data.sql_pass}'
            f'@{self.data.sql_host}/'
            f'{self.data.sql_db}',
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

    async def send_transaction(self):
        async with self.pool.acquire as connection:
            async with connection.transaction():
                await connection.execute("TRANSACTION_QUERY")
