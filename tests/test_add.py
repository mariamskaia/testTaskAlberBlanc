import pytest

from helpers.connections import send_request

from helpers.test_data import *

test_data_success = success_add_data()
test_data_failure = failure_add_data()


@pytest.mark.asyncio
@pytest.mark.parametrize("payload", test_data_success)
async def test_add_success(payload):
    response = await send_request(payload)

    assert response is not None
    assert response['status'] == 'success'
    assert response['method'] == 'add'
    assert response['id'] == payload['id']


@pytest.mark.asyncio
@pytest.mark.parametrize("payload, failure_reason", test_data_failure)
async def test_add_failure(payload, failure_reason):
    response = await send_request(payload)

    assert response is not None
    assert response['status'] == 'failure'
    assert response['reason'] == failure_reason
    assert response['id'] == payload['id']
