
# --- 

import os
import requests
import json
import base64
import time
import hmac
import hashlib

import pandas as pd
from urllib.parse import urlencode
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# load keys from environment
from connectors.config import *
env_binance_api_key = os.environ["BINANCE_API_KEY"]
env_binance_secret_key = os.environ["BINANCE_SECRET_KEY"]

BASE_URL = "https://api.binance.com"

# --- ------------------------------------------------------------------- --- #

def get_server_time(server_url:str):
    """
    a simple REST API type of call to retrieve a remote's server time
    
    Args:
        server_url: str
            url string to query the time
            e.g. "https://api.binance.com/api/v1/time"
    
    Returns:
        The time as known by the server 

    Raises:
        TypeError: if server_url is not str
    
    """

    # Get the current time from the Binance's Server
    servertime = requests.get(server_url)
    servertimeobject = json.loads(servertime.text)
    servertime = servertimeobject['serverTime']

    return servertime

def get_timestamp():
    return int(time.time() * 1000)

# --- ------------------------------------------------------------------- --- #

def sign_params(params, timestamp, secret):
    """
    """ 

    # Sort the parameters by their keys
    params["timestamp"] = timestamp
    
    # Encode the parameters in urlencoding
    encoded_params = urlencode(params)

    # Sign the payload (params)
    signed_params = hmac.new(secret.encode('utf-8'),
                             encoded_params.encode('utf-8'),
                             hashlib.sha256).hexdigest()
 
    return signed_params
    

# --- ------------------------------------------------------------------- --- #
def account_info():
    """
    Get the account information
    """

    pass


# --- ------------------------------------------------------------------- --- #
def new_order():
    """
    place a new order
    """

    pass


# --- ------------------------------------------------------------------- --- #
def query_order():
    """
    get the available info for a given order
    """

    pass

# --- ------------------------------------------------------------------- --- #
def cancel_order():
    """
    cancel a given order
    """

    pass


# --- ------------------------------------------------------------------- --- #
def cancel_all_orders():
    """
    cancel all open orders for a particular symbol
    """

    pass


# --- ------------------------------------------------------------------- --- #
def get_all_orders():
    """
    get all orders (open, filled, cancelled) for a given instrument in a 
    given period of time
    """

    pass

# --------------------------------------------------------------------------- #
 
KEY = os.environ["BINANCE_API_KEY"]
SECRET = os.environ["BINANCE_SECRET_KEY"]
BASE_URL = "https://api.binance.com"
HASH_METHOD = hashlib.sha256

def hashing(query_string,
            encoding_type:str = "utf-8",
            hash_method:object = HASH_METHOD):
    """
    """

    encoded_secret = SECRET.encode(encoding_type)
    encoded_string = query_string.encode(encoding_type)
    r_hased = hmac.new(encoded_secret, encoded_string, hash_method)
    
    return r_hased.hexdigest()

def get_timestamp():
    return int(time.time() * 1000)


def dispatch_request(http_method):
    """
    """

    session = requests.Session()
    session.headers.update(
        {"Content-Type": "application/json;charset=utf-8", "X-MBX-APIKEY": KEY}
    )
    return {
        "GET": session.get,
        "DELETE": session.delete,
        "PUT": session.put,
        "POST": session.post,
    }.get(http_method, "GET")


def send_signed_request(http_method, url_path, payload={}):
    """
    """

    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = "timestamp={}".format(get_timestamp())

    url = (
        BASE_URL + url_path + "?" + query_string + "&signature=" + hashing(query_string)
    )
    print("{} {}".format(http_method, url))
    params = {"url": url, "params": {}}
    response = dispatch_request(http_method)(**params)
    return response.json()


# used for sending public data request
def send_public_request(url_path, payload={}):
    query_string = urlencode(payload, True)
    url = BASE_URL + url_path
    if query_string:
        url = url + "?" + query_string
    print("{}".format(url))
    response = dispatch_request("GET")(url=url)
    return response.json()

