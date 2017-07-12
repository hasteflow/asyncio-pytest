
import asyncio

# One method on this class is an asyncio coroutine.
class PersonClass(object):

    def __init__(self, name=None, cursor=None):
        """Constructor for PersonClass."""
        self.name = name
        self.cursor = cursor
        self.insert_sql = 'INSERT INTO person VALUES ?;'


    async def create(self):  # ....HOW TO TEST THIS METHOD??
        """Persist the person to the database."""
        return await self.cursor.execute(self.insert_sql, (self.name,))
        # await asyncio.sleep(0)
