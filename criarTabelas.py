from App.dependencias.database import engine
from App.dependencias.config import setting


async def create_tables() -> None:
    from App.Model import __all_models

    print('Creating tables...')

    async with engine.begin() as conn:
        await conn.run_sync(setting.DBBaseModel.metadata.drop_all)
        await conn.run_sync(setting.DBBaseModel.metadata.create_all)


    print('Finished creating tables')


if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())