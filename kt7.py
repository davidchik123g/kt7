import asyncio
import aiohttp
import pytest


async def get_plus(x, y):
    await asyncio.sleep(3)
    return x + y


@pytest.mark.asyncio
async def test_get_plus(event_loop):
    result = await get_plus(66, 3)
    assert result == 69


async def valueerror():
    await asyncio.sleep(3)
    value = int("da")
    return int


@pytest.mark.asyncio
async def test_valueerror(event_loop):
    with pytest.raises(ValueError):
        await valueerror()


async def get_code(code):
    url = f"http://numbersapi.com/#{code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return code


@pytest.mark.asyncio
async def test_get_code():
    code = await get_code(43)
    assert code == 43


asyncio.run(test_get_code())
