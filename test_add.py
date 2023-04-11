import pytest
from helpers.connections import *


@pytest.mark.asyncio
async def test_add():
    request_data = '{"id": "12egwe", "method": "add", "name": "Jack1", "surname": "Dorris1", "phone": "21285071", "age": 31}'
    response = await send_request(request_data)
    assert response["id"] == "12egwe"
    assert response["method"] == "add"
    assert response["status"] == "success"

@pytest.mark.asyncio
async def test_add_duplicate():
    request_data = '{"id": "123456", "method": "add", "name": "Jack", "surname": "Dorris", "phone": "2128507", "age": 30}'
    response = await send_request(request_data)

    assert response["id"] == "123456"
    assert response["method"] == "add"
    assert response["status"] == "failure"

