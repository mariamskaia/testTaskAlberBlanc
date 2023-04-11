import websockets
import json

import websockets.connection

uri = "ws://app:4000"


async def send_request(request_data):
    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps(request_data))
        repl = await ws.recv()
        response = json.loads(repl)
        print(response)

        if not ws.close:
            ws.close()

        return response
