from loguru import logger


def main() -> int:
    """
    Runs main.

    Returns:
        Constant value of 42.
    """
    logger.info("Hello from pybase!")
    return 42


if __name__ == "__main__":
    main()
