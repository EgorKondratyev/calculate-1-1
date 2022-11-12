import asyncio

from logger.create_logger import logger


async def calculate(first_num: int = 0, second_num: int = 0) -> str:
    my_first_number = str(first_num) + str(second_num)
    logger.debug(my_first_number)
    return my_first_number


async def main():
    task_one = asyncio.create_task(
        calculate(1, 2)
    )

    await task_one


if __name__ == '__main__':
    asyncio.run(main())
