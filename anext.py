import asyncio

async def async_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10

async def main():
    async for item in async_generator():
        print(item)

asyncio.run(main())
