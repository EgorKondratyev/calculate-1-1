from logger.create_logger import logger


def foo(first_num: int = 0, second_num: int = 0) -> int:
    return first_num + second_num


if __name__ == '__main__':
    my_first_number = foo(1, 1)

    logger.debug(my_first_number)