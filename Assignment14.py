import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)

try:
    logging.debug("Program started")

    a = 10
    b = 2

    result = a / b
    logging.info("Division performed successfully")

    print("Result:", result)

    x = 10
    y = 0

    result2 = x / y

except ZeroDivisionError:
    logging.error("Division by zero error occurred")

finally:
    logging.info("Program execution completed")
