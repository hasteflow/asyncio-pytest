from unittest.mock import MagicMock
import asyncio
import logging
import pytest

from person import PersonClass

logger = logging.getLogger(__name__)


loopid = None


class TestPersonClass(object):

    @pytest.mark.asyncio
    async def test_send_query_on_create(self):
        """Should send insert query to database on create()"""

        # Stub the database cursor
        database_cursor = MagicMock()

        # Stub the execute function with mocked results from the database
        execute_stub = MagicMock(return_value='future result!')
        # Wrap the stub in a coroutine (so it can be awaited)
        execute_coro = asyncio.coroutine(execute_stub)
        database_cursor.execute = execute_coro

        # Instantiate new person obj
        person = PersonClass(name='Johnny', cursor=database_cursor)

        # Call person.create() to trigger the database call
        person_create_response = await person.create()

        # Assert the response from person.create() is our predefined future
        assert person_create_response == 'future result!'
        # Assert the database cursor was called once
        execute_stub.assert_called_once_with(person.insert_sql, ('Johnny',))


    @pytest.mark.asyncio
    async def test_first_loop(self):
        global loopid

        await asyncio.sleep(3)
        loop = asyncio.get_event_loop()
        loopid = id(loop)


    @pytest.mark.asyncio
    async def test_second_first_loop(self):
        global loopid

        await asyncio.sleep(3)
        loop = asyncio.get_event_loop()
        assert id(loop) != loopid
