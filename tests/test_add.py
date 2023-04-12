import pytest

from helpers.connections import send_request
from helpers.test_data import *


@pytest.mark.asyncio
@pytest.mark.parametrize("payload", success_data())
async def test_add_success(payload):
    response = await send_request(payload)

    assert response is not None
    assert response['status'] == 'success'
    assert response['method'] == 'add'
    assert response['id'] == payload['id']


@pytest.mark.asyncio
@pytest.mark.parametrize("payload, failure_reason", failure_data())
async def test_add_failure(payload, failure_reason):
    response = await send_request(payload)

    assert response is not None
    assert response['status'] == 'failure'
    assert response['reason'] == failure_reason
    assert response['id'] == payload['id']
