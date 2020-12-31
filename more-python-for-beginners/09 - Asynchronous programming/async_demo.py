from timeit import default_timer
import aiohttp
import asyncio

async def load_data(session, delay):
    print(f'Starting {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed {delay} second timer')
        return text

async def main():
    # 타이머 시작
    start_time = default_timer()

    # 하나의 세션 생성
    async with aiohttp.ClientSession() as session:
        # 작업을 설정하고 실행
        two_task = asyncio.create_task(load_data(session, 2))
        three_task = asyncio.create_task(load_data(session, 3))

        # 다른 프로세싱 시뮬레이션
        await asyncio.sleep(1)
        print('Doing other work')

        # value 값들을 가져오기
        two_result = await two_task
        three_result = await three_task

        # 결과 출력
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(main())
