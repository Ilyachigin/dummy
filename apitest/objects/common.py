import logging
import requests
from time import sleep
from random import choice, randint
from string import ascii_lowercase

logger = logging.getLogger(__name__)
HEADERS = {"User-Agent": "requests"}  # solve issue with 406 status code


def get_request(url, error=False):
    answer = requests.get(url, headers=HEADERS)
    while answer.status_code == 429:
        sleep(5)  # server has a limit on the number of requests (429: Too Many Requests)
        answer = requests.get(url, headers=HEADERS)
    else:
        if error:
            return answer
        else:
            answer.raise_for_status()
            logger.info('Status code %s - OK' % answer.status_code)
            response = answer.json()
            logger.info('Response:' + str(response))
            return response


def post_request(url, data):
    logger.info('Request:' + str(data))
    answer = requests.post(url=url, json=data, headers=HEADERS)
    while answer.status_code == 429:
        sleep(5)  # server has a limit on the number of requests (429: Too Many Requests)
        answer = requests.post(url=url, json=data, headers=HEADERS)
    else:
        answer.raise_for_status()
        logger.info('Status code %s - OK' % answer.status_code)
        response = answer.json()
        logger.info('Response:' + str(response))
        return response


def random_number(n):
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return randint(start, end)


def random_word(m):
    return ''.join(choice(ascii_lowercase) for i in range(m))

