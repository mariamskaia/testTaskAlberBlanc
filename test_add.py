import pytest
import websockets
import asyncio
import json

@pytest.mark.asyncio
async def test_add():
    uri = "ws://app:4000"
    async with websockets.connect(uri) as ws:
        await ws.send('{"id": "12345", "method": "add", "name": "Jack", "surname": "Dorris", "phone": "2128507", "age": 30}')
        repl = await ws.recv()
        resp = json.loads(repl)
        print(resp)
        assert resp["id"] == "12345"
        assert resp["method"] == "add"
        assert resp["status"] == "success"

asyncio.get_event_loop().run_until_complete(test_add())

