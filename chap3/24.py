from time import sleep
from datetime import datetime
from typing import Optional

def log_typed(message: str, when: Optional[datetime]=None) -> None:

    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time. (동적인 디폴트 값)
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

# def log(message, when=datetime.now()):
#     print(f'{when}: {message}')
#
log_typed('Hi there!')
# sleep(0.1)
# log('Hello again!')