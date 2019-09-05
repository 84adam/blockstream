#!/usr/bin/env python3

# print the last 10 Bitcoin blocks mined
# includes height, hash/id, and timestamp (UTC)
# uses blockstream API
# based on prior art: https://github.com/pasquantonio/blockstream

# requires Python 3.6+ and the following packages
# just run `pip install {package_name}` before executing this script
import requests
import datetime
import numpy as np

BASE_URL = 'https://blockstream.info/api/'

def call_api(endpoint):
    """
    Build the API URL and request data
    :param str endpoint: specific api endpoint to hit
    :return response: server's reponse to the request
    """
    url = BASE_URL + endpoint
    try:  # try to get json data
        response = requests.get(url).json()
    except ValueError:  # if bytes, convert to str
        response = requests.get(url).content.decode('utf-8')
    except Exception as e:
        response = e
    return handle_response(response)
    
def handle_response(response):
    """
    Responses from blockstream's API are returned in json or str
    :param response: http response object from requests library
    :return response: decoded response from api
    """
    if isinstance(response, Exception):
        print(response)
        return response
    else:
        return response

def get_blocks(start_height=''):
    """
    Request the 10 newest blocks starting at tip (most recent)
    or at start_height (optional)
    :param str start_height: block height
    :return: a list of :class:`Block` objects
    """
    resource = f'blocks/{start_height}'
    response = call_api(resource)
    blocks = []
    for block in response:
        blocks.append(Block(block))
    return blocks

def btc_utc(ts):
    dt = datetime.datetime.fromtimestamp(ts)
    dt_date = f'{dt.year:04}/{dt.month:02}/{dt.day:02}'
    dt_time = f'{dt.hour:02}:{dt.minute:02}:{dt.second:02}'
    return f'{dt_date} {dt_time}'

def last_ten():
    last_ten = get_blocks()
    output = []
    header = f'{"HEIGHT":<9}{"HASH":<67}{"TIME (UTC)":<23}'
    output.append(header)
    for i in last_ten:
        output.append(i)
    return output

def print_last_ten():
    output = last_ten()
    for i in output:
        print(i)

class Block:
    """Bitcoin block utility class"""
    def __init__(self, block):
        self.id = block['id']
        self.height = block['height']
        self.version = block['version']
        self.timestamp = block['timestamp']
        self.tx_count = block['tx_count']
        self.size = block['size']
        self.weight = block['weight']
        self.merkle_root = block['merkle_root']
        self.previous_block_hash = block['previousblockhash']
        self.nonce = block['nonce']
        self.bits = block['bits']
    def __repr__(self):
        return f"{self.height} - {self.id} - {btc_utc(self.timestamp)}"
    
print_last_ten()
